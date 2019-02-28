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
   

### Setup - Server
#### Creating Migrations
1. `SET DJANGO_SETTINGS_MODULE=fras.settings.dev`
2. `python fras/manage.py makemigrations`
2. `python fras/manage.py migrate`

#### Setup Client
`pip install awscli`
`aws configure`
AWS Access Key ID [None]: input your access key
AWS Secret Access Key [None]: input your secret access key
Default region name [None]: input your region
Default output format [None]: json
`aws s3 ls`

### Frequently Used Git Commands

1. Remove a File from Staging Area `git reset HEAD -- Code/filename.extension`


### FAQ 

1. How to download IEEE Papers?
  * Visit http://sci-hub.tw/
  * Paste link of IEEE paper which you want to download example (https://ieeexplore.ieee.org/document/7013165/)
