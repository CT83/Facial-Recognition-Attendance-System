from utils import is_raspberry_pi, load_dict_from_file

CAMERA_PORT = 0
IS_RASPBERRY_PI = is_raspberry_pi()
RESOLUTION_H = 320
RESOLUTION_W = 320

GPIO_SWITCH = 24

IMAGE_PATH = 'captured_images/'
SENDER_EMAIL = 'collegerohansawantct83@gmail.com'
SENDER_PASSWORD = 'eminemcybertech83'
RECEIVER_EMAIL = '3rohansawantct83@gmail.com'

FACE_API_KEY = load_dict_from_file('FACE_API_KEY.json')['face_api_key']
FACE_BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'

FACE_PERSON_ID_NAME_DICT = {'ce8b5f24-91c5-4726-bfc0-36f3fc469786': 'Rohan Sawant'}
FACE_GROUP_ID = 'allowed_persons'
