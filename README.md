# Face Emotion Detection
Computer Vision system that is capable of detecting the emotion from the face in the input image/video feed in real time.

![image](https://github.com/theingale/face_emotion_detection/assets/98829449/f1b01a17-d622-454c-bb20-22acd2861acc)

## Installation Steps:

1. Clone the repo in your local system
   <pre> git clone https://github.com/theingale/face_emotion_detection.git </pre>
2. Create Python 3.8 Virtual Environment
   <pre> conda create -p ./venv python=3.8 -y </pre>
3. Activate virtual Environment
   <pre> conda activate ./venv </pre>
6. Install dependancies
7. <pre> pip install -r requirements.txt </pre>
8. Download trained VGG19 Model File
   <pre> Model Download Link: https://drive.google.com/file/d/1gE1lvbFz_gC5L4dcrg93qRur47vzuFy0/view?usp=sharing</pre>
10. Paste the downloaded model at location app_data/emotion_model/
    <pre> Model path: app_data\emotion_model\emotion_model_VGG19.hdf5  </pre>
12. Run the emotion_detector_app script
    <pre> python emotion_detector_app.py </pre>
14. Let your Webcam know your Emotions...!
   

