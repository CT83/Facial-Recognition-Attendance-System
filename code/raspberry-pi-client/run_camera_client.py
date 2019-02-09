import time

import cv2
import requests

from CONSTANTS import CURRENT_IMAGE_FILE, FACE_API_KEY, FACE_BASE_URL, CAPTURE_INTERVAL, \
    REST_SERVER_URL, FACE_GROUP_ID
from camera.Camera import Camera
from face.FaceAPIWrapper import FaceAPIWrapper
from utils import get_lecture_number


def main():
    image_file = CURRENT_IMAGE_FILE
    person_group_id = FACE_GROUP_ID
    camera = Camera()
    camera.start_capture()
    face_api_wrapper = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)

    print("Capturing Image every ", CAPTURE_INTERVAL)

    i = 0

    while 1:
        try:
            image = camera.current_frame.read()
            cv2.imwrite(image_file, image)
            cv2.imshow("Camera Image", image)
            cv2.waitKey(1)
            face_ids = face_api_wrapper.detect_faces(image=image_file)
            i += 1
            print(i, "Captured at ", time.time())
            if face_ids:
                print("Detected Faces...")
                person_ids = \
                    face_api_wrapper.identify_faces(face_ids=face_ids,
                                                    large_person_group=person_group_id)
                req_ids = [{id} for id in person_ids]

                requests.post(REST_SERVER_URL + 'time-face-id', data={
                    'lecture_number': get_lecture_number(),
                    'face_ids': req_ids
                })
                print("Present IDs:", req_ids)

            time.sleep(CAPTURE_INTERVAL)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # initial_setup()
    main()
