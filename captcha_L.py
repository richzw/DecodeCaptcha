#Ref: http://www.boyter.org/decoding-captchas/

from PIL import Image
import sklearn.svm
import hashlib
import time
import os
import math

#Removing Noise
def clean(im):
    im = im.convert('L')
    im = im.point(lambda x:255 if x>128 or x==0 else x)
    im = im.point(lambda x:0 if x<255 else 255)
    return im

# Seperating Characters
def seperateLetters(im):
    inletter = False
    foundletter = False
    start = 0
    end = 0

    letters = []
    print im.size[0], im.size[1]
    for y in xrange(im.size[0]):
        for x in xrange(im.size[1]):
            pix = im.getpixel((y,x))
            if pix != 255:
                inletter += 1
        if foundletter == False and inletter > 1: #TODO: 3 is magic number and need to verify
            foundletter = True
            start = y
        if foundletter == True and inletter <= 1 :
            foundletter = False
            end = y
            letters.append((start, end))
        inletter = 0
    return letters
    
# correct the range of letters 
def correctLetters(letters):
    length = len(letters)
    for idx, val in enumerate(letters):
        if val[1] - val[0] <= 2:
            if 0 < idx < length-1:
                if val[0]-letters[idx-1][1] >= letters[idx+1][0] - val[1]:
                    letters[idx+1][0] = val[1]
                else:
                    letters[idx-1][1] = val[0]
            del letters[idx]
    # hard code here for demo
    letters[0][1] += 1
    letters[0][0] -= 1
    return letters
    

#  
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
        im3 = im.crop(( letter[0] , 0, letter[1], im.size[1] ))

        guess = []
        for image in imageset:
            for x,y in image.iteritems():
                if len(y) != 0:
                    guess.append( ( v.relation(y[0], buildDict(im3)),x) )

        guess.sort(reverse=True)
        print "",guess[0]

def main():
    im = Image.open("captcha.gif")#("VerifyCode.jpg")
    im = clean(im)
    letters_locations = seperateLetters(im)
    letters_locations = correctLetters(letters_locations)
    #letters_locations = [(6, 14), (15, 25), (27, 35), (37, 46), (48, 56), (57, 67)]
    #letters_locations = [letter for letter in letters_locations if letter[0] != letter[1]]
    print letters_locations
    matchLetter(letters_locations, im, buildVectorSpace())


if __name__ == '__main__':
    main()
