import pyautogui
import time

def openVS():
    pyautogui.hotkey('win')
    time.sleep(10)
    pyautogui.write('vs')
    time.sleep(10)
    pyautogui.hotkey('enter')
    time.sleep(10)

def openExtensionWindow():
    pyautogui.hotkey('ctrl'+'shift'+'x')
    time.sleep(10)

def installCppExtension(ExtensionName):
    pyautogui.write(ExtensionName)
    time.sleep(10)
    pyautogui.click(x=399,y=252)
    time.sleep(10)
    pyautogui.doubleClick(x=233,y=159)
    time.sleep(10)
    pyautogui.press('backspace')
    time.sleep(10)


openVS()
openExtensionWindow()

Extentions = ('clangd','c++ testmate','c++ helper')
for Extention in Extentions:
    installCppExtension(Extention)

pyautogui.hotkey('ctrl','w')