import cv2
import os
# import numpy as np
# import random
# import tensorflow as tf
# import tqdm as tqdm
# import matplotlib.pyplot as plt

daisy = "/flowers/daisy"
roses = "/flowers/roses"
# cd = os.getcwd()

daisy_files = [] # Files Containing on the Daisy Folder
roses_files = [] # Files Containing on the roses folder

def read_directories():
    global daisy_files
    global roses_files
    daisy_files = os.listdir('.' + daisy) 
    roses_files = os.listdir('.' + roses) 

def import_files():
    
    return 0

# print(os.getcwd())
read_directories()