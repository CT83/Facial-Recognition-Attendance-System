import os

import cognitive_face as CF
from cognitive_face import CognitiveFaceException

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL


class FaceAPIWrapper:

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url

        CF.Key.set(self.key)
        CF.BaseUrl.set(self.base_url)

    @staticmethod
    def list_groups():
        res = CF.large_person_group.list()
        return res

    @staticmethod
    def create_group(person_group):
        """Will Silently fail if group already exists"""
        try:
            CF.large_person_group.create(person_group)
        except CognitiveFaceException as cfe:
            print(cfe)

    @staticmethod
    def delete_group(person_group):
        """Will Silently fail if group does not exist"""
        try:
            CF.large_person_group.delete(person_group)
        except CognitiveFaceException as cfe:
            print(cfe)

    @staticmethod
    def train_group(person_group):
        CF.large_person_group.train(person_group)

    @staticmethod
    def create_person(person_group, person_name):
        res = CF.large_person_group_person.create(person_group, person_name)
        person_id = res['personId']
        print("Person ID:", person_id, "| Person Name:", person_name)
        return person_id

    @staticmethod
    def add_faces_to_person(person_group, person_id, image_url):
        try:
            if os.path.isfile(image_url):
                print("Adding Image", image_url)
                persisted_face = CF.large_person_group_person_face.add(image_url,
                                                                       person_group, person_id)
                # print("Persisted Face:", persisted_face, "for ", image_url)
        except CognitiveFaceException as cfe:
            print(cfe)

    @staticmethod
    def detect_faces(image):
        detected_results = CF.face.detect(image,
                                          attributes="age,gender,smile,facialHair,glasses,emotion,makeup,accessories,occlusion,blur,exposure,noise")
        print("Detected Faces", detected_results)
        face_ids = []
        for result in detected_results:
            face_ids.append(result['faceId'])
        return face_ids

    @staticmethod
    def detect_face(image):
        res = CF.face.detect(image)
        return res

    @staticmethod
    def identify_faces(face_ids, large_person_group,
                       person_group_id=None, max_candidates_return=1,
                       threshold=None):
        identify_results = CF.face.identify(face_ids,
                                            large_person_group_id=large_person_group,
                                            person_group_id=person_group_id,
                                            max_candidates_return=max_candidates_return,
                                            threshold=threshold
                                            )
        person_ids = []

        for identify_result in identify_results:
            for candidate in identify_result['candidates']:
                person_id = candidate['personId']
                person_ids.append(person_id)

        return person_ids


def main():
    key = FACE_API_KEY
    base_url = FACE_BASE_URL

    image_urls = ['Peter_Hook/train/1.jpg',
                  'Peter_Hook/train/2.jpg',
                  'Peter_Hook/train/3.jpg',
                  'Peter_Hook/train/4.jpg',
                  'Peter_Hook/train/5.jpg',
                  'Peter_Hook/train/6.jpg',
                  'Peter_Hook/train/7.jpg',
                  'Peter_Hook/train/8.jpg',
                  'Peter_Hook/train/9.jpg',
                  'Peter_Hook/train/10.jpg',
                  ]
    test_image = 'Peter_hook/test/11.jpg'
    # test_image = 'detection2.jpg'
    person_group = 'bassist'
    person_name = 'Peter Hook'

    face_api = FaceAPIWrapper(key, base_url)
    print(face_api.list_groups())
    face_api.delete_group(person_group)
    face_api.create_group(person_group)
    person_id = face_api.create_person(person_group=person_group, person_name=person_name)
    for image_url in image_urls:
        face_api.add_faces_to_person(person_group=person_group, person_id=person_id, image_url=image_url)
    face_api.train_group(person_group)
    face_ids = face_api.detect_faces(image=test_image)
    identified_person_id = face_api.identify_faces(face_ids=face_ids, large_person_group=person_group) or " "
    if identified_person_id in person_id:
        print(test_image, " and training data are of the same person")
    else:
        print(test_image, " and training data are of different people")


if __name__ == '__main__':
    main()
