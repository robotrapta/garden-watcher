#!/usr/bin/env python3
import time

from groundlight import Groundlight
import pygame

def main():
    print("Deerbark connecting to Groundlight")
    gl = Groundlight()
    print("Connected to Groundlight")
    print(gl)

    pygame.init()
    pygame.mixer.init()
    SOUND = pygame.mixer.Sound("./dog-barking.mp3")

    while True:
        print("barking!")
        SOUND.play()
        print("waiting")
        time.sleep(10)

if __name__ == "__main__":
    main()
