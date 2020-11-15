import ctypes
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pyautogui
import os


url = "https://www.google.com/search?hl=jp&q="
setter = "&btnG=Google+Search&tbs=0&safe=off&tbm=isch"

'''
WERE U WANT TO MAKE THE FOLDER
'''
SAVE_FOLDER = r"C:\Users\Desktop\images"
try:
    os.mkdir(SAVE_FOLDER)
except:
    pass

'''
PUT AMOUNT OF IMAGES HERE V
'''
imgAmount = 24
'''
COOLDOWN BETWEEN EACH PICTURE BEING SHOWN V
'''
cooldown = 28800


'''
DONT TOUCH THE REST C; (unless u know python :P)
'''
imglinks = []
def main():
    download_images()

def download_images():
    data = pyautogui.prompt("What Wallpaper Do You Want Today!")
    print("searching...")
    searchurl = url + data + setter

    response = requests.get(searchurl)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    results = soup.findAll("img", limit=imgAmount + 1)
    print("found " + str(len(results)-1) + " images of " + data)

    results.pop(0)
    for result in results:
        imglinks.append(result["src"])

    for i, imglink in enumerate(imglinks):
        response = requests.get(imglink)

        imagename = SAVE_FOLDER + "\\" + data + str(i+1) + ".jpg"
        with open(imagename, "wb") as file:
            file.write(response.content)

    for i, imglink in enumerate(imglinks):
        print("imageloaded")
        img = SAVE_FOLDER + "\\" + data + str(i+1) + ".jpg"

        new = Image.open(img)
        new = new.resize((1400,  900))
        new.save(img, quality=200000, optimize=True)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)
        time.sleep(cooldown)
        os. remove(img)

if __name__ == "__main__":
    main()
