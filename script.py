import cv2
import os
import numpy as np
import random
# import tensorflow as tf
# import tqdm as tqdm
# import matplotlib.pyplot as plt

daisy = "/flowers/daisy"
roses = "/flowers/roses"
SIZE = 128
RATIO = 0.7
# cd = os.getcwd()

daisy_files = [] # Files Containing on the Daisy Folder
roses_files = [] # Files Containing on the roses folder

def read_directories():
    global daisy_files
    global roses_files
    daisy_files = os.listdir('.' + daisy) 
    roses_files = os.listdir('.' + roses) 

def import_files():
    all_data = [] # all the data daisy + roses in grayscale format
    training_data = []
    testing_data = []
    # DAISY ===> Label = 1
    # for each daisy image
    for dsy in daisy_files:
        # convert that image into a grayscale
        img = cv2.imread('.' + daisy + '/' + dsy ,cv2.IMREAD_GRAYSCALE)
        # resize the image
        img = cv2.resize(img,(SIZE,SIZE))
        # Add the image as an array with a label 1 in all data
        all_data.append([np.array(img),1])
    
    # ROSES ===> Label = 2
    for ros in roses_files:
        img = cv2.imread('.' + roses + '/' + ros ,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img,(SIZE,SIZE))
        all_data.append([np.array(img),2])
    
    random.shuffle(all_data)
    length  = len(all_data)
    train_count = int(length * RATIO)
    training_data = all_data[:train_count]
    testing_data = all_data[train_count:]
    ############# MESSAGES ##########
    print("TOTAL LENGTH OF DATA : ",length)
    print("RATIO OF DIVIDING DATA : ",(RATIO*100))
    print("TOTAL LENGTH OF TRAINING DATA : ",train_count)
    print("TOTAL LENGTH OF TESTING DATA : ",(length - train_count))
    return training_data,testing_data

# print(os.getcwd())
read_directories()
import_files()