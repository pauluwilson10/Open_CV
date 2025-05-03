import numpy as np
import cv2 as cv

# Load the Haar Cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# List of people (labels)
people = ['Ben Affleck', 'Elton John', 'Jerry Seinfeld', 'Madonna', 'Mindy Kaling']

# Load the pre-trained LBPH face recognizer model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Read the input image
img = cv.imread(r"C:\Users\Paulu wilson\Desktop\college\Open cv\Faces\val\elton_john\3.jpg")

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

# Process each detected face
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    # Predict the label and confidence for the face region of interest
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    # Draw a rectangle around the detected face and add a label
    cv.putText(img, str(people[label]), (20,20 ), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the detected image with annotations
cv.imshow("Detected Image", img)

# Wait for a key press and close the image window
cv.waitKey(0)
cv.destroyAllWindows()
