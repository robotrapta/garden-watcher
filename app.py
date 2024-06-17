#!/usr/bin/env python3
import time

from groundlight import Groundlight
from imgcat import imgcat
import cv2
import framegrab
import pygame

camera = framegrab.FrameGrabber.from_yaml("./framegrab.yaml")[0]
motdet = framegrab.MotionDetector(pct_threshold=1, val_threshold=50)


def main():
    gl = Groundlight()

    pygame.init()
    pygame.mixer.init()
    SOUND = pygame.mixer.Sound("./dog-barking.mp3")

    while True:
        print("grabbing")
        img = camera.grab()  # img is a numpy array
        print(f"grabbed image of size {img.shape}")
        # Resize the numpy array to 800x600
        img = cv2.resize(img, (800, 600))
        if motdet.motion_detected(img):
            print("motion")
            imgcat(img)
        else:
            print("no motion")
            time.sleep(0.05)
            continue
        #SOUND.play()
        print("waiting")
        #time.sleep(10)

if __name__ == "__main__":
    main()
