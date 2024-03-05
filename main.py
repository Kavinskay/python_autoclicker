import pyautogui as pt
from time import sleep


class Clicker:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.9)
            pt.moveTo(position[0] + 30, position[1] + 30, duration=self.speed)
            pt.doubleClick()

        except:
            print("no image found...")
            return 0


if __name__ == "__main__":
    sleep(2)
    Clicker = Clicker("images\cirkel_png.PNG", speed=0.001)

    end = 0
    while True:
        if Clicker.nav_to_image() == 0:
            end += 1

        if end > 100:
            break
