# Package Imports
import time
import torch
import numpy as np
from torchvision import models, transforms
import cv2
from PIL import Image
import json
#import matlab.engine

# Helper Function Inputs
import imagerecog
#import lightbulbDetect

start_time = time.time()

while (True):
    now_time = time.time()
    time_diff = int(now_time - start_time) # Seconds
    if time_diff % 20 == 0:
        detected = imagerecog.image_recog_one_frame()
        print(detected)
        exit()
        continue