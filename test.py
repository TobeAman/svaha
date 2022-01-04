#encodeing:utf-8
import subprocess
import time
import random
import cv2
import os
import shutil
import threading
from api import *
from datetime import datetime

if __name__ == '__main__':
    try:
        yuhun()
    except KeyboardInterrupt:
        print("exit!")
