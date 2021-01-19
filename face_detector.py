import cv2

face_cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, img_test = capture.read()
    gray = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    face = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img_test, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img_test', img_test)

    k = cv2.waitKey(30) & 0xff
    if k==27:
          break

capture.release()