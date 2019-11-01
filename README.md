# Multi-view Multi-distortion Image Dataset (MVMDD)

## 1. Dataset Information
To study the impact of image distortion on multi-view augmented reality system, we create the Multi-View Multi-Distortion image dataset (MVMDD). The dataset includes a pristine image set (i.e., clear images without distortion) and an augmented distortion image set. The detailed information of the collected MVMDD dataset is presented below.

### 1.1 Pristine image set
The pristine images are collected using a commodity Nokia 7.1 smartphone. **Six categories** of everyday objects are considered, *cup, phone, bottle, book, bag, and pen*. Each category has **six instances**. For each instance, images are taken from **six different views** (i.e., six different angles with a 60 degree angle difference between any two adjacent views), **two different background complexity levels** (i.e., a clear white table background and a noisy background containing other non-target objects), and **three distances**. The resolution of the image is 3024x4032. The details are summarized in the table below:

 |  |  | 
 | --- | :---: |
 | Object categories | 6 |
 | Number of views | 6 |
 | Background complexity| 2|
 | Size of object in image| 3|
 | Number of instances|6|
 |**Total pristine images**|6 x 6 x 2 x 3 x 6 = 1,296|

#### Example of pristine images collected in the dataset.
 
  ![image](https://github.com/CollabAR-Source/MVMDD/blob/master/example.PNG) 

### 1.2 Augmented image set
We apply data augmentation techniques on the pristine image set to generate a new augmented image set. Specifically, **three types of image distortion** are considered, *motion blur, Gaussian blur, and Gaussian noise*. For each type of distortion, **eight distortion levels** are considered.

## 2. Download MVMDD Dataset
The pristine image set can be downloaded via: ***[Link to the full-dataset will be made available after acceptance]***

A partial example set can access via: 

The MVMDD dataset provided here including only the pristine image set. Data augmentation source codes are provided for generating the augmented image set.

### 2.1 Hierarchical structure of the pristine image set

The pristine image set follows a hierarchical file structure below. The two sub-folders, ***Clear_Background*** and ***Complex Background***, correspond to the two background complexities, respectively. In each of the sub-folders, there are six folders that are corresponding to the ***six object categories***. 

- Tree structure of the dataset:
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

For instance, image with name *'bag1_view1_distance1.jpg'* corresponds to the 

## 2.2 Synthesize distorted images using data augmentation

After downloading the pristine image set, one can create the distortion image set by running the script "distortion_generation.py".

1. you need to install open-cv, skimage, numpy before running the script.
2. put the script in the folder "MVMDD".
3. runing the script: python .\distortion_generation.py -source_dir -distortion_type -distortion_degree<br>
   -source_dir -- the original dir that contains pristine images<br>
   -distortion_type:  "MB" for Montion blur, "GB" for Gaussian blur, "GN" for Gaussain noise<br>
   -distortion_degree: distortion level. <br>
   **ex: python .\distortion_generation.py .\Clear_Background\ GN 0.01**
4. you will see a generated folder that contains distortion images in "MVMDD"
  
 
