# made by swappermawe
# rip brogress
# started 22:31 UTC +8:00 06.11.2026

import colorama
from colorama import init
from colorama import Fore, Back, Style
import pathlib
import configparser
import os
import subprocess
import shutil
init()
file_req_u = 0
path_steam = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale"
path_steam_backup = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale"
def Main():
    global path_steam
    global file_req_u
    print(Fore.MAGENTA+Back.YELLOW+"   _  _      ____         _    __   _    ")
    print("  FJ  L]    F ___J     ___FJ   LJ  FJ_   ")
    print(" J |  | L  J |___:    F __  L     J  _|  ")
    print(" | |  | |  | _____|  | |--| |  FJ | |-'  ")
    print(" F L__J J  F L____:  F L__J J J  LF |__-.")
    print("J\______/FJ________LJ\____,__LJ__L\_____/")
    print(" J______F |________| J____,__F|__|J_____F")
    print("                                         ")
    print("         - BY SWAPPERMAWE -              ")
    print(Fore.BLUE+"            Alpha 3 | PC                 "+Style.RESET_ALL)
    print("\nSearching for save files...")
    print("\nSearching for Undertale files...\n")
    if os.path.exists(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE")):
                      print(Fore.CYAN+" > Found the Undertale save directory...\n"+ Style.RESET_ALL)
                      if os.path.exists(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file0")):
                          print(Fore.CYAN+" > Found file0..."+ Style.RESET_ALL)
                          file_req_u += 1
                      else:
                          print(Fore.RED+" ! file0 not found!"+ Style.RESET_ALL)   
                      if os.path.exists(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file9")):
                          print(Fore.CYAN+" > Found file9..."+ Style.RESET_ALL)
                          file_req_u += 1
                      else:
                          print(Fore.RED+" ! file9 not found!"+ Style.RESET_ALL)
                      if os.path.exists(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\undertale.ini")):
                          print(Fore.CYAN+" > Found undertale.ini..."+ Style.RESET_ALL)
                          file_req_u += 1
                      else:
                          print(Fore.RED+" ! undertale.ini not found!"+ Style.RESET_ALL)
    else:
        print(Fore.RED+" ! Undertale directory is missing!"+ Style.RESET_ALL)
    if os.path.exists(path_steam):
        print("\n"+Fore.CYAN+" > Found the Undertale Steam directory...\n"+ Style.RESET_ALL)
        if os.path.exists(path_steam+"\\data.win"):
            print(Fore.CYAN+" > Found data.win..."+ Style.RESET_ALL)
            file_req_u += 1
        else:
            print(Fore.RED+" ! data.win not found!"+ Style.RESET_ALL)
        if os.path.exists(path_steam+"\\UNDERTALE.exe"):
            print(Fore.CYAN+" > Found the executable...\n"+ Style.RESET_ALL)
            file_req_u += 1
        else:
            print(Fore.RED+" ! UNDERTALE.exe not found!"+ Style.RESET_ALL)  
    else:
        print(Fore.YELLOW+" * Seems that the Undertale Steam directory is not found. If you have Undertale installed elsewhere, please input the location (or type 'n' to skip and proceed with saves only) with double dashes (e.g. 'C:\\Undertale')"+ Style.RESET_ALL)
        utloc = input("> ")
        path_steam = utloc
        if os.path.exists(utloc) and utloc != "n":
            print(Fore.CYAN+" > Found the Undertale directory...\n"+ Style.RESET_ALL)
            if os.path.exists(utloc+"\\data.win"):
                print(Fore.CYAN+" > Found data.win...\n"+ Style.RESET_ALL)
            else:
                print(Fore.RED+" ! data.win not found!"+ Style.RESET_ALL)
            if os.path.exists(utloc+"\\UNDERTALE.exe"):
                print(Fore.CYAN+" > Found the executable...\n"+ Style.RESET_ALL)
            else:
                print(Fore.RED+" ! UNDERTALE.exe not found!"+ Style.RESET_ALL)
        elif utloc == "n":
            print(Fore.YELLOW+" * Proceeding with saves only.")
        else:
            print(Fore.RED+"Invalid!"+Style.RESET_ALL)
            input("")
    if file_req_u == 3:
        print(Fore.GREEN + '\nUndertale save files found. Using saves only.\n' + Style.RESET_ALL)
        while True:
            i = input("Select file:\n   1) file0\n   2) file9\n   3) undertale.ini\n> ")
            try:
                if int(i) == 2:
                    print(Fore.YELLOW+"file9 is the same as file0! Do you want to copy the file0 over it?"+Style.RESET_ALL)
                    a = input("(y/n)> ")[:1]
                    try:
                        if a == "y":
                            shutil.copy(os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file0", os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file9")
                            print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                        elif a == "n":
                            print(Fore.YELLOW+"* Cancelling...")
                    except Exception as e:
                        print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                elif int(i) == 1:
                    with open(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file0"), "r", encoding="utf-8") as f:
                            lines = f.readlines()
                    while True:
                        ch = input("Select flag (1-549, 3 symbols)/0 to save & exit: ")[:3]
                        try:
                            if int(ch) > 0 and int(ch) < 550:
                                ch2 = input("Input value: ")
                                lines[int(ch)-1] = ch2 + "\n"
                                print("\n")
                            elif int(ch) == 0:
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file0"), "w", encoding="utf-8") as f:
                                    f.writelines(lines)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                        
                elif int(i) == 3:
                    utconf = configparser.ConfigParser()
                    utconf.optionxform = str
                    utconf.read(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"))
                    while True:
                        ch = input("Select mod:\n   1) Name\n   2) LV\n   3) fun\n   4) Kills\n   5) BC (overall count of items collected)   6) TIME\n   7) Room   8) Back\n> ")
                        try:
                            if int(ch) == 3:
                                try:
                                    new_fun = input("\nNew value (2 symbols): ")[:2]
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "fun", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 1:
                                try:
                                    new_fun = input("\nNew value (6 symbols): ")[:6]
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Name", f'"{new_fun}"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 2:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Love", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 4:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Kills", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 5:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "bc", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 6:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Time", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 7:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Room", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 8:
                                print("\n")
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
    elif file_req_u > 0 and file_req_u < 4:
        print(Fore.YELLOW + "\nUndertale save files partially found.\nPlease check your save directory.\n" + Style.RESET_ALL)
        input("Press enter to continue: ")
    elif file_req_u == 0:
        print(Fore.RED + "\nNo Undertale files found.\nPlease check your save directory.\n" + Style.RESET_ALL)
        input("Press enter to continue: ")
    elif file_req_u > 3:
        print(Fore.GREEN + '\nUndertale files found.\n' + Style.RESET_ALL)
        while True:
            i = input("Select file:\n   1) file0\n   2) file9\n   3) undertale.ini   4) Other...\n> ")
            try:
                if int(i) == 2:
                    print(Fore.YELLOW+"file9 is the same as file0! Do you want to copy the file0 over it?"+Style.RESET_ALL)
                    a = input("(y/n)> ")[:1]
                    try:
                        if a == "y":
                            shutil.copy(os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file0", os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file9")
                            print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                        elif a == "n":
                            print(Fore.YELLOW+"* Cancelling...")
                    except Exception as e:
                        print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                elif int(i) == 1:
                    with open(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file0"), "r", encoding="utf-8") as f:
                            lines = f.readlines()
                    while True:
                        ch = input("Select flag (1-549, 3 symbols)/0 to save & exit: ")[:3]
                        try:
                            if int(ch) > 0 and int(ch) < 550:
                                ch2 = input("Input value: ")
                                lines[int(ch)-1] = ch2 + "\n"
                                print("\n")
                            elif int(ch) == 0:
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE\\file0"), "w", encoding="utf-8") as f:
                                    f.writelines(lines)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                elif int(i) == 4:
                    while True:
                        ch = input("Select:\n   1) Debug Mode (1.08 exclusive)   2) Undo Debug Mode   3) Launch Game   4) Backup data.win   5) Restore data.win   6) Exit\n> ")
                        try:
                            if int(ch) == 1:
                                with open(path_steam+"\\data.win", "rb") as f:
                                    file_data = bytearray(f.read())

                                file_data[0x7748C4] = 0x01

                                with open(path_steam+"\\data.win", "wb") as f:
                                    f.write(file_data)

                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 2:
                                with open(path_steam+"\\data.win", "rb") as f:
                                    file_data = bytearray(f.read())

                                file_data[0x7748C4] = 0x00

                                with open(path_steam+"\\data.win", "wb") as f:
                                    f.write(file_data)

                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 3:
                                subprocess.run([path_steam+"\\UNDERTALE.exe"])
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 4:
                                shutil.copy(path_steam+"\\data.win", path_steam+"\\backup.win")
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 5:
                                if os.path.exists(path_steam+"\\backup.win"):
                                    shutil.copy(path_steam+"\\backup.win", path_steam+"\\data.win")
                                    print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                                else:
                                    print(Fore.YELLOW+"\n* Create a backup first!\n",Style.RESET_ALL)
                            elif int(ch) == 6:
                                print("\n")
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                elif int(i) == 3:
                    utconf = configparser.ConfigParser()
                    utconf.optionxform = str
                    utconf.read(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"))
                    while True:
                        ch = input("Select mod:\n   1) Name\n   2) LV\n   3) fun\n   4) Kills\n   5) BC (overall count of items collected)   6) TIME\n   7) Room   8) Back\n> ")
                        try:
                            if int(ch) == 3:
                                try:
                                    new_fun = input("\nNew value (2 symbols): ")[:2]
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "fun", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 1:
                                try:
                                    new_fun = input("\nNew value (6 symbols): ")[:6]
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Name", f'"{new_fun}"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 2:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Love", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 4:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Kills", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 5:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "bc", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 6:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Time", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 7:
                                try:
                                    new_fun = input("\nNew value: ")
                                except Exception as e:
                                    print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                                utconf.set("General", "Room", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 8:
                                print("\n")
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
Main()
