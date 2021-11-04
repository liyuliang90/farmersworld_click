import os
from pynput.mouse import Controller
import pyautogui
from time import sleep as sl
import keyboard
import webbrowser
import cv2
from numpy.lib.type_check import imag
import pytesseract
from PIL import Image, ImageGrab
from PIL import ImageOps
import numpy as nm
import pydirectinput
import psutil


open_area = (253, 266)
tab_one = (114, 20)
tab_two = (346, 23)
home_btn = (653, 838)
fwg_box = (869, 541)
fww_box = (1023, 540)
fwf_box = (1171, 543)
deposit_area = (1030, 429)
withdrawl_area = (882, 427)
withdrawl_btn = (965, 704)
wood_exchange_box = (1017, 564)
crypto_exchange_btn = (977, 834)
energy_exchange_btn = (966,615)
energy_amt_box_pos = (1001,539)
add_energy_btn = (1509,269)
plant_area = (771,670)
mining_area = (781,438)
map_btn = (1084,839)
repair_btn = (1164, 697)
use_objects_btn = (1020, 696)
wax_wallet_btn = (963, 530)
login_btn = [960,916]



def login():
    print("Logging in To Account")
    pydirectinput.moveTo(login_btn[0],login_btn[1])
    pydirectinput.click()
    sl(2)
    pydirectinput.moveTo(wax_wallet_btn[0],wax_wallet_btn[1])
    pydirectinput.click()
    sl(20)
    mine_axe()


def mine_axe():
    print("Starting Axe Mining")
    goto_mining()
    sl(2)
    i = 0
    while True:
        timer = check_timer()
        if timer == "00:00:00":
            sl(3)
            pyautogui.click(use_objects_btn)
            sl(15)
            pyautogui.click(open_area)
            sl(10)
            farm_crop()
            break
        else:
            i = i + 1
            if i == 500:
                farm_crop()
                break
                

def farm_crop():
    # print("Starting Crop Farming")
    # goto_farming()
    # sl(2)
    # i = 0
    # while True:
    #     timer = check_timer()
    #     if timer == "00:00:00":
    #         sl(3)
    #         pyautogui.click(use_objects_btn)
    #         sl(15)
    #         pyautogui.click(open_area)
    #         sl(5)
    #         mine_axe()
    #         break
    #     else:
    #         i = i + 1
    #         if i == 500:
    #             mine_axe()
    #             break
    mine_axe()


def goto_mining():
    pyautogui.click(open_area)
    sl(1)
    pyautogui.click(map_btn)
    sl(1)
    pyautogui.click(mining_area)

def goto_farming():
    pyautogui.click(open_area)
    sl(1)
    pyautogui.click(map_btn)
    sl(1)
    pyautogui.click(plant_area)

def check_timer():
    box = (1001,618,1189,674)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    return ocr



def on_press():
    os.system('taskkill /f /im firefox.exe')
    psutil.Process(os.getpid()).terminate()

keyboard.add_hotkey("ctrl+q",on_press)

def open_game():
    print("Starting Browser")
    try:
        print("Opening Game")
        webbrowser.open_new("https://play.farmersworld.io")
        sl(15)
        login()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    open_game()