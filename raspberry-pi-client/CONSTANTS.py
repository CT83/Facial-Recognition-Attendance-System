import os

from utils import is_raspberry_pi

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 1640
RESOLUTION_W = 922
CAPTURE_INTERVAL = 15
GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
CAMERA_NAME = os.environ.get('CAMERA_NAME', "Camera 1")

FACE_API_KEY = os.environ.get('FACE_API_KEY', "")

FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'FACE_ID1': 'Tanmay Sawant',
                            'FACE_ID2': 'Anirudh Iyer',
                            'FACE_ID3': 'Rohan Sawant',
                            }
FACE_GROUP_ID = 'students'

CURRENT_IMAGE_FILE = "temp.png"
DEFAULT_PERSON_GROUP = 'co6g_students'  # DON'T USE CAPITAL LETTERS

REST_SERVER_URL = os.environ.get('REST_SERVER_URL', 'http://fras-1.herokuapp.com/')
