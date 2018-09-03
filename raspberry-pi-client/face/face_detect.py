import os

import cognitive_face as CF
import cv2

KEY = '36dfa79442044ade81d2e14cf5de659c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'images/class4.jpg'
img_url = "images/Tanmay_Sawant/test/IMG_20180801_141310.jpg"
if not os.path.isfile(img_url):
    raise FileNotFoundError

detected_faces = CF.face.detect(img_url,
                                attributes='age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise')

print(detected_faces)
image_result = cv2.imread(img_url)
print("Number of faces:", len(detected_faces))
cv2.rectangle(image_result, (0, 0), (36, 36), color=(215, 245, 225), thickness=3)
for face in detected_faces:
    face_rectange = face['faceRectangle']

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (face_rectange['left'], face_rectange['top'])
    fontScale = 3
    fontColor = (255, 255, 255)
    lineType = 3
    print(face)
    cv2.putText(image_result, str(face['faceAttributes']['gender']) + str(face['faceAttributes']['age']),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)

    cv2.rectangle(image_result,
                  (face_rectange['left'], face_rectange['top']),
                  (face_rectange['left'] + face_rectange['width'], face_rectange['top'] + face_rectange['height']),
                  color=(215, 245, 225), thickness=3)
cv2.imshow("Detected Faces", cv2.resize(image_result, (1200, 900)))
cv2.waitKey()
