#!/usr/bin/env python3
import time

from groundlight import Groundlight
from imgcat import imgcat
import cv2
import framegrab
import pygame

def main():
    camera = framegrab.FrameGrabber.from_yaml("./framegrab.yaml")[0]
    motdet = framegrab.MotionDetector(pct_threshold=1, val_threshold=50)

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("./dog-barking.mp3")
    last_sound = 0

    gl = Groundlight()
    detector = gl.get_or_create_detector(
        name="deerbark",
        query="Can you see any animals?"
    )

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
            time.sleep(0.5)
            continue

        img_query = gl.ask_ml(detector=detector, image=img)
        if img_query.result.label == "YES":
            print(f"FOUND animal! {img_query}")
            elapsed = time.time() - last_sound
            if elapsed > 30:
                print("Playing sound!")
                sound.play()
                last_sound = time.time()
            else:
                print(f"Last sound was played {elapsed:.1f} seconds ago - too recent to play again")
        else:
            print(f"No animal found: {img_query.result}")


if __name__ == "__main__":
    main()
