import subprocess
from urllib.request import urlopen
import banners
import time

app_name = ""


def update_client_version(v):
    with open("version.txt", "r") as vers:
        if vers.read() != v:
            return True
        else:
            return False


def main():
    try:
        version = urlopen("..../your_app/version.txt").read()

    except Exception:
        print("[!] Unable to Fetch Origin version.txt     [!]")
        print("[!] Please Check Your Internet Connection! [!]")
        print("[*] Exiting ...                            [*]")
        quit()

    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[+] Updated to latest version: v{}..".format(version)

    else:
        return "[*] You are already up to date [*]"


if __name__ == '__main__':
    print(f"[*] Welcome to {app_name} Auto Updater")
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print("[*] Please Note : Git must be installed in order to use \"updater.py\"")
    time.sleep(5)
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"[*] Checking {app_name} version information..    [*]")
    print(main())
    print("[*] Exiting ... [*]")
