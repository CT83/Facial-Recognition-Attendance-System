import os
import time

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL
from face.FaceAPI_Wrapper import FaceAPI_Wrapper

key = FACE_API_KEY
base_url = FACE_BASE_URL

# image_urls = os.listdir("images/Rohan_Sawant/train")
image_urls = [os.path.join("images/Rohan_Sawant/train", f) for f in os.listdir("images/Rohan_Sawant/train")]
print("Images:", image_urls)

person_group = 'allowed_persons'
person_name = 'Rohan Sawant'

face_api = FaceAPI_Wrapper(key, base_url)
print(face_api.list_groups())
face_api.delete_group(person_group)
face_api.create_group(person_group)
person_id = face_api.create_person(person_group=person_group, person_name=person_name)  # Save this
print("PERSON_ID for", person_name, "is", person_id)
for image_url in image_urls:
    time.sleep(5)
    face_api.add_faces_to_person(person_group=person_group,
                                 person_id=person_id, image_url=image_url)
    print("Training ", image_urls.index(image_url), "of ", len(image_urls))
face_api.train_group(person_group)
print("Started Training", person_group, "...")
