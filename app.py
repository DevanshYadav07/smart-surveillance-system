from flask import Flask, Response, render_template
import cv2
from playsound import playsound
app = Flask(__name__)
import requests
# import twilio
# from twilio.rest import Client
# Load the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



# regin of interest
top_left = (150, 150)
bottom_right = (450, 450)

# Open the camera
cap = cv2.VideoCapture(0)

frequency = 2500
duration = 1000
# Set the alarm duration in seconds
alarm_duration = 5

account_sid="ACbbbe08628a31e86c22d0ef947a27a508"
auth_token="1f366b5226c2f3b727cc484cf22c3714"


# client=Client(account_sid,auth_token)
# sending the image to user by devansh
to_whatsapp_number='whatsapp:+917300789205'

def generate_frames():
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw rectangle for area of interest
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 3)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            
            # Save the image
            if x > top_left[0] and y > top_left[1] and x + w < bottom_right[0] and y + h < bottom_right[1]:
                filename = "intruder.jpg"
                cv2.imwrite(filename, frame)
                # twilio sms alert
                # message=client.messages.create(
                # body="Alert Intrusion detected at your premise",
                # from_="+16816801434",
                # to="+917300789205"
                # )

            
                print("INTRUDER ALERT")
                playsound('Beep.mp3')
                # # sending the image to user by devansh
                # mes=client.messages.create(
                #     from_='whatsapp:+14155238886',
                #     body='Intrusion detected using python',
                #     to=to_whatsapp_number
                    
                # )
                # # # image url
                # image_url='http://127.0.0.1:5000/intruder.jpg'
                # Response=requests.get(image_url)

                # client.messages.create(
                #     from_='whatsapp:+14155238886',
                #     body='tejus is theif',
                #     media_url=Response.url,
                #     to=to_whatsapp_number

                # )
        # Return the frame to the webpage
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
