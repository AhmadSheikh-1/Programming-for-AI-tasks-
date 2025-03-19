from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
    [5, 107, 0, 19, 255, 255],    
    [133, 56, 0, 159, 156, 255],   
    [57, 76, 0, 100, 255, 255],    
    [90, 48, 0, 118, 255, 255]     
]

myColorValues = [
    [51, 153, 255],  
    [255, 0, 255],   
    [0, 255, 0],     
    [255, 0, 0]      
]

myPoints = []

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)

        if x != 0 and y != 0:
            newPoints.append([x, y, count])
            cv2.circle(img, (x, y), 15, myColorValues[count], cv2.FILLED)

        count += 1
    return newPoints

def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y

def generate_frames():
    while True:
        success, img = cap.read()
        if not success:
            break

        newPoints = findColor(img, myColors, myColorValues)
        if newPoints:
            for newP in newPoints:
                myPoints.append(newP)

        for point in myPoints:
            cv2.circle(img, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
