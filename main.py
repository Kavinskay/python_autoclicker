import pyautogui as pt
import glob
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
        
class Folder_clicker:
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
    def __init__(self, image, speed) -> None:
        self.target_png = image
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_script(self):
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
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        except:
            print("No popup found or can't close")
            return 0


class Run_clicker:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        except:
            print("Cannot run script, image not found")
            return 0
    
class Done:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        except:
            print("Run not done or can't close window")
            return 0
    
class Close_alteryx:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        except:
            print("Can't close alteryx window")
            return 0


class Second_popup:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=0.8)
            pt.moveTo(position[0] + 10, position[1] + 10, duration=self.speed)
            pt.click()

        except:
            print("No second popup found or can't close window")
            return 0

if __name__ == "__main__":
    pt.FAILSAFE = True
    sleep(2)
    Close_ide = Close_IDE('images/Close_python.PNG', speed=.001)
    Click_folder = Folder_clicker('images/Folder.PNG', speed=.001) 
    Popup_closer = Close_popup('images\close_popup.PNG', speed=.001)
    Run = Run_clicker('images/Run_button.PNG', speed=.001)
    Click_done = Done('images\Done_button.PNG', speed=.001)
    End_Alteryx = Close_alteryx('images\Close_alteryx.PNG', speed=.001)
    Popup_closer2 = Second_popup('images\Alteryx_pop_up.PNG', speed=.001)

    end = 0 
    while True:
        Close_ide.nav_to_image()
        sleep(1)       
        Click_folder.nav_to_image()

        images = glob.glob('images\Alteryx_pipelines/*.PNG')

        for image in images: 
            Script = Script_clicker(image, speed=.001)
            sleep(1)
            Script.nav_to_script()
            sleep(20)
            Popup_closer.nav_to_image()
            sleep(1)
            Run.nav_to_image()
            sleep(1)

            for run in range(60): 
                succeeded = Click_done.nav_to_image() != 0
                if succeeded:
                    break
                else:
                    sleep(60)
            
            if not succeeded:
                print(f"Run failed at {image} on run:{run}") 
            
            sleep(5)
            End_Alteryx.nav_to_image()
            sleep(3)
            Popup_closer2.nav_to_image()
            sleep(2)



# def nav_to_image(self, target_png, speed):
#     position = pt.locateOnScreen(target_png, confidence=0.8)
#     pt.moveTo(position[0] + 10, position[1] + 10, duration=speed)
#     pt.click()

# try:
#     nav_to_image()
# except:
#     print("No second popup found or can't close window")


