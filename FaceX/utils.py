# Importing of necessary modules
import cv2

# Initializing the masks array that  will store user masks
masks = ["example.jpg"]

def create_mask(image_file):
    print('Function allowing a user to create a mask')

def assign_mask(image_file):
    print('This function will add a mask to a users face')

# Function that extracts faces and returns them in a JSON format
def extract_faces(image_file):
    faces_detected = []
    cascasdepath = "haarcascade_frontalface_default.xml"
    gray = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cascasdepath)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Loop through all faces in image and save them
    for (x, y, w, h) in faces:
        cuttout_region = cv2.rectangle(image_file, (x, y), (x + h, y + h), (0, 255, 0), 2)
        faces_detected.append(cuttout_region)
    
    # Check if faces are present before response
    if (faces_detected) > 0:
        # Format faces response
        faces_response_formatted = {
            status:"success",
            num_faces_found: len(faces),
            faces: faces_detected
        }
    else:
        faces_response_formatted = {
            status: "failed",
            response: "There where no faces detected"
        }
    # Return all faces detected
    return faces_response_formatted
        
# Function that cuts the image in half horizontally
def cropImage(image_file):
    height,width,depth = image_file.shape
    return [image_file[height//2 , :width] , x[height//2, width:]]
