import cv2
import sys

# Provide a dummy image path
imagePath = './img2.jpeg'

# Load the image
image = cv2.imread(imagePath)
if image is None:
    print("Could not open or find the image.")
    sys.exit(1)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the face cascade classifier
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Detect faces in the grayscale image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

# Print the number of faces found
print("[INFO] Found {0} Faces!".format(len(faces)))

# Draw rectangles around the detected faces
for i, (x, y, w, h) in enumerate(faces):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Face {} found. Saving locally.".format(i+1))
    cv2.imwrite('detected/face{}_{}.jpg'.format(i+1, str(w) + str(h)), roi_color)

# Save the result image with rectangles
status = cv2.imwrite('faces_detected1.jpg', image)
if status:
    print("[INFO] Image faces_detected.jpg written to filesystem.")
else:
    print("[ERROR] Failed to write the image to filesystem.")

# Display the image (optional)
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()