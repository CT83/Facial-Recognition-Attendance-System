import os
import time

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL, FACE_GROUP_ID
from face.FaceAPIWrapper import FaceAPIWrapper


def setup_persons(names_of_person, delete_existing=False):
    person_id_name = {}
    person_group = FACE_GROUP_ID
    face_api = FaceAPIWrapper(FACE_API_KEY, FACE_BASE_URL)

    if delete_existing:
        face_api.delete_group(person_group)
        face_api.create_group(person_group)

    for person_name in names_of_person:
        person_id = face_api.create_person(person_group=person_group, person_name=person_name)  # Save this

        image_urls = [os.path.join("images/" + person_name + "/train/", f)
                      for f in os.listdir("images/" + person_name + "/train/")]

        for image_url in image_urls:
            time.sleep(5)
            face_api.add_faces_to_person(person_group=person_group,
                                         person_id=person_id, image_url=image_url)
            print("Training ", image_urls.index(image_url), "of ", len(image_urls))
        face_api.train_group(person_group)
        person_id_name[person_name] = person_id

    return person_id_name


def main():
    person_id_name = setup_persons(["Tanmay Sawant", "Rohan Sawant", "Anirudh Iyer"])

    for id, name in person_id_name.items():
        print(name, "'s ID is", id)


if __name__ == '__main__':
    main()
