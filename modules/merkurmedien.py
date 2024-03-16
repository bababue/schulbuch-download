import requests
import os
from PIL import Image

filelist = []


def download(email, password, bookid, maxpages):


    print("Attempting login...")
    payload = {"username": email, "password": password, "remember-me": 0}
    r = requests.post("https://www.merkur-medien.de/login", data=payload)
    
    
    if r.status_code != 200:
        print("Login failed! Check your username and password")
        exit()

    print("Login successful!")

    session = (r.cookies)
    
    print("Starting download...")
    
    currentpage = 1
    while (currentpage <= maxpages):
        url= f"https://www.merkur-medien.de/dlm/zippo/{bookid}/preview/big/{currentpage}.jpg"
        filename = os.path.basename(url)
        response = requests.get(url , cookies=session)
        filelist.append(filename)
    
    
        if response.status_code == 200:
            with open(f"output/{filename}", 'wb') as file:
                file.write(response.content)
        else:
            print("Error while downlaoding image")
            exit()
    
        currentpage = currentpage + 1
    

    print("Downlaod successful!")

def merge():

    print("Starting PDF Merge...")
    images = [
        Image.open("output/" + f)
        for f in filelist
    ]
    images[0].save("final.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    print("PDF sucesfully merged!")
    print("Check final.pdf for final result")