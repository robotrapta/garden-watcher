#!/usr/bin/env python3
import time
import traceback

from groundlight import Groundlight
from imgcat import imgcat
import cv2
import framegrab
import pygame

class GardenWatcher():

    def __init__(self):
        self.camera = framegrab.FrameGrabber.from_yaml("./framegrab.yaml")[0]
        self.motdet = framegrab.MotionDetector(pct_threshold=3, val_threshold=50)

        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("./dog-barking.mp3")
        self.last_sound_played_at = 0  # start at 0 so that sound always plays first time

        self.gl = Groundlight()
        self.detector = self.gl.get_or_create_detector(
            name="deerbark",
            query="Can you see any animals?"
        )

    def run(self):
        while True:
            try:
                self.process_frame()
            except Exception as e:
                traceback.print_exc()
                time.sleep(60)
    
    def process_frame(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        big_img = self.camera.grab()  # big_img is a numpy array
        img = cv2.resize(big_img, (800, 600))  # smaller for preview and motdet
        if not self.motdet.motion_detected(img):
            print(f"no motion at {now}")
        else:
            imgcat(img)
            img_query = self.gl.ask_ml(detector=self.detector, image=big_img)
            if img_query.result.label == "YES":
                print(f"Animal detected at {now}! {img_query}")
                elapsed = time.time() - self.last_sound_played_at
                if elapsed > 30:
                    print("Playing sound!")
                    self.sound.play()
                    self.last_sound_played_at = time.time()
                else:
                    print(f"Last sound was played {elapsed:.1f} seconds ago - too recent to play again")
            else:
                print(f"No animal found at {now}: {img_query}")
        time.sleep(5)

if __name__ == "__main__":
    GardenWatcher().run()
