# Multi-view Multi-distortion Image Dataset (MVMDD)

## Dataset Information
To study the impact of image distortion on multi-view augmented reality system, we create the Multi-View Multi-Distortion image dataset (MVMDD). The dataset includes a pristine image set (i.e., clear images without distortion) and an augmented distortion image set. The detailed information of the collected MVMDD dataset is summarized in the tables below.

### Pristine image set
The pristine images are collected using a commodity Nokia 7.1 smartphone. **Six categories** of everyday objects are considered, *cup, phone, bottle, book, bag, and pen*. Each category has **six instances**. For each instance, images are taken from **six different views** (i.e., six different angles with a 60 degree angle difference between any two adjacent views), **two different background complexity levels** (i.e., a clear white table background and a noisy background containing other non-target objects), and **three distances**. The resolution of the image is 3024x4032. The details are summarized in the table below:

|  |  | 
| --- | :---: |
| Object categories | 6 |
| Number of views | 6 |
| Background complexity| 2|
| Size of object in image| 3|
| Number of instances|6|
|**Total pristine images**|6x6x2x3x6=1,296|


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

## What is the meaning of  files' names?
When you download and unzip the file, a file tree shows above. Clear_Background and Complex Background are two different background complexity level. Either of them contains six object categories (**bag, books, bottles, cups, pens, phones**). For every image in a certain category, the file name is "(instance number) _ (view number) _ (distance number).jpg" 

## Example of several images
 
  ![image](https://github.com/CollabAR-Source/MVMDD/blob/master/example.PNG)

Here are the coresponding names for the above image examples

| Bag      | Book | Bottle     |Cup   |Pen    |Phone    |
| :---        |    :----:   |         :----:  |:----:     |:----:    |---:    |
|bag1_view1_distance1|book1_view1_distance1|bottle1_view1_distance1|cup1_view1_distance1|pen1_view1_distance1|phone1_view1_distance1|
|bag5_view1_distance2|book2_view6_distance2|bottle2_view2_distance2|cup5_view5_distance2|pen2_view1_distance2|phone6_view2_distance2|
|bag6_view2_distance3|book2_view6_distance2|bottle3_view4_distance3|cup3_view6_distance3|pen5_view4_distance3|phone5_view6_distance3|

## Synthesize Distortion Images

You can make your own distortion image dataset by running the script "distortion_generation.py".

1. you need to install open-cv, skimage, numpy before running the script.
2. put the script in the folder "MVMDD".
3. runing the script: python .\distortion_generation.py -source_dir -distortion_type -distortion_degree<br>
   -source_dir -- the original dir that contains pristine images<br>
   -distortion_type:  "MB" for Montion blur, "GB" for Gaussian blur, "GN" for Gaussain noise<br>
   -distortion_degree: distortion level. <br>
   **ex: python .\distortion_generation.py .\Clear_Background\ GN 0.01**
4. you will see a generated folder that contains distortion images in "MVMDD"
  
 
