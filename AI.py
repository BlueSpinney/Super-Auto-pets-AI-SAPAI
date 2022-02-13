

import cv2

import pyautogui

import numpy as np

import imutils

from tkinter import *

import time


main = Tk()

counter4 = 0

AI_run = 1
counter = 0
counter2 = 0

availibleornot = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

pos1 = [527,437]
pos2 = [671,437]
pos3 = [821,437]
pos4 = [971,437]
pos5 = [1127,437]

times = 1

re = False

yeah = 0

tf1 = 0
tf2 = 0
tf3 = 0
tf4 = 0
tf5 = 0
tf6 = 0
tf7 = 0
tf8 = 0
tf9 = 0
tf10 = 0
tf11 = 0
tf12 = 0
tf13 = 0
tf14 = 0
tf15 = 0
tf16 = 0

sheep = False
worm = False
ant = False
bever = False
cricket = False
dog = False
duck = False
elephant = False
giraff = False
money_bird = False
otter = False
phenix = False
pig = False
pink_bird = False
spike = False
moskito = False
horse = False
fish = False
counter4 = 0

sl1 = [523,446]
sl2 = [669,446]
sl3 = [815,446]
sl4 = [961,446]
sl5 = [1107,446]

avialable = []
indeck = []

oldloc = []
oldloc2 = []
oldloc3 = []
oldloc4 = []
oldloc5 = []
oldloc6 = []
oldloc7 = []
oldloc8 = []
oldloc9 = []
oldloc10 = []
oldloc11 = []
oldloc12 = []
oldloc13 = []
oldloc14 = []
oldloc15 = []
oldloc16 = []
oldloc17 = []
oldloc18 = []

loc = []

loc2 = []

loc3 = []

loc4 = []

loc5 = []

loc6 = []

loc7 = []

loc8 = []

loc9 = []

loc10 = []

loc11 = []

loc12 = []

loc13 = []

loc14 = []

loc15 = []

loc16 = []

loc17 = []

loc18 = []

Th2 = 27

oldposy1 = 0
oldposx1 = 0
oldposy12 = 0
oldposx12 = 0
oldposy13 = 0
oldposx13 = 0
oldposy14 = 0
oldposx14 = 0
oldposy15 = 0
oldposx15 = 0
oldposy16 = 0
oldposx16 = 0
oldposy17 = 0
oldposx17 = 0
oldposy18 = 0
oldposx18 = 0
oldposy19 = 0
oldposx19 = 0
oldposx110 = 0
oldposy110 = 0
oldposy111 = 0
oldposx111 = 0
oldposy112 = 0
oldposx112 = 0
oldposy113 = 0
oldposx113 = 0
oldposy114 = 0
oldposx114 = 0
oldposy115 = 0
oldposx115 = 0
oldposy116 = 0
oldposx116 = 0
oldposy117 = 0
oldposx117 = 0
oldposy118 = 0
oldposx118 = 0
threshold = 0.57
counter3 = 0
place2 = 600

trasch = [1090,988]

id_list = [0]


def val(name,location,char_name):
    
    global avialable
    global indeck
    
    if name == True:
        print(len(location))
        
        print(avialable)
        posx = location[1]
        print(location[0])

        print(location[1])
        posy = location[0]


        if len(posx) >= 1 and len(posy) >= 1:
            if posy[0] > 549:
            
                avialable.append(char_name)
            elif posy[0] < 549:
                indeck.append(char_name)  
            if len(posx) >= 30 and len(posy) >= 30:
                halfx = int(len(posx) * 0.5  + 1)
                halfy = int(len(posy) * 0.5  + 1)
                print(halfy)
                print(halfx)
                if posy[halfy + 1] > 549:
            
                    avialable.append(char_name)
                elif posy[halfy + 1] < 549:
                    indeck.append(char_name) 
                    
def toporbottom(posyv,val,availibleornot_):
    global place2
    global availibleornot
    global counter3
    
    for each in range(5):
        if len(posyv) > 0 and len(posyv) > 0:
            if len(posyv) > 0:
                if posyv[1] < 537:
                    if posyv[1] <= place2:
                        if counter3 == 0:
                            availibleornot_[1] = 1
                            availibleornot_[6] = val
                            break
                        elif counter3 == 1:
                            availibleornot_[2] = 1
                            availibleornot_[7] = val
                            break
                        elif counter3 == 2:
                            availibleornot_[3] = 1
                            availibleornot_[8] = val
                            break
                        elif counter3 == 3:
                            availibleornot_[4] = 1
                            availibleornot[9] = val
                            break
                        elif counter3 == 4:
                            availibleornot_[5] = 1
                            availibleornot_[10] = val
                            break
        counter3 = counter3 + 1
        place2 = place2 +  145
    counter3 = 0
    place2 = 600
    availibleornot = availibleornot_

def place_a(name,posxv,posyv,sl1t,sl2t,sl3t,sl4t,sl5t,availibleornot_,gval,i_d):
    
    global availibleornot
    placesl = 0
    wow = 1
    if len(posxv) > Th2:
        wow = 2
        
    for each in range(wow):
        if name == True and availibleornot_ == availibleornot:
            
            counter5 = 0
            
            for i in range(len(id_list)): 
                try:
                    counter5 = counter5 + 1
                    
                    if i_d == id_list(counter5):
                        is_there = True
                        break
                    else:
                        is_there = False
                except:
                    is_there = False
                    
            if is_there == True:
                print("dublicant detected argument " + str(counter5) + " : " + str(is_there))
                start_AI()    
                
                
            
            posx = posxv[0]
            posy = posyv[0]
            halfx = int(len(posxv) / 2 + 1)
            halfy = int(len(posyv) / 2 + 1)
            print("id " + str(i_d))
            
            # placement code
            
            if posy > 549 and is_there == False:
                if i_d != availibleornot_[11] and i_d != availibleornot_[12] and i_d != availibleornot_[13] and i_d != availibleornot_[14] and i_d != availibleornot_[15]:
                    
                    if sl1t == True and availibleornot_[1] + 1 == 1 and availibleornot_[11] == 0:
                        print("place1" + str(availibleornot_[5]) + str(availibleornot_[10]) + str(availibleornot_[15]))
                        pyautogui.click(posx + 50,posy + 90)
                        pyautogui.dragTo(sl1)
                        availibleornot_[6] = gval
                        availibleornot_[1] = 1
                        availibleornot_[11] = i_d
                        placesl = 1
                    elif sl2t == True and availibleornot_[2] + 1 == 1 and availibleornot_[12] == 0:
                        print("place2")
                        pyautogui.click(posx + 50,posy + 90)
                        pyautogui.dragTo(sl2)
                        availibleornot_[7] = gval
                        availibleornot_[2] = 1
                        availibleornot_[12] = i_d
                        placesl = 2
                    elif sl3t == True and availibleornot_[3] + 1 == 1 and availibleornot_[13] == 0:
                        print("place3")
                        pyautogui.click(posx + 50,posy + 90)
                        pyautogui.dragTo(sl3)
                        availibleornot_[8] = gval
                        availibleornot_[3] = 1
                        availibleornot_[13] = i_d
                        placesl = 3
                    elif sl4t == True and availibleornot_[4] + 1 == 1 and availibleornot_[14] == 0:
                        print("place4")
                        pyautogui.click(posx + 50,posy + 90)
                        pyautogui.dragTo(sl4)
                        availibleornot_[9] = gval
                        availibleornot_[4] = 1
                        availibleornot_[14] = i_d
                        placesl = 4
                    elif sl5t == True and availibleornot_[5] + 1 == 1 and availibleornot_[15] == 0:
                        print("place5")
                        pyautogui.click(posx + 50,posy + 90)
                        pyautogui.dragTo(sl5)
                        availibleornot_[10] = gval
                        availibleornot_[5] = 1
                        availibleornot_[15] = i_d
                        placesl = 5
            
            # duplicant code 
                    
            if len(posxv) > Th2:
                print("dub")
                time.sleep(3)
                posy = posyv[halfy + 1]
                posx = posxv[halfx + 1]
                if placesl == 1 or i_d == availibleornot_[11]:
                    pyautogui.click(posx + 50,posy + 90)
                    time.sleep(0.3)
                    pyautogui.dragTo(sl1)
                    availibleornot_[6] = gval * 1.10
                    availibleornot_[1] = 1
                elif placesl == 2 or i_d == availibleornot_[12]:
                    pyautogui.click(posx + 50,posy + 90)
                    time.sleep(0.3)
                    pyautogui.dragTo(sl2)
                    availibleornot_[7] = gval * 1.10
                    availibleornot_[2] = 1
                elif placesl == 3 or i_d == availibleornot_[13]:
                    pyautogui.click(posx + 50,posy + 90)
                    time.sleep(0.3)
                    pyautogui.dragTo(sl3)
                    availibleornot_[8] = gval * 1.10
                    availibleornot_[3] = 1
                elif placesl == 4 or i_d == availibleornot_[14]:
                    pyautogui.click(posx + 50,posy + 90)
                    time.sleep(0.3)
                    pyautogui.dragTo(sl4)
                    availibleornot_[9] = gval * 1.10
                    availibleornot_[4] = 1
                elif placesl == 5 or i_d == availibleornot_[15]:
                    pyautogui.click(posx + 50,posy + 90)
                    time.sleep(0.3)
                    pyautogui.dragTo(sl5)
                    availibleornot_[10] = gval * 1.10
                    availibleornot_[5] = 1
                    
            # delete animal
            
            if availibleornot_[5] == 1 and availibleornot_[4] == 1 and availibleornot_[3] == 1 and availibleornot_[2] == 1 and availibleornot_[1] == 1:
                print("del")
                if gval > availibleornot_[6]:
                    pyautogui.click(sl1)
                    pyautogui.dragTo(trasch)
                    pyautogui.click(posx + 50,posy + 90)
                    pyautogui.dragTo(sl1)
                    availibleornot_[6] = gval
                    availibleornot_[11] = i_d
                elif gval > availibleornot_[7]:
                    pyautogui.click(sl2)
                    pyautogui.dragTo(trasch)
                    pyautogui.click(posx + 8,posy + 90)
                    pyautogui.dragTo(sl2)
                    availibleornot_[7] = gval
                    availibleornot_[12] = i_d
                elif gval > availibleornot_[8]:
                    pyautogui.click(sl3)
                    pyautogui.dragTo(trasch)
                    pyautogui.click(posx + 50,posy + 90)
                    pyautogui.dragTo(sl3)
                    availibleornot_[8] = gval
                    availibleornot_[13] = i_d
                elif gval > availibleornot_[9]:
                    pyautogui.click(sl4)
                    pyautogui.dragTo(trasch)
                    pyautogui.click(posx + 50,posy + 90)
                    pyautogui.dragTo(sl4)
                    availibleornot_[9] = gval
                    availibleornot_[14] = i_d
                elif gval > availibleornot_[10]:
                    pyautogui.click(sl5)
                    pyautogui.dragTo(trasch)
                    pyautogui.click(posx + 50,posy + 90)
                    pyautogui.dragTo(sl5)
                    availibleornot_[10] = gval
                    availibleornot_[15] = i_d
            id_list.append(i_d)
            print("test" + str(availibleornot_))
            availibleornot = availibleornot_
            

def start_AI():
    
    global re
    
    global id_list
    
    global tf1
    global tf2
    global tf3
    global tf4
    global tf5
    global tf6
    global tf7
    global tf8
    global tf9
    global tf10
    global tf11
    global tf12  
    global tf13
    global tf14
    global tf15
    global tf16  
    
    global loc

    global loc2

    global loc3

    global loc4

    global loc5

    global loc6

    global loc7

    global loc8

    global loc9

    global loc10

    global loc11

    global loc12

    global loc13

    global loc14

    global loc15

    global loc16

    global loc17

    global loc18
    
    global indeck
    global sheep 
    global AI_run
    global worm
    
    global oldloc
    global oldloc2
    global oldloc3
    global oldloc4
    global oldloc5
    global oldloc6
    global oldloc7
    global oldloc8
    global oldloc9
    global oldloc10
    global oldloc11
    global oldloc12
    global oldloc13
    global oldloc14
    global oldloc15
    global oldloc16
    global oldloc17
    global oldloc18
    
    global ant
    global bever 
    global cricket
    global dog
    global duck
    global elephant
    global giraff
    global money_bird
    global otter
    global phenix
    global pig
    global pink_bird
    global spike
    global moskito
    global horse
    global fish
    global counter2
    
    global Th2
    
    place = 527
    
    global counter4
    
    global oldposx1
    global oldposy1
    global oldposx12
    global oldposy12
    global oldposx13
    global oldposy13
    global oldposx14
    global oldposy14
    global oldposx15
    global oldposy15
    global oldposx16
    global oldposy16
    global oldposx17
    global oldposy17
    global oldposx18
    global oldposy18
    global oldposx19
    global oldposy19
    global oldposx110
    global oldposy110
    global oldposx111
    global oldposy111
    global oldposx112
    global oldposy112
    global oldposx113
    global oldposy113
    global oldposx114
    global oldposy114
    global oldposx115
    global oldposy115
    global oldposx116
    global oldposy116
    global oldposx117
    global oldposy117
    global oldposx118
    global oldposy118
    
    global counter4
    
    global yeah
           
    print(" \n counter value : " + str(counter4) + "\n")
    
    text.configure(text="all animals :")
    #all the variables
    
    img_rgb = pyautogui.screenshot()
    img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_BGR2GRAY)
    charsheep = cv2.imread('sheep.png',0)
    charworm = cv2.imread('worm.png',0)
    charant = cv2.imread('ant.png',0)
    charbever = cv2.imread('bever.png',0)
    charcricket = cv2.imread('cricket.png',0)
    chardog = cv2.imread('dog.png',0)
    charduck = cv2.imread('duck.png',0)
    charelephant = cv2.imread('elephant.png',0)
    chargiraff = cv2.imread('giraff.png',0)
    charmoney = cv2.imread('money_bird.png',0)
    charotter = cv2.imread('otter.png',0)
    charpohenix = cv2.imread('phenix.png',0)
    charpig = cv2.imread('pig.png',0)
    charpink_bird = cv2.imread('pink_bird.png',0)
    charspike = cv2.imread('spike_fish.png',0)
    charmoskito = cv2.imread('moskito_v2.png',0)
    charhorse = cv2.imread('horse.png',0)
    charfish = cv2.imread('fish.png',0)
    
    #part that does the detecting
    
    w, h = charsheep.shape[::-1]
    detectsheep = cv2.matchTemplate(img_gray,charsheep,cv2.TM_CCOEFF_NORMED)
    detectworm = cv2.matchTemplate(img_gray,charworm,cv2.TM_CCOEFF_NORMED)
    detectant = cv2.matchTemplate(img_gray,charant,cv2.TM_CCOEFF_NORMED)
    detectbever = cv2.matchTemplate(img_gray,charbever,cv2.TM_CCOEFF_NORMED)
    detectcricket = cv2.matchTemplate(img_gray,charcricket,cv2.TM_CCOEFF_NORMED)
    detectdog = cv2.matchTemplate(img_gray,chardog,cv2.TM_CCOEFF_NORMED)
    detectduck = cv2.matchTemplate(img_gray,charduck,cv2.TM_CCOEFF_NORMED)
    detectelephant = cv2.matchTemplate(img_gray,charelephant,cv2.TM_CCOEFF_NORMED)
    detectgiraff = cv2.matchTemplate(img_gray,chargiraff,cv2.TM_CCOEFF_NORMED)
    detectmoney = cv2.matchTemplate(img_gray,charmoney,cv2.TM_CCOEFF_NORMED)
    detectotter = cv2.matchTemplate(img_gray,charotter,cv2.TM_CCOEFF_NORMED)
    detectphenix = cv2.matchTemplate(img_gray,charpohenix,cv2.TM_CCOEFF_NORMED)
    detectpig = cv2.matchTemplate(img_gray,charpig,cv2.TM_CCOEFF_NORMED)
    detectpink_bird = cv2.matchTemplate(img_gray,charpink_bird,cv2.TM_CCOEFF_NORMED)
    detectspike= cv2.matchTemplate(img_gray,charspike,cv2.TM_CCOEFF_NORMED)
    detectmoskito= cv2.matchTemplate(img_gray,charmoskito,cv2.TM_CCOEFF_NORMED)
    detecthorse= cv2.matchTemplate(img_gray,charhorse,cv2.TM_CCOEFF_NORMED)
    detectfish = cv2.matchTemplate(img_gray,charfish,cv2.TM_CCOEFF_NORMED)
    threshold = 0.57
    
    #draws the square
    
    loc = np.where( detectsheep >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            sheep = True
        
    loc2 = np.where( detectworm >= threshold)
    for pt in zip(*loc2[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            worm = True
    loc3 = np.where( detectant >= threshold)
    for pt in zip(*loc3[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            ant = True
    loc4 = np.where( detectbever >= threshold)
    for pt in zip(*loc4[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            bever = True
        
    loc5 = np.where( detectcricket >= threshold)
    for pt in zip(*loc5[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            cricket = True
    loc6 = np.where( detectdog >= threshold)
    for pt in zip(*loc6[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            dog = True
    loc7 = np.where( detectduck >= threshold)
    for pt in zip(*loc7[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            duck = True
        
    loc8 = np.where( detectelephant >= threshold)
    for pt in zip(*loc8[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            elephant = True
    loc9 = np.where( detectgiraff >= threshold)
    for pt in zip(*loc9[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            giraff = True
    loc10 = np.where( detectmoney >= threshold)
    for pt in zip(*loc10[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            money_bird = True
        
    loc11 = np.where( detectotter >= threshold)
    for pt in zip(*loc11[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            otter = True
    loc12 = np.where( detectphenix >= threshold)
    for pt in zip(*loc12[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            phenix = True
    loc13 = np.where( detectpig >= threshold)
    for pt in zip(*loc13[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            pig = True
    loc14 = np.where( detectpink_bird >= threshold)
    for pt in zip(*loc14[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            pink_bird = True
    loc15 = np.where( detectspike >= threshold)
    for pt in zip(*loc15[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            spike = True
    loc16 = np.where( detectmoskito >= threshold)
    for pt in zip(*loc16[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            moskito = True
    loc17 = np.where( detecthorse >= threshold)
    for pt in zip(*loc17[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            horse = True
    loc18 = np.where( detectfish >= threshold)
    for pt in zip(*loc18[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        if w > 0:
            fish = True

                
    #showes the image
    
    cv2.imwrite('res.png',img_rgb)
    cv2.imshow('result',imutils.resize(img_rgb, width=1000))
    print("sheep : " + str(sheep))
    print("worm : " + str(worm))
    print("ant : " + str(ant))
    print("bever : " + str(bever))
    print("cricket : " + str(cricket))
    print("dog : " + str(dog))
    print("duck : " + str(duck))
    print("elephant : " + str(elephant))
    print("giraff : " + str(giraff))
    print("money bird : " + str(money_bird))
    print("otter : " + str(otter))
    print("phenix : " + str(phenix))
    print("pig : " + str(pig))
    print("pink bird : " + str(pink_bird))
    print("spike fish : " + str(spike))
    print("moskito : " + str(moskito))
    print("horse : " + str(horse))
    print("fish : " + str(fish))
    
    txtant.configure(text="ant : " + str(ant))
    txtbever.configure(text="bever : " + str(bever))
    txtcricket.configure(text="cricket : " + str(cricket))
    txtdog.configure(text="dog : " + str(dog))
    txtduck.configure(text="duck : " + str(duck))
    txtelephant.configure(text="elephant : " + str(elephant))
    txtgirff.configure(text="giraff : " + str(giraff))
    txtmoney_bird.configure(text="money bird : " + str(money_bird))
    txtotter.configure(text="otter : " + str(otter))
    txtphenix.configure(text="phenix : " + str(phenix))
    txtpig.configure(text="pig : " + str(pig))
    txtpink_bird.configure(text="pink bird : " + str(pink_bird))
    txtspike.configure(text="spike fish : " + str(spike))
    txtworm.configure(text="worm : " + str(worm))
    txtsheep.configure(text="sheep : " + str(sheep))
    txtmokito.configure(text="moskito : " + str(moskito))
    txthorse.configure(text="horse : " + str(horse))
    txtfish.configure(text="fish : " + str(fish))
    
    
    text.pack()
    txtant.pack()
    txtbever.pack()
    txtcricket.pack()
    txtdog.pack()
    txtduck.pack()
    txtelephant.pack()
    
    txtgirff.pack()
    txtmoney_bird.pack()
    txtotter.pack()
    txtphenix.pack()
    txtpig.pack()
    txtpink_bird.pack()
    
    txtspike.pack()
    txtworm.pack()
    txtsheep.pack()
    txtmokito.pack()
    txthorse.pack()
    txtfish.pack()
    
    # sets values for all chars 
    
    val(name = sheep,location = loc,char_name = "sheep")

    val(name = worm,location = loc2,char_name = "worm")

    val(name = ant,location = loc3,char_name = "ant")
    
    val(name = bever,location = loc4,char_name = "bever")
    
    val(name = cricket,location = loc5,char_name = "cricket")

    val(name = dog,location = loc6,char_name = "dog")
        
    val(name = duck,location = loc7,char_name = "duck")
        
    val(name = elephant,location =loc8,char_name = "elephant")
    
    val(name = elephant,location =loc8,char_name = "elephant")

    val(name = giraff,location =loc9,char_name = "giraff")

    val(name = money_bird,location =loc10,char_name = "money bird")
    
    val(name = otter,location = loc11,char_name = "otter")
    
    val(name = phenix,location = loc12,char_name = "phenix")

    val(name = pig,location = loc13,char_name = "pig")
    
    val(name = pink_bird,location =loc14,char_name = "pink bird")
    
    val(name = spike,location =loc15,char_name = "spike")

    val(name = moskito,location =loc16,char_name = "moskito")

    val(name = horse,location =loc17,char_name = "horse")

    val(name = fish,location =loc18,char_name = "fish")

        
    
        
    print("animals in deck : " + str(indeck))
    print("availible animals : " + str(avialable))
    indeck.clear()
    avialable.clear()
    
    sposx = loc[1]
    sposy = loc[0]
    wposx = loc2[1]
    wposy = loc2[0]
    aposx = loc3[1]
    aposy = loc3[0]
    bposx = loc4[1]
    bposy = loc4[0]
    cposx = loc5[1]
    cposy = loc5[0]
    dposx = loc6[1]
    dposy = loc6[0]
    duposx = loc7[1]
    duposy = loc7[0]
    eposx = loc8[1]
    eposy = loc8[0]
    gposx = loc9[1]
    gposy = loc9[0]
    mposx = loc10[1]
    mposy = loc10[0]
    oposx = loc11[1]
    oposy = loc11[0]
    pposx = loc12[1]
    pposy = loc12[0]
    piposx = loc13[1]
    piposy = loc13[0]
    pinposx = loc14[1]
    pinposy = loc14[0]
    spposx = loc15[1]
    spposy = loc15[0]
    moposx = loc16[1]
    moposy = loc16[0]
    hposx = loc17[1]
    hposy = loc17[0]
    fposx = loc18[1]
    fposy = loc18[0]
    place2 = 600
    counter3 = 0
    availibleornot = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sl1 = [523,446]
    sl2 = [669,446]
    sl3 = [815,446]
    sl4 = [961,446]
    sl5 = [1107,446]
    
    wval = 9
    sval = 20
    aval = 15
    bval = 13
    cval = 16
    dval = 12
    duval = 13
    eval = 17
    fval = 15
    gival = 17
    hval = 25
    mval = 17
    moval = 19
    oval = 13
    pval = 18
    pival = 13
    pinkval = 20
    spval = 19
    
    # constants
    gval = 0
    

    
    
    toporbottom(posyv = wposy,val = wval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = fposy,val = fval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = aposy,val = aval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = bposy,val = bval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = cposy,val = cval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = dposy,val = dval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = duposy,val = duval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = eposy,val = eval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = gposy,val = gval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = hposy,val = hval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = mposy,val = mval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = moposy,val = moval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = oposy,val = oval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = pposy,val = pval,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = piposy,val = pival,availibleornot_ = availibleornot)
    
    
    toporbottom(posyv = pinposy,val = pinkval,availibleornot_ = availibleornot)


    print("st " + str(availibleornot))
    
    counter4 = 0
    
    if yeah == 0:
        
        yeah = 1
        start_AI()

    elif yeah == 1:
        yeah = 0
    
    
    if tf15 == 0 and len(wposx) > 0:
        place_a(name = worm,posxv = wposx,posyv = wposy,sl1t = True,sl2t = True,sl3t = False,sl4t = False,sl5t = False,availibleornot_ = availibleornot,gval = wval,i_d = 1)
        tf15 = 1
        counter4 = 1
        start_AI()

    elif tf1 == 0 and len(fposx) > 0:
        place_a(name = fish,posxv = fposx,posyv = fposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = fval,i_d = 2)
        tf1 = 1
        counter4 = 2
        start_AI()

    elif tf2 == 0 and len(aposx) > 0:
        place_a(name = ant,posxv = aposx,posyv = aposy,sl1t = False,sl2t = False,sl3t = False,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = aval,i_d = 3)
        tf2 = 2
        counter4 = 3
        start_AI()

    elif tf3 == 0 and len(bposx) > 0:
        place_a(name = bever,posxv = bposx,posyv = bposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = bval,i_d = 4)
        tf3 = 1
        counter4 = 4
        start_AI()

    elif tf4 == 0 and len(cposx) > 0:
        place_a(name = cricket,posxv = cposx,posyv = cposy,sl1t = False,sl2t = False,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = cval,i_d = 5)
        tf4 = 1
        counter4 = 5
        start_AI()

    elif tf5 == 0 and len(dposx) > 0:
        place_a(name = dog,posxv = dposx,posyv = dposy,sl1t = True ,sl2t = True,sl3t = False,sl4t = False,sl5t = False,availibleornot_ = availibleornot,gval = dval,i_d = 6)
        tf5 = 1
        counter4 = 6
        start_AI()
    
    elif tf6 == 0 and len(duposx) > 0:
        place_a(name = duck,posxv = duposx,posyv = duposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = duval,i_d = 7)
        tf6 = 1
        counter4 =7
        start_AI()
        
    elif tf7 == 0 and len(eposx) > 0:
        place_a(name = elephant,posxv = eposx,posyv = eposy,sl1t = True,sl2t = False,sl3t = False,sl4t = False,sl5t = False,availibleornot_ = availibleornot,gval = eval,i_d = 8)
        tf7 = 1
        counter4 = 8
        start_AI()
        
    elif tf8 == 0 and len(gposx) > 0:    
        place_a(name = giraff,posxv = gposx,posyv = gposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = False,availibleornot_ = availibleornot,gval = gival,i_d = 9)            
        tf8 = 1
        counter4 = 9
        start_AI()
        
    elif tf9 == 0 and len(hposx) > 0:
        place_a(name = horse,posxv = hposx,posyv = hposy,sl1t = True,sl2t = True,sl3t = False,sl4t = False,sl5t = False,availibleornot_ = availibleornot,gval = hval,i_d = 10)
        tf9 = 1
        counter4 = 10
        start_AI()
        
    elif tf10 == 0 and len(mposx) > 0:
        place_a(name = money_bird,posxv = mposx,posyv = mposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = mval,i_d = 11)
        tf10 = 1
        counter4 = 11
        start_AI()
        
    elif tf11 == 0 and len(moposx) > 0:
        place_a(name = moskito,posxv = moposx,posyv = moposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = moval,i_d = 12)
        tf11 = 1
        start_AI()
        
    elif tf12 == 0 and len(oposx) > 0:                
        place_a(name = otter,posxv = oposx,posyv = oposy,sl1t = True,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = oval,i_d = 13)
        tf12 = 1
        counter4 = 12
        start_AI()
        
    elif tf13 == 0 and len(pposx) > 0:   
        place_a(name = phenix,posxv = pposx,posyv = pposy,sl1t = False,sl2t = True,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = pval,i_d = 14)
        tf13 = 1
        counter4 = 13
        start_AI()
        
    elif tf14 == 0 and len(piposx) > 0:
        place_a(name = pig,posxv = piposx,posyv = piposy,sl1t =True ,sl2t =True ,sl3t =True ,sl4t =True ,sl5t = True ,availibleornot_ = availibleornot,gval = pival,i_d = 15)
        tf14 = 1
        counter4 = 14
        start_AI()
        
    elif tf15 == 0 and len(pinposx) > 0:
        place_a(name = pink_bird,posxv = pinposx,posyv = pinposy,sl1t = False,sl2t = False,sl3t = True,sl4t = True,sl5t = True,availibleornot_ = availibleornot,gval = pinkval,i_d = 16)
        tf16 = 1
        counter4 = 15
        re = True
        start_AI()
                        

    if re == True:
        tf1 = 0
        tf2 = 0
        tf3 = 0
        tf4 = 0
        tf5 = 0
        tf6 = 0
        tf7 = 0
        tf8 = 0
        tf9 = 0
        tf10 = 0
        tf11 = 0
        tf12 = 0
        tf13 = 0
        tf14 = 0
        tf15 = 0
        tf16 = 0
        
        id_list = []
                 

 
                
    print("fin " + str(availibleornot))

                    
                    
    # if pyautogui.position() != (1698,981) and pyautogui.position() != (100,100):
    #     pyautogui.click(1598,1005)
    #     pyautogui.click(1246,663)
    #     pyautogui.click(930,395)
    #     pyautogui.click(930,693)
    #     pyautogui.click(1698,981)
    # else:
    #     pyautogui.click(100,100)
    
    


    worm = False
    sheep = False
    ant = False
    bever = False
    cricket= False
    dog= False
    duck= False
    elephant= False
    giraff= False
    money_bird= False
    otter= False
    phenix= False
    pig= False
    pink_bird= False
    spike= False
    moskito= False
    horse= False
    fish= False
    

    if AI_run == 1:
        print("\n")
        text.after(5000,start_AI)

    else:
        print("stop")
        
def stop_AI():
    global counter
    global AI_run
    if counter == 0:
    
        AI_run = 0
        counter = 1
        print(AI_run)
        b2.configure(text="restart_AI")
    elif counter == 1:
        counter = 0
        AI_run = 1
        b2.configure(text="stop_AI")
        print("on")

main.title("AI")

b1 = Button(main,text="start AI",command=start_AI)

text = Label(main,text="")

b2 = Button(main,text="stop AI",command=stop_AI)

txtant = Label(main,text="")

txtbever = Label(main,text="")

txtcricket = Label(main,text="")

txtdog = Label(main,text="")

txtduck = Label(main,text="")

txtelephant = Label(main,text="")

txtgirff = Label(main,text="")

txtmoney_bird = Label(main,text="")

txtotter = Label(main,text="")

txtphenix = Label(main,text="")

txtpig = Label(main,text="")

txtpink_bird = Label(main,text="")

txtspike = Label(main,text="")

txtworm = Label(main,text="")

txtsheep = Label(main,text="")

txtmokito = Label(main,text="")

txthorse = Label(main,text="")

txtfish = Label(main,text="")

b1.pack()
b2.pack()
main.mainloop()