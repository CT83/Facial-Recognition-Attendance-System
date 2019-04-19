# Facial Recognition Attendance System using Deep Learning with Microsoft FaceAPI, Django and Raspberry Pi-es!
### F.R.A.S!

Other than being a mouthful to say; 
_FRAS_ allows **tens of facial-recognition-camera-clients** aka tiny *Raspberry Pi-es* to be deployed all across a college, 
or an industrial campus, which then record who they see and when they see then to a central database.

The entire system runs for dirt cheap on cloud using [Microsoft Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face), [Heroku](https://fras-1.herokuapp.com) and [AWS S3](https://aws.amazon.com/s3) and using multiple [Raspberry Pi Zeros](https://www.raspberrypi.org/products/raspberry-pi-zero), which cost about **15**-**17$**

## How does it work? 

#### Dystopian node-based Facial Recognition in 5 simple steps.

1. A [Django REST Server](<https://github.com/CT83/Facial-Recognition-Attendance-System/tree/master/django-server>), with a **PostGres Database** runs on [Heroku](https://fras-1.herokuapp.com).
2. A **15$** [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero) with a [Camera Module](https://www.raspberrypi.org/products/camera-module-v2) and internet connection is placed at any location - entrances, exits, hallways
3. The **Raspberry Pi** - *Camera Client* takes an image at regular intervals and sends this to [Microsoft Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face), which tells <u>who-is-who</u> in the image.
4. The *Camera Client* then sends the names of recognized persons to the **REST Server** for storage with the captured images which are sent to [AWS S3](https://aws.amazon.com/s3) for storage.
5. [Angular Frontend](https://fras-ui.herokuapp.com) allows users to view the stored data.

> This was my high school's final semester project on which I barely spent 48 hours building. The REST Server and 
Angular proved to be quite an undertaking! But, the professor seems pleasantly surprised with what 
I built so it all ended just fine. :)

## Architectural Overview

### Basic Architecture

![arch-1](images\arch-1.png)

Every Camera Client is responsible for recognizing all of the faces on it’s own and communicating with the **Microsoft Face API** as well as saving the images to S3, also the users connected to the Angular Client can also need to see the uploaded images, so everything ends up looking like this.

![arch-1](images\arch-2.png)

### User Interface

The Main Page shows the list of all registered students, **Face API** is sent about about ~20 images of each student during the initial setup. 

![img](images\acOWKiIrYYWj7kYNbbTsiMtoAVkX5cXyJc4OYOliBeEfTUVj-34iflCaEgPR4LaqUheeuBP_4-07vQy2oOAod03wnZpVq7n-WbaTcGS1oHZb8iEZFgtFquOI_7BRP_XjWmsUoeUbsls)

Selecting one of the students allows you to see where they were last seen, how many days they were present, and more

![img](images\RSIqhvcq2klaNNKZL55IkHQlD3C_SBoXYal4QizpCMTNkUkQfMom82n6pL6d7hcnTJ8QwONkIMacLEsKM6xRqOTb-VyIQp-b2pBZJmY5Ker3e-P6613himhWf5knlaCjx6yQfTd4014)

## Hardware

### Raspberry Pi Zero - Camera Module

![Image](images/camera-client.JPG)

#### Add a 5$ Case and Viola!

![Image](images/camera-case.JPG)

## How do I run it? -- Ehh

This is a high level description of what you could do, but feel free to hit me up on Hangouts at rohansawantct83@gmail.com if you are interesting in getting something like this up and running.
1. [Setup Microsoft Face API](https://docs.microsoft.com/en-us/azure/cognitive-services/Face/Tutorials/FaceAPIinPythonTutorial) 
2. [Build OpenCV on a Raspberry Pi Zero](https://www.pyimagesearch.com/2015/12/14/installing-opencv-on-your-raspberry-pi-zero)
3. [Setup up Django Server on Heroku](https://devcenter.heroku.com/articles/deploying-python)
4. [Setup Angular Frontend on Heroku](https://medium.com/@hellotunmbi/how-to-deploy-angular-application-to-heroku-1d56e09c5147)
5. [Setup AWS S3](https://www.whizlabs.com/blog/aws-s3/)

## Problem that I started out to solve



![Image](images/no-success.gif)



## Vision

In my worst nightmares, I imagine a highly sophisticated version of this running running on embedded devices like the [Nvidia Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/) - on every street corner, every shop and every stop light, the data could be continuosly stored in on the blockchain with no central point of failure, as we try and hope hard that our [Funky-Glasses](https://www.theverge.com/2016/11/3/13507542/facial-recognition-glasses-trick-impersonate-fool) are enough to fool the cutting edge ML Models.   



