#Imports
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import os
from PIL import Image


filelist = []

def download(email, password, bookid, maxpages):

    #Start Playwright browser
    with sync_playwright() as p:
        #Login
        browser = p.chromium.launch(headless=False, slow_mo=50)
        print("Playwright started...")
        page = browser.new_page()
        print("Attempting login...")
        page.goto(f'https://bibox2.westermann.de/book/{bookid}/page/1')
        page.is_visible("#account")
        page.fill("#account", email)
        page.fill("#password", password)
        page.click("#form_login > div > div:nth-child(4) > button")
        page.wait_for_selector(".pageview")
        print("Login successful!")

        print("Starting download...")

        #Main downloading loop
        currentpage = 1
        while (currentpage <= maxpages):

            page.goto(f'https://bibox2.westermann.de/book/{bookid}/page/{currentpage}')
            page.wait_for_selector(".pageview")

            html = page.inner_html("body")
            soup = BeautifulSoup(html, "lxml")
            images = soup.find_all("img", {"alt": "Buchseite"})

            for imageelement in images:
                url = (imageelement['src'])
                filename = os.path.basename(url)
                response = requests.get(url)
                filelist.append(filename)

                if response.status_code == 200:
                    with open(f"output/{filename}", 'wb') as file:
                        file.write(response.content)
                else:
                    print("Error while downlaoding image")

            if currentpage == 1:
                currentpage = currentpage + 1
            else:
                currentpage = currentpage + 2
        browser.close()
        print("Download successful!")

def merge():

    print("Starting PDF Merge...")
    images = [
        Image.open("output/" + f)
        for f in filelist
    ]
    images[0].save("final.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    print("PDF sucesfully merged!")
    print("Check final.pdf for final result")