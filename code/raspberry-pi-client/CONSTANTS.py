from utils import is_raspberry_pi

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 1640
RESOLUTION_W = 1232
CAPTURE_INTERVAL = 30
GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
CAMERA_NAME = 'camera_2'
AWS_ACCESS_KEY = 'AKIAJJXPMJJP6CMFFKLQ'
AWS_ACCESS_SECRET_KEY = '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'

# try:
#     FACE_API_KEY = load_dict_from_file('FACEAPI_KEY.json')['face_api_key']
# except FileNotFoundError:
#     FACE_API_KEY = ""

FACE_API_KEY = "170fff2406f348459a790f78b16dcd43"

FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'da3c26c5-5745-46df-9fa2-8003aed1eff7': 'Tanmay Sawant',
                            '301a333c-2bcf-45b1-b847-fe9191f2ecaa': 'Anirudh Iyer',
                            'f0b07f85-3d65-4ff4-a1f9-41d1d11edb35': 'Rohan Sawant',
                            }
FACE_GROUP_ID = 'students'

CURRENT_IMAGE_FILE = "temp.png"
DEFAULT_PERSON_GROUP = 'co6g_students'  # DON'T USE CAPITAL LETTERS

# REST_SERVER_URL = 'http://localhost:8000/'
REST_SERVER_URL = 'http://192.168.1.2:8000/'
