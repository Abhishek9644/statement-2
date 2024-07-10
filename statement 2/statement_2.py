#script that can check the uptime of an application :

from ctypes.wintypes import SERVICE_STATUS_HANDLE
from email.mime import application
from tkinter import TRUE
from urllib import request, response

import time

from requests import Request, RequestException

def check_app(url):
    try:
        response =response.get(url)
        if response.status_code ==200:
            return True,"app is up"
        else:
            return False,f"app is down(status code:{response.status_code})"
    except Request.ConnectionError:
        return False,"app is down (Connection error)"
    except request.Timeout:
        return False,"app is down (Timeout)"
    except RequestException.RequestException:
        return False,"app is down(Request Exception )"
    
if __name__ == "_main_":
   app_url = "http.//google.com" 
   while True:
       
    is_up,status_message = check_app(app_url)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}-{status_message}")
    time.sleep(60)
   