DecodeCaptcha
=============

Decode captcha by python.

> **Ref** 
    [<i class="icon-share"></i> http://slid.es/jingchaohu/decoding-weibo-captcha-in-python]
    
>   [http://www.boyter.org/decoding-captchas/]

### Introduction

In this post, we will investigate the methods of decode captcha. Currently, the texts in the captcha is not overrided 
with each other, just for simplicity.

Generally Speaking, there are several steps to do that:

1. Remove Noise
2. Seperate Characters
3. Extract Characters
4. Classifying Features, data training
5. Predicting charactoer

#### Remove Noise

Here the Image module is used in this post, and there are two ways to remove noise from captcha.

+ convert to **L** Pattern
    
    convert the Image into black-white mode, 
    ```python
    im = im.point(lambda x:255 if x>128 or x==0 else x)
    im = im.point(lambda x:0 if x<255 else 255)
    ```
+ extract characters according to color
    
    extract characters from Image according to the color of them，
    first of all, the color of text should be known previously. should be hard code here.

`Image filters` which blur the image horizontally and look for darker areas (because the blur causes the text to be highlighted). 

`Edge detection` filters which just leave the outline of text, pattern detection, colour extraction

#### Seperate Characters

Base on the previous process, then the range of one character can be detected.
Since there are only two colors (black and white) in the captcha after noise removing, the boundary of one character
can be recognize by counting the number of black dots. After that, we get the coordinates of boundary. 

#### Extract Characters

chop the characters from captcha through coordinates of character boundarys.
    
```python
Image.chop(coordianttopleft, coordinaterightbottom)
```

#### Classify Features, data training

There are many algorithm to do data training.

+ Netual network
+ Vector Space module
    
    curretly, this method is implemented in this post.

+ svm machine learning


### TODO:

1. Image filter and Edge detection
2. sklearn.svm to training data
2. characters are overrided in captcha
3. ...
