# Multi-view Multi-distortion Image Dataset (MVMDD)

This repository contains the download links and introduction of Multi-view Multi-distortion Image Dataset (MVMDD) for IPSN 2020 Paper "CollabAR: Edge-assisted Collaborative Image Recognition for Mobile Augmented Reality" by [Zida Liu](daliu.github.io), [Guohao Lan](https://guohao.netlify.com/), Jovan Stojkovic, Yunfan Zhang, [Carlee Joe-Wong](https://www.andrew.cmu.edu/user/cjoewong/), and [Maria Gorlatova](https://maria.gorlatova.com/).

If you have any questions on this repository or the related paper, feel free to create an issue or send me an email.
Email address: zida.liu (at) duke.edu

**Summary**:

* [Dataset Information](#1)
* [Download MVMDD Dataset](#2)
* [CollabAR Demo](#3)
* [Citation](#4)
* [Acknowledgements](#5)

## 1. <span id="1">Dataset Information</span>
To study the impact of image distortion on multi-view augmented reality system, we create the Multi-View Multi-Distortion image dataset (MVMDD). The dataset includes a pristine Multi-view image set (i.e., clear images without distortion) and an augmented distortion Multi-view image set. The detailed information of the collected MVMDD dataset is presented below.


### 1.1 Pristine image set
The pristine images are collected using a commodity Nokia 7.1 smartphone. The resolution of the original image is 3024x4032. Six categories of everyday objects are considered, *cup, phone, bottle, book, bag, and pen*. The data are collected under **two different background complexity** (i.e., a clear white table background and a noisy background containing other non-target objects). Each category has **six instances**. For each instance, images are taken from **six different views** (i.e., six different angles with a 60 degree angle difference between any two adjacent views) and **three distances** (We adjust the distance between the camera and the object such that the sizes of the object in the images are different. For the three distances, the object occupies approximately the whole, half, and one-tenth of the total area of the image). The details are summarized in the table below:

 |  |  | 
 | --- | :---: |
 | Object categories | 6 |
 | Number of views | 6 |
 | Background complexity| 2|
 | Size of object in image| 3|
 | Number of instances|6|
 |**Total pristine images**|6 x 6 x 2 x 3 x 6 = 1,296|

#### Example of pristine images collected in the dataset:
![image](https://github.com/CollabAR-Source/MVMDD/blob/master/example.PNG) 

### 1.2 Augmented image set
We apply data augmentation techniques on the pristine image set to generate a new augmented image set. Specifically, **three types of image distortion** are considered, *motion blur, Gaussian blur, and Gaussian noise*. Motion blur always appears because of the movement of mobile and head-mounted AR devices. Gaussian blur is used to simulate defocus and underwater effects. And Gaussian noise is evident in dim light conditions because of the high ISO value.

For each type of distortion, **eight distortion levels** are considered. We are using the following models to augment images:

- Motion blur:
  - Sun, Jian, Wenfei Cao, Zongben Xu, and Jean Ponce. "Learning a convolutional neural network for non-uniform motion blur removal." In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 769-777. 2015.
- Gaussian blur:
  - Flusser, Jan, Sajad Farokhi, Cyril Höschl, Tomáš Suk, Barbara Zitová, and Matteo Pedone. "Recognition of images degraded by Gaussian blur." IEEE transactions on Image Processing 25, no. 2 (2015): 790-806.
- Gaissian noise:
  - Liu, Wei, and Weisi Lin. "Additive white Gaussian noise level estimation in SVD domain for images." IEEE Transactions on Image processing 22, no. 3 (2012): 872-883.

#### Example of augmented distorted images in the dataset:
<img src="https://github.com/CollabAR-Source/MVMDD/blob/master/distorted_images.png" width = "700" height = "400" hspace="70" align=center />
The codes and procedure for generating the augmented image set are introduced below (in section 2.2).

## 2. <span id="2">Download MVMDD Dataset</span>
+ The pristine image set can be downloaded via: https://1drv.ms/u/s!Aqyf-lNI69G1hBi5mn31KDNzuw2u?e=qxX2gs
+ An augmented distortion image set can be downloaded via: https://drive.google.com/file/d/1GHtqs2B3Unuhej-BnvZ2QbRCgCPULPvq/view?usp=sharing, which contains three different levels for each destortion category. 

| Distortion parameter | level 1 | level 2 | level 3 |
| ------ | ------ | ------ | ------ |
| Blur kernel length (Motion blur) | 10 | 20 | 30 |
| Aperture size (Gaussian blur)| 11 | 21 | 31 |
| Variance (Gaussian noise)| 0.01 | 0.02 | 0.03 |
    
    
+ Data augmentation source codes are provided for generating your own the augmented image set.



    

### 2.1 Hierarchical structure of the pristine image set

The pristine image set follows a hierarchical file structure below. The two sub-folders, ***Clear_Background*** and ***Complex Background***, correspond to the two background complexities, respectively. In each of the sub-folders, there are six folders that are corresponding to the ***six object categories***. 

- Tree structure of the dataset folder:
```
MVMDD
└───Clear_Background
│   │
│   └───bags
│       │   bag1_view1_distance1.jpg
│       │   bag1_view1_distance2.jpg
│       │   ...
│   └───books
│   └───bottles
│   └───cups
│   └───pens
│   └───phones
│   
└───Complex_Background
│   │
│   └───bags
│   └───books
│   └───bottles
|   ...
```
The images are named in the format of ***(instance number) _ (view number) _ (distance number).jpg***, where:
- **(instance number)** corresponds to one of the **six instances**, 
- **(view number)** corresponds to one of the **six views**,
- **(distance number)** corresponds to one of the **six distances**.

For instance, image with name *'bag1_view1_distance1.jpg'* corresponds to the image of *instance #1* of *bag* which captured at *distance1* from *view1*.

### 2.2 Synthesize distorted images using data augmentation

After downloading the pristine image set, one can create the distortion image set by running the Python script "*distortion_generation.py*". The script can be download via: https://github.com/CollabAR-Source/MVMDD/blob/master/distortion_generation.py

You should be able to generate distortion images follow the procedure below:
1. Before running the script, you should install necessary tools and libraries on your computer including: open-cv, skimage, and numpy.
2. Then, put the script under the folder ''MVMDD''.
3. Run the script by: `python .\distortion_generation.py -source_dir -distortion_type -distortion_degree<br>`
   - *source_dir*: indicates the original dir that contains the pristine images.
   - *distortion_type*: indicates the type of distortion you whould like to sythesize. There are three options avaliable: 
      - *MB* for montion blur 
      - *GB* for Gaussian blur 
      - *GN* for Gaussain noise
   - *distortion_degree*: indicates the distortion level you would like to set.
 4. The generated images will be saved in generated folder.

The following is an example of generating *Gaussian noise* distorted images with distortion level *0.01* for all the images in the *./Clear_Background* folder: **python .\distortion_generation.py .\Clear_Background\ GN 0.01**
  
## 3. <span id="3">CollabAR Demo</span>

We make CollabAR AR demonstration by MVMDD dataset. Here is a partial demo video, which aims to collaborate corelated users to improve AR experience in heterogeneous environment. You can find full [video](https://www.youtube.com/watch?v=RFCxe9ZAVQw&feature=youtu.be) and [demo paper](https://maria.gorlatova.com/wp-content/uploads/2019/09/MultiUserAR_SenSysDemo_Gorlatova.pdf) here.


<img src="https://github.com/CollabAR-Source/MVMDD/blob/master/video.gif" width = "500" height = "300" hspace="170" align=center />

## 4. <span id="4">Citation</span>

Please cite the following papers in your publications if the dataset helps your research.

     @inproceedings{liuIPSN20,
      title={CollabAR: Edge-assisted collaborative image recognition for mobile augmented reality },
      author={Liu, Zida and Lan, Guohao and Stojkovic, Jovan and Yunfan, Zhang and Joe-Wong, Carlee and Gorlatova, Maria},
      booktitle={Proceedings of the 19th ACM/IEEE Conference on Information Processing in Sensor Networks},
      year={2020}
    }
  
## 5. <span id="5">Acknowledgements</span>
