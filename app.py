#!/usr/bin/env python3
import time

from groundlight import Groundlight
from imgcat import imgcat
import framegrab
import pygame

def next_image():
    global camera
    if camera is None:
        camera = framegrab.FrameGrabber.create_grabber_yaml("./framegrab.yaml")
    return camera.grab()

def main():
    gl = Groundlight()

    pygame.init()
    pygame.mixer.init()
    SOUND = pygame.mixer.Sound("./dog-barking.mp3")

    while True:
        img = next_image()
        imgcat(img)
        print("barking!")
        #SOUND.play()
        print("waiting")
        #time.sleep(10)

if __name__ == "__main__":
    main()
