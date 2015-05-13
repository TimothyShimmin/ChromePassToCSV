__author__ = 'Tim Shimmin'
import os
from os.path import expanduser
import sqlite3
import win32crypt
import time

# ##### MAIN #####
# Find Chrome's password file, "Login Data".
# Determines Windows User name with expanduser()
## Assumes Windows 7, default installation directory.
home = os.path.join(expanduser("~"), "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
print(home)


# TODO: Require user to exit from Chrome.exe before use -> http://stackoverflow.com/a/10457565
# TODO: Check if running before and after this. Before, then pose question; After, then wait some seconds?
# Before accessing Chrome file while in use, exit from all instances of Chrome.exe
# print("Would you like me to force close Chrome? Yes/No")
# answer = input()
# if answer == "Yes" or answer == "yes":
os.system("taskkill /f /im chrome.exe >nul")
    # else:
    #     throw exception


# Opens writable file to save passwords to. Labeled with date and timestamp.
## Saving with extension .csv is readable by OpenOffice4
txtFile = open('Chrome Passwords ' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.csv', 'w')

try:
    # Opens sqlite3 interface. Create connection to "Login Data" sqlite3 database.
    conn = sqlite3.connect(home)
    cursor = conn.cursor()      # Used to traverse records from the result set

    # Execution of SQL statement. Selects website, username, and password values from Chrome's pwd file
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')

    # For each row of values, write decrypted row to txtFile
    for result in cursor.fetchall():
        try:
            # Removes Windows encryption on password_value for current user.
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        except:
            print(result + "Decrypt Failed")
        # Writes row with values separated by commas. Row separated with \n.
        # Decodes password from binary (bytes) string to utf-8.
        txtFile.write(result[0] + "," + result[1] + "," + password.decode('utf-8') + "\n")
except:
    conn.close()
    txtFile.close()
    # cursor.close()        # Closes with conn.close()
    # csvFile.close()


# TODO: Make it *this* readable.
# ORIGINAL EXAMPLE PROGRAM
#
# conn = sqlite3.connect('example.db')
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

