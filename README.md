# Facial Recognition Attendance System using Deep Learning (Machine Learning) with OpenCV, Django in Python

## How to Install - Server?

* Install NodeJS and Angular
* Install all dependencies `pip install -r requirements.txt`
* Create Database migrations `python manage.py makemigrations`
* Migrate Database `python manage.py migrate`

## How to run

1. Start Django Server
* `cd code/django-server/fras`
* `python manage.py runserver`


2. Start Angular Server
* `cd code/angular_ui/fras-ui`
* `ng serve --open`


3. Start Camera Client
* `cd code/raspberry-pi-client`
* `python run_camera_client.py`


### What are we trying to build?

An attendance system which uses facial recognition to detect which people are present in any image.

### What are we using? 

1. [Microsoft Face API ](https://azure.microsoft.com/en-in/services/cognitive-services/face/)
   

### What do we plan on implementing?

The method of image processing using Face API is very black boxed and does not expose it's implementation. Hence, in future we plan to re-use some code from,
1.[OpenCV-Face-Recognition-Python](https://github.com/informramiz/opencv-face-recognition-python)

* This can be tweaked and modified to make it use ensemble learning to increase accuracy.
* Three Algorithms are mentioned in the projects readme, their respective papers can be found in 'Papers/Face Recognition Algorithms'

2.https://github.com/ageitgey/face_recognition
3.https://github.com/Mjrovai/OpenCV-Face-Recognition

### How to get up to speed?

1. [Read Relevant Papers](https://github.com/CT83/Facial-Recognition-Attendance-System/tree/master/Papers)
2. [Basic Understanding of Python 3 YouTube Playlist](https://www.youtube.com/watch?v=oVp1vrfL_w4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)
3. [Know how Python Virtual Environments Work](https://www.youtube.com/watch?v=N5vscPTWKOk)
4. [Basic Understanding of Git and GitHub](https://www.youtube.com/watch?v=cEGIFZDyszA&list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx)
5. [Install PyCharm JetBrains IDE](https://www.jetbrains.com/help/pycharm/install-and-set-up-pycharm.html)

### Frequently Used Git Commands

1. Remove a File from Staging Area `git reset HEAD -- Code/filename.extension`


### Setup - Server
#### Creating Migrations
1. `SET DJANGO_SETTINGS_MODULE=fras.settings.dev`
2. `python fras/manage.py makemigrations`
2. `python fras/manage.py migrate`

#### Setup Client
`aws configure`
AWS Access Key ID [None]: input your access key
AWS Secret Access Key [None]: input your secret access key
Default region name [None]: input your region
Default output format [None]: json
`aws s3 ls`




### FAQ 

1. How to download IEEE Papers?
  * Visit http://sci-hub.tw/
  * Paste link of IEEE paper which you want to download example (https://ieeexplore.ieee.org/document/7013165/)
