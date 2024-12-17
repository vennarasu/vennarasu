import numpy as np
import cv2
import dlib

# Connect to your computer's default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the coordinates
detector = dlib.get_frontal_face_detector()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    frame = cv2.flip(frame, 1)

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Counter to count number of faces
    i = 0
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (255, 255, 255), 2)

        # Increment the iterator each time you get the coordinates
        i += 1

        # Adding face number to the box detecting faces
        cv2.putText(frame, 'face num ' + str(i), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 240, 0), 2)
        print(face, i)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Enter key 'q' to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
