#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2 as cv
import numpy as np 
import os
import time


# In[2]:


prompt='Input person`s name eg oswell_musariri NB NO SPACES ALLOWED'
print(prompt)
personname=input()
video_name=personname + '.avi'


# In[3]:


def record_train_video():
    cap=cv.VideoCapture(0)
    frame_width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    
    output=cv.VideoWriter(personname+'.avi',cv.VideoWriter_fourcc('M','J','P','G'),8,(frame_width,frame_height))
    while True:
        ret, frame=cap.read()
        output.write(frame)
        cv.imshow("person_me",frame)
        
        k=cv.waitKey(30)&0xff
        if k==27:
            break


# In[4]:


def make_rawtrain_dataset():
    video_path=video_name
    print(video_name)
    cap = cv.VideoCapture(video_name)
    owd = os.getcwd()
    
    file_path_img="person_"+ personname
    file_path_img_dir="/image_dir/"+file_path_img
    if not os.path.exists("image_dir"):
        os.mkdir("image_dir")
    os.chdir("image_dir")
    if not os.path.exists(file_path_img):
        os.mkdir(file_path_img)
        
    os.chdir(owd)
    i=0
    while True:
        ret, image = cap.read()
        value = image is None
        if not(value):
            cv.imshow('original',image)
            image_name = file_path_img+'/'+str(i) + '.png'
            cv.imwrite(image_name, image)
        
        i=i+1
        k = cv.waitKey(30) & 0xff
        if k==27 or i==200 or value:
            break
    cap.release()
    cv.destroyAllWindows()


# In[5]:


record_train_video()


# In[ ]:


make_rawtrain_dataset()
#given input from calling program is the the subject's name with underscore not space/ or employee id


# In[ ]:


cv.destroyAllWindows()

