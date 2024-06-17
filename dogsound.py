#!/usr/bin/env python3
import time

import pygame


class FakeDog():
    """Plays a sound to simulate a dog barking.

    The sound is played only if the last time it was played was more than `cooldown` seconds ago.
    """

    def __init__(self, filename="./dog-barking.mp3", cooldown=30):
        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(filename)
        self.last_sound_played_at = 0  # start at 0 so that sound always plays first time
        self.cooldown = cooldown

    def alert(self):
        elapsed = time.time() - self.last_sound_played_at
        if elapsed > self.cooldown:
            print(f"Playing sound!")
            self.sound.play()
            self.last_sound_played_at = time.time()
        else:
            print(f"Last sound was played {elapsed:.1f} seconds ago - too recent to play again")


if __name__ == "__main__":
    print("Testing dog alert...")
    FakeDog().alert()
