#!/usr/bin/env python3
import time

from groundlight import Groundlight
from imgcat import imgcat
import framegrab
import pygame

camera = framegrab.FrameGrabber.from_yaml("./framegrab.yaml")[0]


def main():
    gl = Groundlight()

    pygame.init()
    pygame.mixer.init()
    SOUND = pygame.mixer.Sound("./dog-barking.mp3")

    while True:
        img = camera.grab()
        imgcat(img)
        print("barking!")
        #SOUND.play()
        print("waiting")
        #time.sleep(10)

if __name__ == "__main__":
    main()
