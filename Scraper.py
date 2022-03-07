import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import connect



parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the name of db", type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
Page_num_MAX = args.page_num_max
scraped__info_list=[]
connect.connect(args.dbname)

for page_num in range(1,Page_num_MAX):
    url = oyo_url + str(page_num)
    print("GET Request for: ",url)
    req =requests.get(url)
    content = req.content
    
    soup = BeautifulSoup(content,"html.parser")
    
    all_hotels = soup.find_all("div", {"class","hotelCardListing"})
    scraped_info_list = []
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict['name']=hotel.find("h3", {"class","listingHotelDescription__hotelName"}).text
        hotel_dict['address']=hotel.find("span", {"itemprop","streetaAddress"}).text
        hotel_dict['price']=hotel.find("span", {"class","listingPrice_finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class","hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None
            
        parent_amenities_elements = hotel.find("div",{"class","amenityWrapper"})
        
        amenities_list = []
            
        for amenity in parent_amenities_elements.find_all("div",{"class","amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class":"d-body-sm"})).text.strip()
        
        hotel_dict["amenities"]  = ', '.join(amenities_list[:-1])
        scraped__info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

dataframe = pd.DataFrame(scraped__info_list)
print("Creating Csv file...")
dataframe.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)