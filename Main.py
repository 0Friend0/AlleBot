from functions import Application
from additionalData import AuctionData

def start(item, price_min, price_max):

    Ap = Application()
    ad = AuctionData()

    # Open WebDriver, load Allegro.pl website and search for item.
    Ap.open(item)
    # Insert additional filters to Allegro.pl.
    Ap.additional_filter_price(price_min, price_max)
    # Create excel file.
    Ap.create_excel_file(item)
    # Find items.
    Ap.finding_items(item)
    # Close driver
    Ap.driver_close()
    # Get auction info for every item found. Returns how many items were found.
    item_count = ad.gets_auction_info_master(item)

    return item_count
