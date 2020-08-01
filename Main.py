from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
from functions import Application
from additionalData import AuctionData

def start(item, price_min, price_max):
    Ap = Application()
    ad = AuctionData()

    Ap.open(item)
    Ap.additional_filter_price(price_min, price_max)
    Ap.create_excel_file()
    Ap.finding_items()
    Ap.driver_close()
    ad.gets_auction_info_master()
