# Multi-view Multi-distortion Image Dataset (MVMDD)

## 1. Dataset Information
To study the impact of image distortion on multi-view augmented reality system, we create the Multi-View Multi-Distortion image dataset (MVMDD). The dataset includes a pristine image set (i.e., clear images without distortion) and an augmented distortion image set. The detailed information of the collected MVMDD dataset is presented below.

### 1.1 Pristine image set
The pristine images are collected using a commodity Nokia 7.1 smartphone. The resolution of the original image is 3024x4032. The data are collected under **two different background complexity** (i.e., a clear white table background and a noisy background containing other non-target objects). Six categories of everyday objects are considered under each background complexity, *cup, phone, bottle, book, bag, and pen*. Each category has **six instances**. For each instance, images are taken from **six different views** (i.e., six different angles with a 60 degree angle difference between any two adjacent views) and **three distances**. The details are summarized in the table below:

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
We apply data augmentation techniques on the pristine image set to generate a new augmented image set. Specifically, **three types of image distortion** are considered, *motion blur, Gaussian blur, and Gaussian noise*. For each type of distortion, **eight distortion levels** are considered. We are using the following models to augment distortion images:

- Motion blur:
  - Sun, Jian, Wenfei Cao, Zongben Xu, and Jean Ponce. "Learning a convolutional neural network for non-uniform motion blur removal." In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 769-777. 2015.
- Gaussian blur:
  - Flusser, Jan, Sajad Farokhi, Cyril Höschl, Tomáš Suk, Barbara Zitová, and Matteo Pedone. "Recognition of images degraded by Gaussian blur." IEEE transactions on Image Processing 25, no. 2 (2015): 790-806.
- Gaissian noise:
  - Liu, Wei, and Weisi Lin. "Additive white Gaussian noise level estimation in SVD domain for images." IEEE Transactions on Image processing 22, no. 3 (2012): 872-883.

The codes and procedure in generating the augmented image set are introduced below (in section 2.2).

## 2. Download MVMDD Dataset
The pristine image set can be downloaded via: https://1drv.ms/u/s!Aqyf-lNI69G1g3plety8Ie4FD8h9?e=9Ys6Rz

The MVMDD dataset provided here including only the pristine image set. Data augmentation source codes are provided for generating the augmented image set.

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

For instance, image with name *'bag1_view1_distance1.jpg'* corresponds to the image of *instance #1* of *bag* which captured at *distance1* from *view1*. (Notice that the *instance number* and *view number* are not **one-on-one corresponded** under two background complexity folders, the number is used to distinguish it from other instances and views within the current folder. But the distance number is strictly corresponding to the proportion of objects in the picture.)

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

The following is an example of generating *Gaussian noise* distorted images with distortion level *0.01* for all the images in the *.\Clear_Background* folder: **python .\distortion_generation.py .\Clear_Background\ GN 0.01**
  
