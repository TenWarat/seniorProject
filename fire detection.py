import cv2
from playsound import playsound
import smtplib
import datetime

date = datetime.datetime.now()

email_adress = 'python.tenwarat@gmail.com'
email_password = 'Ten28209'




# fired detection
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')  # load classifier from a file

cap = cv2.VideoCapture('Candle Flame Stock Footage - ToobStock- Free Stock Video of Fire!.mp4')#  0 is Webcam ,can be replace by video file

while True:

    ret, frame = cap.read()                               # Read a classifier from ()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)   # Detect object of diif type of input img

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected",date)

        # sending email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_adress, email_password)

            subject = 'fire is detected'
            body = ' fire is detected !!!'
            time = date
            msg = f'Subject:{subject}\n\n{body}\n{time}'

            smtp.sendmail(email_adress, 'facelessten@gmail.com', msg)
            #smtp.sendmail(email_adress, 'dragonhello18@gmail.com', msg)

        #playsound('audio.mp3')

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break