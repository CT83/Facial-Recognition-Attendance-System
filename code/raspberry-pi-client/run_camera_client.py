import os
import time
from pprint import pprint

import requests

from CONSTANTS import CURRENT_IMAGE_FILE, FACE_API_KEY, FACE_BASE_URL, DEFAULT_PERSON_GROUP, CAPTURE_INTERVAL, \
    REST_SERVER_URL
from camera.Camera import Camera
from face.FaceAPIWrapper import FaceAPIWrapper
from utils import get_lecture_number


def add_person(person_name, image_urls, person_group=DEFAULT_PERSON_GROUP):
    print("Name:", person_name)
    print("Images:", image_urls)
    face_api = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)
    person_id = face_api.create_person(person_group=person_group, person_name=person_name)  # Save this
    print("IMP! PERSON_ID for", person_name, "is", person_id)

    for image_url in image_urls:
        time.sleep(5)
        face_api.add_faces_to_person(person_group=person_group,
                                     person_id=person_id, image_url=image_url)
        print("Adding ", image_urls.index(image_url), "of ", len(image_urls))

    face_api.train_group(person_group)
    print("Started Training", person_group, "...")
    return person_name, person_id


def initial_setup():
    person_group = DEFAULT_PERSON_GROUP

    face_api = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)
    pprint(face_api.list_groups())

    face_api.delete_group(person_group)
    face_api.create_group(person_group)

    person_and_images = [
        ("Tanmay Sawant", "face/images/Tanmay_Sawant/"),
        ("Rohan Sawant", "face/images/Rohan_Sawant/"),
        ("Peter Hook", "face/images/Peter_Hook/"),
    ]
    person_id_dict = {}
    for person_name, images_dir in person_and_images:
        name, id = add_person(person_name,
                              [os.path.join(images_dir, f) for f in
                               os.listdir(images_dir)],
                              person_group=person_group)
        person_id_dict[id] = name
    pprint(person_id_dict)

    # image_urls = os.listdir("images/Rohan_Sawant/train")


def main():
    image_file = CURRENT_IMAGE_FILE
    person_group_id = DEFAULT_PERSON_GROUP
    camera = Camera()
    face_api_wrapper = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)

    time_face_id_dict = {
        'lecture_number': get_lecture_number(),
        'face_ids': ["e376f233-70b3-4b70-a30e-44b7990192bd",
                     "810as202ff-6f6sa-4582-a3sa7f97eb67ad"]
    }

    r = requests.post(REST_SERVER_URL + 'time-face-id', data={
        'lecture_number': get_lecture_number(),
        'face_ids': [{"e376f233-70b3-4b70-a30e-44b7990192bd"},
                     {"810as202ff-6f6sa-4582-a3sa7f97eb67ad"}]
    })
    print(r)

    print("Capturing Image every ", CAPTURE_INTERVAL)

    # while 1:
    #     image = camera.capture_image()
    #     cv2.imwrite(image_file, image)
    #     cv2.imshow("Camera Image", image)
    #     cv2.waitKey(1)
    #     face_ids = face_api_wrapper.detect_faces(image=image_file)
    #     if face_ids:
    #         # TODO Send the face id to server here.
    #         identified_person_id = \
    #             face_api_wrapper.identify_face(face_ids=face_ids,
    #                                            large_person_group=person_group_id)
    #         if identified_person_id:
    #             try:
    #                 pass
    #             except IndexError as ie:
    #                 pass
    #     time.sleep(CAPTURE_INTERVAL)


if __name__ == '__main__':
    # initial_setup()
    main()
