"""
WI-Fi Show Passwords

Made by : Mohammad boorboor
Email : m.boorboor315@gmail.com
github : github.com/mohammadbourbour

"""

# Refrence

import subprocess
from termcolor import colored
import pyfiglet


def show_wifi_passwords():
    # My information
    email = "m.boorboor315@gmail.com"
    name = "Mohammad boorboor"

    # program information
    description = "This program displays saved Wi-Fi networks and their passwords."
    Banner = "Wi-Fi Show"

    # print program information
    print(colored(pyfiglet.figlet_format(Banner), color="green"))
    print(colored(description, color="green") + "\n")
    print(f"Made By : {name} \nEmail : {email}\n")

    # prompt user to proceed
    input("Press Enter to continue...\n\n")

    # get list of saved Wi-Fi profiles
    try:
        data = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError as e:
        print("An error occurred: ", e)
        return

    profiles = [i.split(":", 1)[1].strip() for i in data if "All User Profile" in i]

    # get Wi-Fi passwords for each profile
    ssid_passwords = {}
    for profile in profiles:
        try:
            results = (
                subprocess
                .check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
                .decode("utf-8")
                .split("\n")
            )
        except subprocess.CalledProcessError as e:
            print("An error occurred: ", e)
            continue

        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            ssid_passwords[profile] = results[0]
        except IndexError:
            ssid_passwords[profile] = ""

    # print results in a cool hacker style
    print("\033[1;32m{:<30}|\033[1;31m  {:<}\033[0m".format("SSID", "Password"))
    print("\033[1;36m" + "-" * 45 + "\033[0m")
    for ssid, password in ssid_passwords.items():
        print("\033[1;32m{:<30}|\033[1;31m  {:<}\033[0m".format(ssid, password))

    # prompt user to exit in a mysterious way
    print("\n\033[1;36mHIT ENTER TO EXIT LIKE A HACKER...\033[0m")




if __name__ == '__main__':
    show_wifi_passwords()
    input()
