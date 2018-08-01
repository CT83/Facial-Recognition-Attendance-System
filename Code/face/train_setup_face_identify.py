import os
import time

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL, FACE_GROUP_ID, FACE_PERSON_ID_NAME_DICT
from face.FaceAPI_Wrapper import FaceAPI_Wrapper

key = FACE_API_KEY
base_url = FACE_BASE_URL

# image_urls = os.listdir("images/Rohan_Sawant/train")
image_urls = [os.path.join("images/Tanmay_Sawant/", f) for f in os.listdir("images/Tanmay_Sawant/")]
print("Images:", image_urls)

person_group = 'allowed_persons'
person_name = 'Tanmay Sawant'

face_api = FaceAPI_Wrapper(key, base_url)
print(face_api.list_groups())


# face_api.delete_group(person_group)
# face_api.create_group(person_group)
# person_id = face_api.create_person(person_group=person_group, person_name=person_name)  # Save this
# print("PERSON_ID for", person_name, "is", person_id)
# for image_url in image_urls:
#     time.sleep(5)
#     face_api.add_faces_to_person(person_group=person_group,
#                                  person_id=person_id, image_url=image_url)
#     print("Training ", image_urls.index(image_url), "of ", len(image_urls))
# face_api.train_group(person_group)
# print("Started Training", person_group, "...")


def identify_person_in_image(image_path):
    face_api = FaceAPI_Wrapper(FACE_API_KEY, FACE_BASE_URL)

    face_ids = face_api.detect_faces(image=image_path)
    if not face_ids:
        return None
    identified_person_id = face_api.identify_face(face_ids=face_ids,
                                                  large_person_group=FACE_GROUP_ID)
    if identified_person_id:
        try:
            person_name = FACE_PERSON_ID_NAME_DICT[identified_person_id]
        except IndexError as ie:
            person_name = None
        return person_name
    else:
        return None


test_image_urls = [os.path.join("images/Tanmay_Sawant/test", f) for f in os.listdir("images/Tanmay_Sawant/test")]
print("Test Images:", test_image_urls)
for test_image_url in test_image_urls:
    print("Person in Image is :", identify_person_in_image(test_image_url))
    time.sleep(2)
