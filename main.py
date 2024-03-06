import pyautogui as pt
from time import sleep

class Close_IDE:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            pt.doubleClick()

        except:
            print("Can't close IDE")
            return 0
        
class Alteryx_clicker:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
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
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.doubleClick()

        except:
            print("Can not find alteryx script in folder")
            return 0
        
class Close_popup:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        #try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        #except:
            print("No popup found or can't close")
            return 0


class Run_clicker:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        #try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        #except:
            print("Cannot run script, image not found")
            return 0


if __name__ == "__main__":
    sleep(2)
    Clicker = Close_IDE('images/Close_python.PNG', speed=.001)
    Clicker_1 = Alteryx_clicker('images/Alteryx_pipelines/GA_script.PNG', speed=.001) # NOG PARAMETERISEREN
    Clicker_2 = Script_clicker('images/GA_script.PNG', speed=.001)
    Clicker_3 = Close_popup('images\close_popup.PNG', speed=.001)
    Clicker_4 = Run_clicker('images/Run_button.PNG', speed=.001)

    end = 0 
    while True:
        Clicker.nav_to_image()
        sleep(1)       
        Clicker_1.nav_to_image()
        sleep(1)
        Clicker_2.nav_to_image()
        sleep(20)
        Clicker_3.nav_to_image()
        sleep(1)
        Clicker_4.nav_to_image()
