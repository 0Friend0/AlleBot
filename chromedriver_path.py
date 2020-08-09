import os, sys

def chromedriverpath():

    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

    chromedriver_path =  os.path.join(dirname, "chromedriver.exe")

    return chromedriver_path
