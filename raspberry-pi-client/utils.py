import datetime
import io
import os

import boto3


def is_raspberry_pi(raise_on_errors=False):
    """Checks if Raspberry PI.

    :return:
    """
    try:
        with io.open('/proc/cpuinfo', 'r') as cpuinfo:
            found = False
            for line in cpuinfo:
                if line.startswith('Hardware'):
                    found = True
                    label, value = line.strip().split(':', 1)
                    value = value.strip()
                    if value not in (
                            'BCM2708',
                            'BCM2709',
                            'BCM2835',
                            'BCM2836'
                    ):
                        if raise_on_errors:
                            raise ValueError(
                                'This system does not appear to be a '
                                'Raspberry Pi.'
                            )
                        else:
                            return False
            if not found:
                if raise_on_errors:
                    raise ValueError(
                        'Unable to determine if this system is a Raspberry Pi.'
                    )
                else:
                    return False
    except IOError:
        if raise_on_errors:
            raise ValueError('Unable to open `/proc/cpuinfo`.')
        else:
            return False

    return True


def preview_image(image, name="window", time=1000):
    import cv2
    cv2.imshow(name, image)
    if cv2.waitKey(time):
        cv2.destroyAllWindows()


def create_save_random_image(file_path='result_image.png'):
    import numpy as np
    rgb = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)
    import cv2
    cv2.imwrite(file_path, rgb)
    return file_path


def save_dict_to_file(file_name, dict_data):
    import json
    with open(file_name, 'w') as outfile:
        json.dump(dict_data, outfile)


def load_dict_from_file(file_name):
    with open(file_name) as data_file:
        import json
        data = json.load(data_file)
        return data


def get_lecture_number(time=datetime.datetime.now()):
    """Convert current hour to lecture indices"""
    idx = time.hour - 9
    if idx < 0:
        idx = 0

    if time.hour > 17:
        idx = 8
    return idx


def upload_to_s3(key):
    print("Uploading file to S3...")
    bucket_name = 'fras-store'

    folder_name = "public_folder"
    output_name = folder_name + "/" + key
    location = 'us-east-1'

    s3 = boto3.client('s3')
    s3.upload_file(key, bucket_name, output_name, ExtraArgs={'ACL': 'public-read'})

    url = "https://s3.amazonaws.com/%s/%s/%s" % (bucket_name, folder_name, key)
    return url


def current_time_to_string():
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d_%H%M%S%f")


def create_dir_if_not_exists(output_dir):
    try:
        os.makedirs(output_dir)
    except OSError:
        if not os.path.isdir(output_dir):
            raise
