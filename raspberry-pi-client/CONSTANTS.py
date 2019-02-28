import os

from utils import is_raspberry_pi

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 1640
RESOLUTION_W = 922
CAPTURE_INTERVAL = 15
GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
CAMERA_NAME = os.environ.get('CAMERA_NAME', "")

FACE_API_KEY = os.environ.get('FACE_API_KEY', "170fff2406f348459a790f78b16dcd43")

FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'1d7d18cb-8e0b-498d-80c6-0d95c3d391e0': 'Tanmay Sawant',
                            '08ef7629-f8d8-406e-b366-88df696517d8': 'Anirudh Iyer',
                            '1bf15e0f-3837-493a-8f72-aa3e5e98694f': 'Rohan Sawant',
                            }
FACE_GROUP_ID = 'students'

CURRENT_IMAGE_FILE = "temp.png"
DEFAULT_PERSON_GROUP = 'co6g_students'  # DON'T USE CAPITAL LETTERS

REST_SERVER_URL = os.environ.get('REST_SERVER_URL', 'http://fras-1.herokuapp.com/')
