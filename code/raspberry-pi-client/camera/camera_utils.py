import cv2


def preview_image(image, name="window", time=100, resize=True):
    if resize:
        cv2.imshow(name, cv2.resize(image, (400, 400)))
    else:
        cv2.imshow(name, image)
    cv2.waitKey(time)
