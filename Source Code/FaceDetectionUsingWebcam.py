import cv2

faceCascade = cv2.CascadeClassifier("cascade.xml") #name of the xml file created after training the images

cam = cv2.VideoCapture(0)  #inbuilt opencv command to capture video

while True:
    success, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect face
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
