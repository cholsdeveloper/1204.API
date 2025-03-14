
import requests as rq
import json as js
from os import remove as x
from sys import argv
import re as rx
import datetime as dt
import random as rd
import base64 as b64
from threading import Thread as Th
from concurrent.futures import ThreadPoolExecutor as sux
reset = "\033[0m"
purple = "\033[1;35m"
yellow = "\033[93m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
red = "\033[1;31m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"

# ✅ API Class (Merged)
class API:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://top1phsmm.com/adminapi/v1"
        self.headers = {'Content-Type': 'application/json', 'X-Api-Key': self.api_key}

    def complete_order(self, order_id):
        """ Mark order as cancelled """
        data = {"key": self.api_key, "action": "setCancelled", "id": order_id}
        try:
            response = rq.post(self.base_url, data=data)
            return response.json().get('status', None)
        except Exception as e:
            print("Error Cancelled Order:", e)
            return None
        
    def complete_order(self, order_id):
        """ Mark order as completed """
        data = {"key": self.api_key, "action": "setCompleted", "id": order_id}
        try:
            response = rq.post(self.base_url, data=data)
            return response.json().get('status', None)
        except Exception as e:
            print("Error Completing Order:", e)
            return None

    def get_order(self, order_type='1204'):
        """ Fetch order details """
        data = {"key": self.api_key, "action": "getOrder", "type": order_type}
        try:
            response = rq.post(self.base_url, data=data)
            result = response.json()
            return result if result.get("status") == "success" else None
        except Exception:
            return None

# ✅ Facebook Helper Class (Merged)
class FacebookHelper:
    def __init__(self):
        self.headers_web = {'User-Agent': 'Mozilla/5.0'}

    def extract_post_id(self, url):
        """ Extract Facebook Post ID """
        try:
            page_content = rq.get(url, headers=self.headers_web).text
            post_id = rx.search('"post_id":"(.*?)"', str(page_content))
            if post_id:
                return post_id.group(1)
            else:
                fallback_id = rx.search('story_fbid=(.*?)&', str(page_content))
                return fallback_id.group(1) if fallback_id else None
        except Exception:
            return None

import random

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.choice(["8.1", "10", "11"])  # More realistic Windows versions
    is_win64 = random.choice([True, False])

    win64_text = "Win64; x64" if is_win64 else "WOW64"

    user_agent = (
        f"Mozilla/5.0 (Windows NT {windows_version}; {win64_text}) "
        f"AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) "
        f"Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0"
    )

    return user_agent
        
# ✅ Load Facebook Tokens
try:
    with open('/sdcard/boostphere/RPWPAGES.txt', 'r', encoding='utf-8') as file:
        fb_tokens = file.read().splitlines()
except FileNotFoundError:
    print("⛔ Token File Not Found!")
    exit()

print(f'✅ Loaded {len(fb_tokens)} Facebook Tokens')

# ✅ Initialization
api_key = '461hsa3qp6yf9q2g1s2qgiii3jf20r584qnpk5fs4psnjlxel53p8kmu0omhbbln'  # 🔥 Replace with actual API key
api = API(api_key)
fb_helper = FacebookHelper()
completed_orders =0
active_threads = []


import os

TEXT_FILE = "/sdcard/cholo/completed_order.txt"  # Change path if needed

def save_order_to_txt(order_id, quantity, completed_orders, elapsed_time):
    """ Save Order ID, Quantity, Completion Message, and Time Taken to a text file. """
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    message = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 Order ID: {order_id}\n"
        f"📦 Quantity: {quantity}\n"
        f"✅ Order ID {order_id} Completed : Delivered {completed_orders} out of {quantity}\n"
        f"⏳ Time Taken: {int(hours)}h {int(minutes)}m {int(seconds)}s\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    )

    try:
        with open(TEXT_FILE, "a", encoding="utf-8") as file:  # Append mode
            file.write(message)
            file.flush()  # Ensure data is written
        print(f"✅ Order {order_id} saved in {TEXT_FILE}")
    except Exception as e:
        print(f"⚠️ Error writing to file: {e}")

# ✅ Facebook Post Function
def share_facebook_post(token, post_url, order_id, quantity):
    global completed_orders
    """ Share Post on Facebook """
    fb_url = 'https://graph.facebook.com/v13.0/me/feed'
    data = {
        'link': post_url,
        'published': '0',
        'privacy': '{"value":"SELF"}',
        'access_token': token
    }
    headers_ = {
        'User-Agent': W_ueragnt()  # Assuming W_ueragnt() function provides user agents
    }
    try:
        # if completed_orders < quantity:
            response = rq.post(fb_url, data=data).json()
            if 'id' in response:
                completed_orders += 1
                print(f"✅ Successfull shares({red}{completed_orders}{reset}/{white}{reset}{quantity})", end='\r')
                return False
            else:
               return True
    except Exception as e:
                return True
                pass
    
import time
import random as rd
from concurrent.futures import ThreadPoolExecutor as sux

# ✅ Main Function
def process_orders():
    """Fetch and Process Orders with a countdown before checking new orders."""
    while True:
        global completed_orders

        # ✅ Countdown before fetching order_data
        countdown_time = 10  # Adjust countdown time as needed
        for remaining in range(countdown_time, 0, -1):
            print('\r' + ' ' * 60, end='')  # Clear previous text
            print(f'\r━━━━━━{yellow} Waiting for new order {reset} : {remaining} seconds', end='', flush=True)
            time.sleep(1)  # Wait 1 second per countdown step
        
        print("\n🚀 Checking for new orders...")  # Message after countdown

        order_data = api.get_order()  # ✅ Fetch order data after countdown

        try:
            if order_data and order_data['status'] == 'success':
                quantity = int(order_data['quantity'])
                order_link = order_data['link']
                order_id = order_data['id']
                if quantity > 0 and 'facebook.com' in order_link:
                    
                    completed_orders = 0
                    start_time = time.time()  # ✅ Capture the start time
                    
                    # Fix Redirects
                    if '/share/' in order_link:
                        order_link = rq.get(order_link, headers=fb_helper.headers_web, allow_redirects=True).url
                    
                    print(f"{darkblue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
                    print(f"📌 New Order : {order_id}{reset}")
                    print(f"{darkblue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
                    print(f"📦 Quantity: {quantity}{reset}")
                    print(f"{darkblue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
                    print(f"🔗 Link: {order_link}{reset}")
                    print(f"{darkblue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}")
                  
                    def work():
                        try:
                            responces = True
                            while responces:
                                fb_token = rd.choice(fb_tokens)
                                token = fb_token.split('|')[1]
                                responces = share_facebook_post(token, order_link, order_id, quantity) 
                        except:
                            pass 
                    
                    with sux(max_workers=200) as sub:
                        for _ in range(quantity):
                            sub.submit(work)
                        sub.shutdown()
                    
                    # ✅ Capture the end time
                    end_time = time.time()
                    
                    # ✅ Calculate elapsed time
                    elapsed_time = end_time - start_time
                    hours, remainder = divmod(elapsed_time, 3600)
                    minutes, seconds = divmod(remainder, 60)

                    # ✅ Print completion message with time taken
                    print(f"✅ Order ID {violet_chu}{order_id}{reset} Completed : Delivered {darkblue}{completed_orders}{reset} out of {red}{quantity}{reset}")         
                    print(f"⏳ Time Taken: {int(hours)}h {int(minutes)}m {int(seconds)}s")
                     
                    #✅ Save to file
                    save_order_to_txt(order_id, completed_orders, quantity, elapsed_time)
                    api.complete_order(order_id)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            pass

# ✅ Start Processing Orders
process_orders()
