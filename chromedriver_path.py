import os

def chromedriverpath():

    dirname, filename = os.path.split(os.path.abspath(__file__))

    chromedriver_path =  os.path.join(dirname, "chromedriver.exe")

    return chromedriver_path
