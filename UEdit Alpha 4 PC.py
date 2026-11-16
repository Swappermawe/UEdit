# made by swappermawe
# rip brogress
# started 13:01 UTC +8:00 15.11.2026
# finished 9:24 UTC +8:00 16.11.2026
# check out swappermawe.github.io/UEdit

import colorama
from colorama import init
from colorama import Fore, Back, Style
import pathlib
from pathlib import Path
import configparser
import os
import subprocess
import shutil
import json
import pyxdelta
import sys
init()
file_req_u = 0
path_steam = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale"
path_steam_backup = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale"
def modlist(path):
    wp_files = [f.name for f in Path(f"{path}").glob("*.xdelta")]
    return wp_files
def plist(path):
    return [f.name for f in Path(path).iterdir() if f.is_dir()]
def apply_xdelta_patch(source_path, xdelta_path, output_path) -> None:
    temp_out = output_path + ".tmp"
    try:
        pyxdelta.decode(source_path, xdelta_path, temp_out)
        os.replace(temp_out, output_path)
        print(Fore.GREEN + "\nSuccess!\n" + Style.RESET_ALL)
    except Exception as e:
        if os.path.exists(temp_out):
            os.remove(temp_out)
        print(Fore.RED + "\nError! Reason:", e, "\n" + Style.RESET_ALL)

def Main():
    def file0():
        global path_steam
        global file_req_u
        global script_dir
        global config_path
        file0_path = os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file0")
        with open(file0_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        while True:
            ch = input(f"Select line (1-{len(lines)}, 3 symbols)/0 to save & exit: ")[:3]
            try:
                if int(ch) > 0 and int(ch) <= len(lines):
                    ch2 = input("Input value: ")
                    lines[int(ch)-1] = ch2 + "\n"
                    print("\n")
                elif int(ch) == 0:
                    with open(file0_path, "w", encoding="utf-8") as f:
                        f.writelines(lines)
                    print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                    break
                else:
                    print(Fore.YELLOW+f"\n* Line must be between 1 and {len(lines)}!\n"+Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)

    def file9():
        global path_steam
        global file_req_u
        global script_dir
        global config_path
        print(Fore.YELLOW+"file9 is the same as file0! Do you want to copy the file0 over it?"+Style.RESET_ALL)
        a = input("(y/n)> ")[:1].lower()
        try:
            if a == "y":
                    shutil.copy(os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file0", os.environ.get("LOCALAPPDATA") + "\\UNDERTALE\\file9")
                    print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
            elif a == "n":
                    print(Fore.YELLOW+"* Cancelling..."+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
    def u_ini():
        global path_steam
        global file_req_u
        global script_dir
        global config_path
        utconf = configparser.ConfigParser()
        utconf.optionxform = str
        utconf.read(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"))
        while True:
                        ch = input("Select mod:\n   1) Name\n   2) LV\n   3) fun\n   4) Kills\n   5) BC (overall count of items collected)   6) TIME\n   7) Room   8) Back\n> ")
                        try:
                            if int(ch) == 3:
                                new_fun = input("\nNew value (2 symbols): ")[:2]
                                utconf.set("General", "fun", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 1:
                                new_fun = input("\nNew value (6 symbols): ")[:6]
                                utconf.set("General", "Name", f'"{new_fun}"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 2:
                                new_fun = input("\nNew value: ")
                                utconf.set("General", "Love", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 4:
                                new_fun = input("\nNew value: ")
                                utconf.set("General", "Kills", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 5:
                                new_fun = input("\nNew value: ")
                                utconf.set("General", "bc", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 6:
                                new_fun = input("\nNew value: ")
                                utconf.set("General", "Time", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 7:
                                new_fun = input("\nNew value: ")
                                utconf.set("General", "Room", f'"{new_fun}.000000"')
                                with open(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), "w", encoding="utf-8") as f:
                                    utconf.write(f)
                                print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                            if int(ch) == 8:
                                print("\n")
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")
    config_ver = 3
    req_conf = 4
    mod_dir = ""
    profiles_dir = ""
    global path_steam
    global file_req_u
    print("="+Fore.MAGENTA+Back.YELLOW+"  _  _      ____         _    __   _   "+Style.RESET_ALL+"=")
    print(Fore.MAGENTA+Back.YELLOW+"  FJ  L]    F ___J     ___FJ   LJ  FJ_   ")
    print(" J |  | L  J |___:    F __  L     J  _|  ")
    print(" | |  | |  | _____|  | |--| |  FJ | |-'  ")
    print(" F L__J J  F L____:  F L__J J J  LF |__-.")
    print(r"J\______/FJ________LJ\____,__LJ__L\_____/")
    print(" J______F |________| J____,__F|__|J_____F")
    print("                                         ")
    print("           - BY SWAPPERMAWE -            ")
    print(Back.YELLOW+Fore.BLUE+"              Alpha 4 | PC               \n"+Style.RESET_ALL+"="+Fore.MAGENTA+Back.YELLOW+"                                       "+Style.RESET_ALL+"=")
    print("\nTrying to load config.json...")
    try:
        with open(f"{config_path}", "r") as f:
            data = json.load(f)
            path = data.get("path", "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale")
            mod_dir = data.get("mod_dir", "")
            config_ver = int(data.get("config_ver", "3"))
            profiles_dir = data.get("profiles_dir", "")
            path_steam = path
            print(Fore.CYAN+" > Loaded config.json...\n"+ Style.RESET_ALL)
    except Exception as e:
        if isinstance(e,FileNotFoundError) == False:
            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
        else:
            print(Fore.YELLOW+" * config.json not found! Creating a new one..."+ Style.RESET_ALL)
            config_ver = 4
            savedata = {
                "path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale",
                "mod_dir": "",
                "profiles_dir": "",
                "config_ver": "4"
            }
            path = savedata["path"]
            with open(f"{config_path}", "w", encoding="utf-8") as file:
                json.dump(savedata, file, indent=4)
            print(Fore.CYAN+" > Created & loaded config.json...\n"+ Style.RESET_ALL)
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
        print("\n"+Fore.CYAN+" > Found the main Undertale directory...\n"+ Style.RESET_ALL)
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
        print(Fore.YELLOW+" * Seems that the Undertale Steam directory is not found. If you have Undertale installed elsewhere, please input the location (or type 'n' to skip and proceed with saves only)"+ Style.RESET_ALL)
        utloc = input("> ")
        path_steam = utloc
        if os.path.exists(utloc) and utloc != "n":
            savedata = {
                "path": f"{utloc}"
            }
            path = savedata["path"]
            with open(f"{config_path}", "w", encoding="utf-8") as file:
                json.dump(savedata, file, indent=4)
            print(Fore.CYAN+" > Updated config.json...\n"+ Style.RESET_ALL)
                
            print(Fore.CYAN+" > Found the Undertale directory...\n"+ Style.RESET_ALL)
            if os.path.exists(utloc+"\\data.win"):
                print(Fore.CYAN+" > Found data.win...\n"+ Style.RESET_ALL)
                file_req_u += 1
            else:
                print(Fore.RED+" ! data.win not found!"+ Style.RESET_ALL)
            if os.path.exists(utloc+"\\UNDERTALE.exe"):
                print(Fore.CYAN+" > Found the executable...\n"+ Style.RESET_ALL)
                file_req_u += 1
            else:
                print(Fore.RED+" ! UNDERTALE.exe not found!"+ Style.RESET_ALL)
        elif utloc == "n":
            print(Fore.YELLOW+" * Proceeding with saves only.")
        else:
            print(Fore.RED+"Invalid!"+Style.RESET_ALL)
            input("> ")
    if config_ver < req_conf:
        print(Fore.YELLOW+"\n * It appears that your config was saved earlier than this release. To fix this, either:\n  1) Delete config.json\n  OR\n  2) If you have the 'Other' menu available, pick the 'Update Config' option.\n"+Style.RESET_ALL)
    if file_req_u == 3:
        print(Fore.GREEN + '\nUndertale save files found. Using saves only.\n' + Style.RESET_ALL)
        while True:
            i = input("Select file:\n   1) file0\n   2) file9\n   3) undertale.ini\n> ")
            try:
                if int(i) == 2:
                    file9()
                elif int(i) == 1:
                    file0()                        
                elif int(i) == 3:
                    u_ini()
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
                    file9()
                elif int(i) == 1:
                    file0()                        
                elif int(i) == 3:
                    u_ini()
                elif int(i) == 4:
                    while True:
                        ch = input("Select:\n   1) Debug Mode (1.08 exclusive)   2) Undo Debug Mode   3) Launch Game   4) Backup data.win   5) Restore data.win   6) Indication Help...   7) Patch .xdelta Mod...   8) Manage Profiles...   9) Update Config   10) Reset Config   11) Delete steamapi.dll   0) Exit\n> ")
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
                            if int(ch) == 6:
                                print("Indication help:")
                                print("\n")
                                print(Fore.GREEN+"Green: Success\n"+Style.RESET_ALL)
                                print(Fore.YELLOW+" * Yellow: Warning\n"+Style.RESET_ALL)
                                print(Fore.RED+" ! Red: Error\n"+Style.RESET_ALL)
                                print(Fore.CYAN+" > Cyan: Progress\n"+Style.RESET_ALL)
                                print("White: Info/Misc")
                                input("\nPress enter to continue: ")
                                print("\n")
                            if int(ch) == 7:
                                if mod_dir == "":
                                    print(Fore.YELLOW+" * mod_dir in the config is empty by default. Do you want to set up a path?"+Style.RESET_ALL)
                                    chece = input("(y/n)> ")[:1].lower()
                                    if chece == "y":
                                        chece = input("New path? (if doesn't exist, will be created)\n> ")
                                        if os.path.exists(chece):
                                            print(Fore.CYAN+" > Found dir..."+Style.RESET_ALL)
                                            print(Fore.CYAN+"\n > Updating config..."+Style.RESET_ALL)
                                            with open(f"{config_path}", "w") as f:
                                                savedata = {
                                                    "path": f"{path_steam}",
                                                    "mod_dir": f"{chece}",
                                                    "profiles_dir": f"{profiles_dir}",
                                                    "config_ver": f"{config_ver}"
                                                }
                                                json.dump(savedata, f)
                                            mod_dir = chece
                                            print(Fore.CYAN+"\nSuccess!"+Style.RESET_ALL)
                                        else:
                                            os.makedirs(chece)
                                            print(Fore.CYAN+" > Created dir..."+Style.RESET_ALL)
                                            print(Fore.CYAN+"\n > Updating config..."+Style.RESET_ALL)
                                            with open(f"{config_path}", "w") as f:
                                                savedata = {
                                                    "path": f"{path_steam}",
                                                    "mod_dir": f"{chece}",
                                                    "profiles_dir": f"{profiles_dir}",
                                                    "config_ver": f"{config_ver}"
                                                }
                                                json.dump(savedata, f)
                                            mod_dir = chece
                                            print(Fore.CYAN+"\nSuccess! If you want to drop your mods, do it now and press enter to continue..."+Style.RESET_ALL)
                                            input("> ")
                                    else:
                                        print("Cancelling...\n")
                                        return
                                print(Fore.CYAN+" > Loading mods..."+Style.RESET_ALL)
                                files = modlist(mod_dir)
                                while True:
                                    print("\nSelect a mod's index or '0' to quit:")
                                    for idx, f in enumerate(files, start=1):
                                        print(f" {idx}) {f}")

                                    u = input("\n> ").strip()

                                    if u.isdigit() and 1 <= int(u) <= len(files):
                                        selected_mod = files[int(u) - 1]
                                        mod_path = os.path.join(mod_dir, selected_mod)
                                        data_win_path = os.path.join(path_steam, "data.win")

                                        if os.path.exists(mod_path):
                                            print(Fore.CYAN + " > Found the mod!" + Style.RESET_ALL)
                                            print(Fore.CYAN + "\n > Applying the mod..." + Style.RESET_ALL)
                                            apply_xdelta_patch(data_win_path, mod_path, data_win_path)
                                            break
                                        else:
                                            print(Fore.RED+"\nInvalid!\n")
                                    elif u == 0:
                                        break
                            elif int(ch) == 8:
                                if profiles_dir == "":
                                    print(Fore.YELLOW+" * profiles_dir in the config is empty by default. Do you want to set up a path?"+Style.RESET_ALL)
                                    chece = input("(y/n)> ")[:1].lower()
                                    if chece == "y":
                                        chece = input("New path? (if doesn't exist, will be created)\n> ")
                                        if os.path.exists(chece):
                                            print(Fore.CYAN+" > Found dir..."+Style.RESET_ALL)
                                            print(Fore.CYAN+"\n > Updating config..."+Style.RESET_ALL)
                                            with open(f"{config_path}", "w") as f:
                                                savedata = {
                                                    "path": f"{path_steam}",
                                                    "mod_dir": f"{mod_dir}",
                                                    "profiles_dir": f"{chece}",
                                                    "config_ver": f"{config_ver}"
                                                }
                                                json.dump(savedata, f)
                                            profiles_dir = chece
                                            print(Fore.CYAN+"\nSuccess!"+Style.RESET_ALL)
                                        else:
                                            os.makedirs(chece)
                                            print(Fore.CYAN+" > Created dir..."+Style.RESET_ALL)
                                            print(Fore.CYAN+"\n > Updating config..."+Style.RESET_ALL)
                                            with open(f"{config_path}", "w") as f:
                                                savedata = {
                                                    "path": f"{path_steam}",
                                                    "mod_dir": f"{mod_dir}",
                                                    "profiles_dir": f"{chece}",
                                                    "config_ver": f"{config_ver}"
                                                }
                                                json.dump(savedata, f)
                                            profiles_dir = chece
                                            print(Fore.CYAN+"\nSuccess! Press enter to continue..."+Style.RESET_ALL)
                                            input("> ")
                                    else:
                                        print("Cancelling...\n")
                                        return
                                while True:
                                    print("Select:\n   1) Make a new profile\n   2) Load a profile\n   3) Delete a profile\n   4) Update a profile\n   0) Exit")
                                    ch = int(input("> ")[:1])
                                    if ch == 1:
                                        print("Type a profile name:")
                                        name = input("> ")
                                        os.mkdir(profiles_dir+f"\\{name}")
                                        print(Fore.GREEN+"Success! Do you want to copy over your saves?"+Style.RESET_ALL)
                                        cho = input("(y/n)> ")[:1].lower()
                                        if cho == "y":
                                            shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file0"), profiles_dir+f"\\{name}")
                                            print(Fore.CYAN+" > Copied file0..."+Style.RESET_ALL)
                                            shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file9"), profiles_dir+f"\\{name}")
                                            print(Fore.CYAN+" > Copied file9..."+Style.RESET_ALL)
                                            shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), profiles_dir+f"\\{name}")
                                            print(Fore.CYAN+" > Copied undertale.ini..."+Style.RESET_ALL)
                                            print(Fore.GREEN+"\nSuccess!\n"+Style.RESET_ALL)
                                        else:
                                            print("Proceeding without updating...\n")
                                    elif ch == 2:
                                        while True:
                                            print("\nSelect a profile's index or '0' to quit:")
                                            files = plist(profiles_dir)
                                            for idx, f in enumerate(files, start=1):
                                                print(f" {idx}) {f}")

                                            u = input("> ")    
                                            if u.isdigit() and 1 <= int(u) <= len(files):
                                                selected_profile = files[int(u) - 1]
                                                profile_path = os.path.join(profiles_dir, selected_profile)

                                                if os.path.exists(profile_path):
                                                    shutil.copy(os.path.join(profile_path, "file0"), os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file0"))
                                                    print(Fore.CYAN+" > Copied file0..."+Style.RESET_ALL)
                                                    shutil.copy(os.path.join(profile_path, "file9"), os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file9"))
                                                    print(Fore.CYAN+" > Copied file9..."+Style.RESET_ALL)
                                                    shutil.copy(os.path.join(profile_path, "undertale.ini"), os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"))
                                                    print(Fore.CYAN+" > Copied undertale.ini..."+Style.RESET_ALL)
                                                    print(Fore.GREEN+"\nSuccess!\n"+Style.RESET_ALL)
                                                    break
                                                else:
                                                    print(Fore.RED+"\nInvalid!\n")
                                            elif u == "0":
                                                break
                                    elif ch == 3:
                                       while True:
                                            print("\nSelect a profile's index or '0' to quit:")
                                            files = plist(profiles_dir)
                                            for idx, f in enumerate(files, start=1):
                                                print(f" {idx}) {f}")

                                            u = input("> ")    
                                            if u.isdigit() and 1 <= int(u) <= len(files):
                                                selected_profile = files[int(u) - 1]
                                                profile_path = os.path.join(profiles_dir, selected_profile)

                                                if os.path.exists(profile_path):
                                                    shutil.rmtree(profile_path)
                                                else:
                                                    print(Fore.RED+"\nInvalid!\n")
                                            elif u == "0":
                                                break
                                    elif ch == 4:
                                        while True:
                                            print("\nSelect a profile's index or '0' to quit:")
                                            files = plist(profiles_dir)
                                            for idx, f in enumerate(files, start=1):
                                                print(f" {idx}) {f}")

                                            u = input("> ")    
                                            if u.isdigit() and 1 <= int(u) <= len(files):
                                                selected_profile = files[int(u) - 1]
                                                profile_path = os.path.join(profiles_dir, selected_profile)

                                                if os.path.exists(profile_path):
                                                    shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file0"), os.path.join(profile_path, "file0"))
                                                    print(Fore.CYAN+" > Copied file0..."+Style.RESET_ALL)
                                                    shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\file9"), os.path.join(profile_path, "file9"))
                                                    print(Fore.CYAN+" > Copied file9..."+Style.RESET_ALL)
                                                    shutil.copy(os.path.join(os.environ.get("LOCALAPPDATA"), "UNDERTALE\\undertale.ini"), os.path.join(profile_path, "undertale.ini"))
                                                    print(Fore.CYAN+" > Copied undertale.ini..."+Style.RESET_ALL)
                                                    print(Fore.GREEN+"\nSuccess!\n"+Style.RESET_ALL)
                                                    break
                                                else:
                                                    print(Fore.RED+"\nInvalid!\n")

                                            elif u == "0":
                                                break
                                    elif ch == 0:
                                        break

                                    elif u == 0:
                                        break
                                                
                            elif int(ch) == 9:
                                if config_ver < req_conf:
                                    print(f"Detected config v.{config_ver}. Updating...")
                                    with open(f"{config_path}", "w") as f:
                                        savedata = {
                                            "path": f"{path_steam}",
                                            "mod_dir": f"{mod_dir}",
                                            "profiles_dir": f"{profiles_dir}",
                                            "config_ver": f"{config_ver}"
                                        }
                                        json.dump(savedata, f)
                                    config_ver = 4
                                    print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                                else:
                                    print("\nYou don't need to update your config, you silly goose!\n")
                            elif int(ch) == 10:
                                if os.path.exists(config_path):
                                    os.remove(config_path)
                                    print(Fore.GREEN+"\nSuccess! Press enter to restart.\n",Style.RESET_ALL)
                                    input("> ")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    Main()
                                else:
                                    print(Fore.RED+"\n ! config.ini not found!\n",Style.RESET_ALL)
                            elif int(ch) == 11:
                                if os.path.exists(path_steam+"\\steam_api.dll"):
                                    os.remove(path_steam+"\\steam_api.dll")
                                    print(Fore.GREEN+"\nSuccess!\n",Style.RESET_ALL)
                                else:
                                    print(Fore.RED+"\n ! steam_api.dll not found!\n",Style.RESET_ALL)
                            elif int(ch) == 0:
                                print("\n")
                                break
                        except Exception as e:
                            print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)
                
            except Exception as e:
                print(Fore.RED+"\nError! Reason:",e,"\n",Style.RESET_ALL)

try:                
    Main()
except Exception as e:
    print(Fore.RED+"\n ! Error! Reason:",e,"\n",Style.RESET_ALL)
    input("")
