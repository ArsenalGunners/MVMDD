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

## What is the files' names mean?
When you download and unzip the file, a file tree shows above. Clear_Background and Complex Background are two different background complexity level. Either of them contains six object categories (**bag, books, bottles, cups, pens, phones**). For every image in a certain category, the file name is "(instance number) _ (view number) _ (distance number).jpg" 

## Example of several images
![image](https://github.com/CollabAR-Source/MVMDD/blob/master/example.jpg.PNG)

| Bag      | Book | Bottle     |Cup   |Pen    |Phone    |
| :---        |    :----:   |         :----:  |:----:     |:----:    |---:    |
|bag1_view1_distance1| Title       |bottle1_view1_distance1|cup1_view1_distance1|pen1_view1_distance1|phone1_view1_distance1|
|bag5_view1_distance2| Text        |bottle2_view2_distance2|cup2_view2_distance2|pen2_view1_distance2|phone6_view2_distance2|
|bag6_view2_distance3| Text        |bottle3_view4_distance3|cup3_view6_distance3|pen5_view4_distance3|phone5_view6_distance3|
