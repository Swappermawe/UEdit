# made by swappermawe
# rip brogress

import colorama
from colorama import init
from colorama import Fore, Back, Style
import pathlib
import json
import configparser
import os
import time
init()
file_req_u = 0
def Main():
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
    print(Fore.BLUE+"            Alpha 1 | PC                 "+Style.RESET_ALL)
    print("\nSearching for save files...")
    print("\nSearching for Undertale files...\n")
    if os.path.exists(os.path.join(os.environ.get("LOCALAPPDATA"),"UNDERTALE")):
                      print(Fore.CYAN+" > Found the Undertale directory...\n"+ Style.RESET_ALL)
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
    if file_req_u == 3:
        print(Fore.GREEN + '\nUndertale files found.\n' + Style.RESET_ALL)
        while True:
            i = input("Select file:\n   1) file0\n   2) file9\n   3) undertale.ini\n> ")
            try:
                if int(i) == 1:
                    print(Fore.YELLOW+"\nWIP...\n"+Style.RESET_ALL)
                elif int(i) == 2:
                    print(Fore.YELLOW+"\nWIP...\n"+Style.RESET_ALL)
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
        print(Fore.YELLOW + "\nUndertale files partially found.\nPlease check your save directory.\n" + Style.RESET_ALL)
        input("Press enter to continue: ")
    elif file_req_u == 0:
        print(Fore.RED + "\nNo Undertale files found.\nPlease check your save directory.\n" + Style.RESET_ALL)
        input("Press enter to continue: ")
Main()
