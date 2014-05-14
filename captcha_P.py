from PIL import Image
import sklearn.svm
import hashlib
import time
import os
import math


class VectorCompare:
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.iteritems():
            total += count**2
        return math.sqrt(total)
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue/(self.magnitude(concordance1) * self.magnitude(concordance2))

def buildDict(im):
    return dict((k,v) for k,v in enumerate(list(im.getdata())))


# get the basic data vector
def buildVectorSpace():
    iconset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    imageset = []

    for letter in iconset:
      for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db": # windows check...
          temp.append(buildDict(Image.open("./iconset/%s/%s"%(letter,img))))
        imageset.append({letter:temp})

    return imageset

# match letter
def matchLetter(letters, im, imageset):
    v = VectorCompare()
    for letter in letters:
        m = hashlib.md5()
        im_char = im.crop(( letter[0] , 0, letter[1], im.size[1] ))

        guess = []
        for image in imageset:
            for x,y in image.iteritems():
                if len(y) != 0:
                    guess.append( ( v.relation(y[0], buildDict(im_char)), x) )

        guess.sort(reverse=True)
        print " ",guess[0]

# filter the noise according to the color
def filterCaptcha(im):
    im = im.convert("P")
    im2 = Image.new("P", im.size, 255)
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            #temp[pix] = pix
            if pix == 220 or pix == 227: # these are the numbers to get
                im2.putpixel((y,x),0)
    #im2.show()
    return im2


# Seperating Characters for color
def seperateLetters_color(im):
    inletter = False
    foundletter = False
    letters = []
    
    for y in xrange(im.size[0]):
        for x in xrange(im.size[1]):
            pix = im.getpixel((y,x))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y
        if foundletter == True and inletter == False :
            foundletter = False
            end = y
            letters.append((start, end))
        inletter = False
    return letters


def main():
    im = Image.open("captcha.gif")#("VerifyCode.jpg")
    #im = clean(im)
    im = filterCaptcha(im)
    letters_locations = seperateLetters_color(im)
    print letters_locations
    matchLetter(letters_locations, im, buildVectorSpace())
