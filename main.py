import pyautogui as pt
import glob
from pyautogui import ImageNotFoundException
from time import sleep

def click_everything(target_png, speed, x_offset, y_offset, click_function):
    position = pt.locateOnScreen(target_png, confidence=0.9)
    pt.moveTo(position[0] + x_offset, position[1] + y_offset, duration=speed)
    click_function()

if __name__ == "__main__":
    pt.FAILSAFE = True
    sleep(2)
    images = glob.glob('images\Alteryx_pipelines/*.PNG')
    end = 0 

    while True:
        try:
            click_everything('images/Close_python.PNG', .001, 15, 15, pt.doubleClick)
        except ImageNotFoundException:
            print("Can't close IDE")
            break
        
        try:
            click_everything('images\Folder.PNG', .001, 30, 30, pt.doubleClick)
        except ImageNotFoundException:
            print("Can't find or open folder")
            break
        
        for image in images: 
            print(image)
            click_everything(image, .001, 10, 10, pt.doubleClick)
            sleep(20)
            click_everything('images\close_popup.PNG', .001, 15, 10, pt.doubleClick)
            sleep(1)
            click_everything('images\Run_button.PNG', .001, 15, 15, pt.doubleClick)
            sleep(1)

            for run in range(3600): 
                try:
                    click_everything('images\Done_button.PNG', .001, 15, 10, pt.doubleClick)
                    break
                except ImageNotFoundException:
                    print(f"Run failed at {image} on run:{run}")
                sleep(1)
                
            try:
                click_everything('images\Close_alteryx.PNG', .001, 15, 15, pt.click)
            except ImageNotFoundException:
                print("Can't find or open folder")
                break
            
            sleep(3)

            try:
                click_everything('images\Alteryx_pop_up.PNG', .001, 15, 15, pt.click)
            except ImageNotFoundException:
                print(f"Can't find or click Alteryx_popup.PNG")