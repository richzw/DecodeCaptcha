DecodeCaptcha
=============

Decode captcha by python.

> **Ref** 
    [<i class="icon-share"></i> http://slid.es/jingchaohu/decoding-weibo-captcha-in-python]
    
>   [http://www.boyter.org/decoding-captchas/]

### Introduction

In this post, we will investigate the methods of decode captcha.

Generally Speaking, there are several steps to do that:

1. Remove Noise
2. Seperate Characters
3. Extract Characters
4. Classifying Features, data training
5. Predicting charactoer

##### Remove Noise

Here the Image module is used in this post, and there are two ways to remove noise from captcha.

+ convert to **L** Pattern
    
    convert the Image into black-white mode, 
    ```python
    im = im.point(lambda x:255 if x>128 or x==0 else x)
    im = im.point(lambda x:0 if x<255 else 255)
    ```
+ extract characters according to color
    
    extract characters from Image according to the color of them
