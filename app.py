#!/usr/bin/env python3
import time

from groundlight import Groundlight
from imgcat import imgcat
import cv2
import framegrab
import pygame

def main():
    camera = framegrab.FrameGrabber.from_yaml("./framegrab.yaml")[0]
    motdet = framegrab.MotionDetector(pct_threshold=5, val_threshold=50)

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("./dog-barking.mp3")
    last_sound_played_at = 0

    gl = Groundlight()
    detector = gl.get_or_create_detector(
        name="deerbark",
        query="Can you see any animals?"
    )

    while True:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        big_img = camera.grab()  # img is a numpy array
        img = cv2.resize(big_img, (800, 600))
        if not motdet.motion_detected(img):
            print(f"no motion at {now}")
        else:
            imgcat(img)
            img_query = gl.ask_ml(detector=detector, image=big_img)
            if img_query.result.label == "YES":
                print(f"Animal detected at {now}! {img_query}")
                elapsed = time.time() - last_sound_played_at
                if elapsed > 30:
                    print("Playing sound!")
                    sound.play()
                    last_sound_played_at = time.time()
                else:
                    print(f"Last sound was played {elapsed:.1f} seconds ago - too recent to play again")
            else:
                print(f"No animal found at {now}: {img_query.result}")
        time.sleep(5)

if __name__ == "__main__":
    main()