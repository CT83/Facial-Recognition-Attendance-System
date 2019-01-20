from utils import is_raspberry_pi

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 320
RESOLUTION_W = 320
CAPTURE_INTERVAL = 30
GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
SENDER_EMAIL = 'collegerohansawantct83@gmail.com'
SENDER_PASSWORD = 'eminemcybertech83'
RECEIVER_EMAIL = '3rohansawantct83@gmail.com'

# try:
#     FACE_API_KEY = load_dict_from_file('FACEAPI_KEY.json')['face_api_key']
# except FileNotFoundError:
#     FACE_API_KEY = ""

FACE_API_KEY = "170fff2406f348459a790f78b16dcd43"

FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'da3c26c5-5745-46df-9fa2-8003aed1eff7': 'Tanmay Sawant',
                            '855de0ff-970f-4b6a-a1d4-557707a7e6c1': 'Anirudh Iyer',
                            'f0b07f85-3d65-4ff4-a1f9-41d1d11edb35': 'Rohan Sawant',
                            }
FACE_GROUP_ID = 'students'

CURRENT_IMAGE_FILE = "temp.png"
DEFAULT_PERSON_GROUP = 'co6g_students'  # DON'T USE CAPITAL LETTERS

REST_SERVER_URL = 'http://localhost:8000/'
