# MVMDD

Here is the hyperlink for downloading MVMDD dataset : https://1drv.ms/u/s!Aqyf-lNI69G1gkZOzXY8pcpU_ouL?e=aOlAfG

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

Here is the coresponding name for the above image examples

| Bag      | Book | Bottle     |Cup   |Pen    |Phone    |
| :---        |    :----:   |         :----:  |:----:     |:----:    |---:    |
|bag1_view1_distance1|book1_view1_distance1|bottle1_view1_distance1|cup1_view1_distance1|pen1_view1_distance1|phone1_view1_distance1|
|bag5_view1_distance2|book2_view6_distance2|bottle2_view2_distance2|cup5_view5_distance2|pen2_view1_distance2|phone6_view2_distance2|
|bag6_view2_distance3|book2_view6_distance2|bottle3_view4_distance3|cup3_view6_distance3|pen5_view4_distance3|phone5_view6_distance3|

## Synthesize Distortion Images

You can make your own distortion image dataset by the script "distortion_generation.py".

1. you need to install open-cv, skimage, numpy before running the script.
2. put the script in the folder "MVMDD".
3. runing the script: python .\distortion_generation.py -source_dir -distortion_type -distortion_degree<br>
   -source_dir -- the original dir that contains pristine images<br>
   -distortion_type: <br>
                       "MB" for Montion blur,<br>
                       "GB" for Gaussian blur,<br>
                       "GN" for Gaussain noise<br>
   -distortion_degree: distortion level. <br>
   **ex: python .\distortion_generation.py .\Clear_Background\ GN 0.01**
4. you will see the generated folder that contains distortion images in "MVMDD"
  
 
