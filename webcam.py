from flask import Flask, render_template,Response
import cv2
from app.file_main import app
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:

        success,frame =  camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg', frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n' 
                       b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')



@app.route('/hoa')
def index():
    return render_template('layout/user.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)