__author__ = 'Tim Shimmin'
from os import getenv
import os
from os.path import expanduser
import sqlite3
import win32crypt
import csv
import time
import winshell



# ## Example script functions
# Create table
# def createTestTable():
#     c.execute('DROP TABLE if exists stocks')
#     c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#
#     # Insert a row of data
#     c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
#     # Save (commit) the changes
#     conn.commit()
#
#
# # Read table
# def readDb():
#     c.execute('SELECT * FROM stocks WHERE qty=100')
#     print(c.fetchone())
# ## End Example script functions


# ##### MAIN #####
# ### modifications

# expanduser attempt
print()
home = expanduser("~")
# print(home)
home = os.path.join(home, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
print(home)
print()
# ### end expanduser attempt


# getenv attempt
# print('------')
# chromeDir = os.path.join(os.getenv('APPDATA').rstrip("Roaming"), "Local\\Google\\Chrome\\User Data\\Default\\Login Data")
# print(os.path.join(os.getenv('APPDATA').rstrip("Roaming"), "Local\\Google\\Chrome\\User Data\\Default\\Login Data"))
# print('------')
# # chromeDir = os.getenv('APPDATA').rstrip("Roaming")
# # print(os.path.normpath(chromeDir))
# # os.listdir(chromeDir)
# # print(os.path.isfile(chromeDir)) # true
# # print(os.path.realpath(chromeDir))
# # chromeDir = os.path.realpath(chromeDir)
# # print(chromeDir)

# ### end getenv attempt

# winshell attempt
# print(winshell.application_data())
# attempt = winshell.application_data()
# print(winshell.)
# ### end winshell attempt


# chromePass = open('C:\\Users\\Kat\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data')
# chromePass = open('C:\\Users\\Kat\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data')
# conn1 = sqlite3.connect(win32api.GetEnvironmentVariable("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
# oldTODO: path is found (expanduser attempt working), but cannot access because it //is a hidden file?// WAS CURRENTLY IN USE, BECAUSE CHROME.EXE WAS OPEN. -->prev iteration:*** not helpful for any other computer. Assumes 1. Windows machine and 2. User name of "Kat"; perhaps "%LOCALAPPDATA%\Google\Chrome\User Data\Default\"
# TODO: Require user to exit from Chrome.exe before use -> http://stackoverflow.com/a/10457565


conn1 = sqlite3.connect(home)  # for expanduser attempt

# conn1 = sqlite3.connect(chromeDir) # for getenv attempt

# conn1 = sqlite3.connect(getenv("APPDATA") + "\\..\\Google\\Chrome\\User Data\\Default\\Login Data")
# conn1 = sqlite3.connect("C:\\Users\\Kat\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
cursor = conn1.cursor()

# csv attempt
# csvFile = open('Chrome Passwords' + time.strftime("%d-%m-%Y_%H-%M-%S") + '.csv', 'w', newline='')  # , encoding='utf-8')
# fileWriter = csv.writer(csvFile)  # , dialect=csv.excel  # TODO: delimiter or lineterminator? http://automatetheboringstuff.com/chapter14/
# ## end csv attempt

txtFile = open('Chrome Passwords' + time.strftime("%d-%m-%Y_%H-%M-%S") + '.csv', 'w')
# fileWriter =



# Before accessing Chrome file while in use, exit from all instances of Chrome.exe
# print("Would you like me to force close Chrome? Yes/No") # TODO: Check if running before and after this. Before, then pose question; After, then wait some seconds?
# answer = input()
# if answer == "Yes" or answer == "yes":
os.system("taskkill /f /im chrome.exe >nul")
    # else:
    #     throw exception

try:
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    for result in cursor.fetchall():
        try:
            password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
        except:
            print(result + "Decrypt Failed")

        # TODO: Instead of print to console, save to CSV file. Perhaps in order (once) required by Firefox.
        # print('Site: ' + result[0])
        # print('Username: ' + result[1])
        # print("Password: " + password.decode('utf-8'))
        # fileWriter.writeRow([result[0], result[1]])  # , password.decode('utf-8') # csv attempt
        txtFile.write(result[0] + "," + result[1] + "," + password.decode('utf-8') + "\n")      #  password.decode('utf-8'),
    # print(cursor.fetchone())
except:
    cursor.close()
    conn1.close()
    # csvFile.close()
    txtFile.close()
# cursor.close()
# conn1.close()

# print(chromePass.read())
# ############# end mods




# ORIGINAL EXAMPLE PROGRAM
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
#
# # Create test table
# createTestTable()
#
#
# # Test current db
# readDb()
#
#
#
# # Close connection
# conn.close()

print("Ran fine!")
# input()

