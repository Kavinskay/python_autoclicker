import pyautogui as pt
from time import sleep


class Alteryx_clicker:
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
            print("Alteryx folder not found")
            return 0


class Script_clicker:
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
            print("Can not find alteryx script in folder")
            return 0


class Run_clicker:
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
            print("Cannot run script, image not found")
            return 0


if __name__ == "__main__":
    sleep(2)
    Clicker_1 = Alteryx_clicker("images\Alteryx_scripts.PNG", speed=0.001)
    sleep(20)
    Clicker_2 = Script_clicker("images\GA_script.PNG", speed=0.001)
    sleep(120)
    Clicker_3 = Run_clicker("images\Run_button.PNG", speed=0.001)

    # end = 0
    # while True:
    #     if Clicker.nav_to_image() == 0:
    #         end += 1

    #     if end > 10:
    #         break
