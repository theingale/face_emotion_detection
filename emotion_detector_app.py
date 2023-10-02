from tensorflow.keras.models import load_model
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN 

# Load trained VGG19 Model for Emotion Detection
emotion_model = load_model('app_data\emotion_model\emotion_model_VGG19.hdf5', compile=False)

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: 'Neutral'}

# Create MTCNN for face Detection in Video feed
face_detector = MTCNN()

# start the webcam feed
cap = cv2.VideoCapture(0)
black = np.zeros((96,96))

# Reference: https://saturncloud.io/blog/opening-web-camera-in-google-colab/#:~:text=Opening%20the%20Web%20Camera,a%20camera%20or%20a%20file.

while True:
    # Webcam feed reading
    ret, frame = cap.read()
    if not ret:
        break
	
    # detect faces in the image
    results = face_detector.detect_faces(frame)
	# extract the bounding box from the first face
    if len(results) == 1: #len(results)==1 if there is a face detected. len ==0 if no face is detected
        try:
            # Get first face
            x1, y1, width, height = results[0]['box']
            x2, y2 = x1 + width, y1 + height
        	
            # extract the face
            face = frame[y1:y2, x1:x2]
            
            #Draw a rectangle around the face
            cv2.rectangle(frame, (x1, y1), (x1+width, y1+height), (255, 0, 0), 2)
            
            # resize pixels to the model size
            cropped_img = cv2.resize(face, (48,48)) 
            cropped_img = np.expand_dims(cropped_img, axis=0)
            cropped_img = cropped_img.astype(float)
            prediction = emotion_model.predict(cropped_img)
            print(prediction)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x1+20, y1-60), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        except:
            pass
    cv2.imshow('Video',frame)
    try:
        cv2.imshow("frame", cropped_img)
    except:
        cv2.imshow("frame", black)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()