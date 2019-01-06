from utils import is_raspberry_pi, load_dict_from_file

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 320
RESOLUTION_W = 320
CAPTURE_INTERVAL = 15
GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
SENDER_EMAIL = 'collegerohansawantct83@gmail.com'
SENDER_PASSWORD = 'eminemcybertech83'
RECEIVER_EMAIL = '3rohansawantct83@gmail.com'

try:
    FACE_API_KEY = load_dict_from_file('FACEAPI_KEY.json')['face_api_key']
except FileNotFoundError:
    FACE_API_KEY = ""

FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'aae2f120-20d6-4fa7-b34c-f1dbe7aa09a9': 'Tanmay Sawant'}
FACE_GROUP_ID = 'allowed_persons'

CURRENT_IMAGE_FILE = "temp.png"
DEFAULT_PERSON_GROUP = 'co5g_students'  # DON'T USE CAPITAL LETTERS

REST_SERVER_URL = 'http://localhost:8000/'
