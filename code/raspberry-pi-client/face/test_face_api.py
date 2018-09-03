import unittest

from CONSTANTS import FACE_API_KEY, FACE_BASE_URL
from face.FaceAPIWrapper import FaceAPIWrapper


class TestFaceAPIWrapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestFaceAPIWrapper, cls).setUpClass()
        key = FACE_API_KEY
        base_url = FACE_BASE_URL

        image_urls = ['images/Peter_Hook/train/1.jpg',
                      'images/Peter_Hook/train/2.jpg',
                      'images/Peter_Hook/train/3.jpg',
                      'images/Peter_Hook/train/4.jpg',
                      'images/Peter_Hook/train/5.jpg',
                      'images/Peter_Hook/train/6.jpg',
                      'images/Peter_Hook/train/7.jpg',
                      'images/Peter_Hook/train/8.jpg',
                      'images/Peter_Hook/train/9.jpg',
                      'images/Peter_Hook/train/10.jpg',
                      ]

        cls.person_group = 'bassist'
        cls.person_name = 'Peter Hook'

        cls.face_api = FaceAPIWrapper(key, base_url)
        cls.face_api.delete_group(cls.person_group)
        cls.face_api.create_group(cls.person_group)
        cls.person_id = cls.face_api.create_person(person_group=cls.person_group, person_name=cls.person_name)
        for image_url in image_urls:
            cls.face_api.add_faces_to_person(person_group=cls.person_group, person_id=cls.person_id,
                                             image_url=image_url)
        cls.face_api.train_group(cls.person_group)

    def test_correct_identification_same_persons(self):
        test_image = 'images/Peter_hook/test/11.jpg'
        face_ids = self.face_api.detect_faces(image=test_image)
        identified_person_id = \
            self.face_api.identify_face(face_ids=face_ids,
                                        large_person_group=self.person_group) or " "
        self.assertEqual(identified_person_id, self.person_id)

    def test_correct_identification_different_persons(self):
        test_image_2 = 'images/detection1.jpg'
        face_ids = self.face_api.detect_faces(image=test_image_2)
        identified_person_id = \
            self.face_api.identify_face(face_ids=face_ids,
                                        large_person_group=self.person_group) or " "
        self.assertNotEqual(identified_person_id, self.person_id)

    def test_create_group(self):
        self.face_api.delete_group("random_test_group")
        self.face_api.create_group("random_test_group")
        groups = self.face_api.list_groups()
        # Format [{'largePersonGroupId': 'allowed_persons', 'name': 'allowed_persons', 'userData': None},]
        found = False
        for group in groups:
            found = 'random_test_group' in group['largePersonGroupId'] or 'random_test_group' in group['name']
            if found:
                break
        self.assertTrue(found)
        self.face_api.delete_group("random_test_group")

    def test_delete_group(self):
        self.face_api.create_group("random_test_group")
        self.face_api.delete_group("random_test_group")
        groups = self.face_api.list_groups()
        # Format [{'largePersonGroupId': 'allowed_persons', 'name': 'allowed_persons', 'userData': None},]
        found = False
        for group in groups:
            found = 'random_test_group' in group['largePersonGroupId'] or 'random_test_group' in group['name']
            if found:
                break
        self.assertFalse(found)

    def tearDown(self):
        # Basic rate limiting
        import time
        time.sleep(30)

    @classmethod
    def tearDownClass(cls):
        super(TestFaceAPIWrapper, cls).tearDownClass()
        cls.face_api.delete_group(cls.person_group)


if __name__ == '__main__':
    unittest.main()
