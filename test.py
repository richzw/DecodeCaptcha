#ref http://slid.es/jingchaohu/decoding-weibo-captcha-in-python
from PIL import Image
import sklearn.svm

#Removing Noise
def clean(im):
    im = im.convert('L')
    im = im.point(lambda x:255 if x>128 or x==0 else x)
    im = im.point(lambda x:0 if x<255 else 255)
    return im

#Separating Characters
def divideByCol(im):
    w, h = im.size
    data = im.load()
    jcolors = [sum(255-data[i,j] for j in range(h)) for i in range(w)]
    return jcolors

#Extracting Features
def im2array(im):
    return [int(x!='\xff') for x in im.tobytes()]

#Classifying Features
# training:
#   data: integer arrays
#   target: arrays of 0-35(represents[0-9A-Z])
#   clf.fit(data, target)

# predicting:
#   array = preprocess char image into arrays
#   code = clf.predict(array)
#   char = lookup code in [0-9A-Z]


def main():
    im = Image.open("VerifyCode.jpg")


if __name__ == '__main__':
    main()

    
