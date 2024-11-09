import cv2

# Load the face detection cascade classifier
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Read the image
img = cv2.imread('image.jpg')

# Check if the cascade classifier file is loaded successfully
if face_cascade.empty():
    print("Error: Unable to load the cascade classifier file.")
    exit()

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load the image file.")
    exit()

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

# Check if any faces are detected
if len(faces) == 0:
    print("No faces detected in the image.")
    exit()

# Draw rectangles around the detected faces and save the image
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img)

# Print a success message
print('Successfully saved the image with detected faces.')