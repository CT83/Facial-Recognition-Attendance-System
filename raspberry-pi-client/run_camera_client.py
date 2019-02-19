import os
import time

import boto3
import cv2
import requests

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL, CAPTURE_INTERVAL, \
    REST_SERVER_URL, FACE_GROUP_ID, CAMERA_NAME
from camera.Camera import Camera
from face.FaceAPIWrapper import FaceAPIWrapper
from utils import get_lecture_number


def upload_to_s3(key):
    print("Uploading file to S3...")
    bucket_name = 'fras-store'

    folder_name = "public_folder"
    output_name = folder_name + "/" + key
    location = 'us-east-1'

    s3 = boto3.client('s3')
    s3.upload_file(key, bucket_name, output_name, ExtraArgs={'ACL': 'public-read'})

    url = "https://s3.amazonaws.com/%s/%s/%s" % (bucket_name, folder_name, key)
    return url


def current_time_to_string():
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d_%H%M%S%f")


def create_dir_if_not_exists(output_dir):
    try:
        os.makedirs(output_dir)
    except OSError:
        if not os.path.isdir(output_dir):
            raise


def main():
    person_group_id = FACE_GROUP_ID
    display_image = False

    face_api_wrapper = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)
    create_dir_if_not_exists('temp_images/' + CAMERA_NAME)

    print("Capturing Image every ", CAPTURE_INTERVAL, " seconds...")

    i = 0

    while 1:
        try:
            image_filename = 'temp_images/' + CAMERA_NAME + "/" + current_time_to_string() + ".jpg"
            image = Camera().capture_image()
            cv2.imwrite(image_filename, image)

            if display_image:
                cv2.imshow("Camera Image", image)
                cv2.waitKey(1)

            image_link = upload_to_s3(image_filename)
            face_ids = face_api_wrapper.detect_faces(image=image_filename)
            i += 1
            print(i, "Captured at ", time.time())
            if face_ids:
                person_ids = \
                    face_api_wrapper.identify_faces(face_ids=face_ids,
                                                    large_person_group=person_group_id)
                req_ids = [{id} for id in person_ids]
                print("Detected Faces...", req_ids)

                requests.post(REST_SERVER_URL + 'time-face-id', data={
                    'lecture_number': get_lecture_number(),
                    'face_ids': req_ids,
                    'image-link': image_link,
                    'camera-name': CAMERA_NAME,
                })
                print("Present IDs:", req_ids)

            time.sleep(CAPTURE_INTERVAL)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # initial_setup()
    main()
