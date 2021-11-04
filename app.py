import cv2
import pyautogui
import webbrowser
from time import sleep
from PIL import ImageGrab
import pytesseract
import numpy as nm
import keyboard
import os
import psutil
from screeninfo import get_monitors


method = cv2.TM_SQDIFF_NORMED


axe_mine_pressed = 1
plant_water_pressed = 1


for m in get_monitors():
    m_height = str(m.height)



def check_timer():
    timer = cv2.imread('timer.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,timer,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location
    box = (X,Y,(X+200),(Y+60))
    image = ImageGrab.grab(bbox=box)
    # cv2.imshow('window',nm.array(image))
    # cv2.waitKey(0)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "")
    return ocr

def goto_farming():
    global m_height
    if m_height == "1080":
        btnn = "map_btn_1080.png"
    elif m_height == "768":
        btnn = "map_btn_720.png"
    map = cv2.imread(btnn)
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,map,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+30),(Y+15))

    sleep(5)

    farming_area = cv2.imread('farming_area_btn.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,farming_area,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+50),(Y+50))

    pyautogui.moveTo(60,150)


def goto_mining():
    global m_height
    if m_height == "1080":
        btnn = "map_btn_1080.png"
    elif m_height == "768":
        btnn = "map_btn_720.png"
    map = cv2.imread(btnn)
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,map,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+30),(Y+15))
    # pyautogui.moveTo((X+30),(Y+15))

    sleep(5)

    mining_area = cv2.imread('mining_area_btn.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    match_loc = cv2.matchTemplate(screen,mining_area,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+50),(Y+50))

    pyautogui.moveTo(60,150)

def farm_crop():
    global plant_water_pressed
    os.system("cls")
    print("Starting Farming")
    goto_farming()
    sleep(2)
    i = 0
    while True:
        timer = check_timer()
        if timer == "00:00:00":
            print("Watering Plants")
            print("Water: {}".format(plant_water_pressed))
            plant_water_pressed += 1
            if plant_water_pressed > 6:
                start_axe_mine()
                break
            sleep(3)
            water_btn = cv2.imread('water_btn.png')
            screen = pyautogui.screenshot("screen.png")
            screen = cv2.imread('screen.png')
            os.remove('screen.png')
            match_loc = cv2.matchTemplate(screen,water_btn,method)
            mn,_,location,_ = cv2.minMaxLoc(match_loc)
            X,Y = location

            pyautogui.click((X+30),(Y+10))

            sleep(15)

            home_btn = cv2.imread('home_btn.png')
            screen = pyautogui.screenshot("screen.png")
            screen = cv2.imread('screen.png')
            os.remove('screen.png')
            match_loc = cv2.matchTemplate(screen,home_btn,method)
            mn,_,location,_ = cv2.minMaxLoc(match_loc)
            X,Y = location

            pyautogui.click((X+5),(Y+5))

            sleep(5)
            start_axe_mine()
            break
        else:
            i = i + 1
            if i == 500:
                start_axe_mine()
                break

def start_axe_mine():
    global axe_mine_pressed
    os.system("cls")
    print("Starting Axe Mining")
    goto_mining()
    sleep(5)
    i = 0
    while True:
        timer = check_timer()
        if timer == "00:00:00":
            print("Cut Woods")
            print("Cut: {}".format(axe_mine_pressed))
            axe_mine_pressed += 1
            if axe_mine_pressed > 24:
                os.system('taskkill /f /im firefox.exe')
                psutil.Process(os.getpid()).terminate()
            sleep(3)
            mine_btn = cv2.imread('mine_btn.png')
            screen = pyautogui.screenshot("screen.png")
            screen = cv2.imread('screen.png')
            os.remove('screen.png')
            match_loc = cv2.matchTemplate(screen,mine_btn,method)
            mn,_,location,_ = cv2.minMaxLoc(match_loc)
            X,Y = location

            pyautogui.click((X+30),(Y+10))

            sleep(15)

            home_btn = cv2.imread('home_btn.png')
            screen = pyautogui.screenshot("screen.png")
            screen = cv2.imread('screen.png')
            os.remove('screen.png')
            match_loc = cv2.matchTemplate(screen,home_btn,method)
            mn,_,location,_ = cv2.minMaxLoc(match_loc)
            X,Y = location

            pyautogui.click((X+5),(Y+5))

            sleep(10)

            farm_crop()

            break
        else:
            i = i + 1
            if i == 500:

                farm_crop()

                break


def login():
    print("Logging In Game")

    login_btn = cv2.imread('login_btn.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,login_btn,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+10),(Y+5))

    sleep(15)

    wax_btn = cv2.imread('wax_btn_bl.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,wax_btn,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+20),(Y+20))

    sleep(2)

    wax_btn = cv2.imread('wax_btn.png')
    screen = pyautogui.screenshot("screen.png")
    screen = cv2.imread('screen.png')
    os.remove('screen.png')
    match_loc = cv2.matchTemplate(screen,wax_btn,method)
    mn,_,location,_ = cv2.minMaxLoc(match_loc)
    X,Y = location

    pyautogui.click((X+20),(Y+20))

    sleep(15)

    start_axe_mine()

def browse_to_game():
    print("Opening Game")
    try:
        webbrowser.open_new("https://play.farmersworld.io")
        sleep(15)
        login()
    except Exception as e:
        print(e)


def close_All():
    os.system('taskkill /f /im firefox.exe')
    psutil.Process(os.getpid()).terminate()

keyboard.add_hotkey("ctrl+q",close_All)


if __name__ == "__main__":
    browse_to_game()
    # goto_mining()