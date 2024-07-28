import requests
from bs4 import BeautifulSoup

coursera_url = "https://www.coursera.org/courseraplus?utm_medium=sem&utm_source=gg&utm_campaign=b2c_india_coursera-plus_coursera_ftcof_subscription_arte_may-24_dr_exact_sem_rsa_gads_lg-all&campaignid=21327429274&adgroupid=162815312357&device=m&keyword=coursera&matchtype=e&network=g&devicemodel=&adposition=&creativeid=700607287634&hide_mobile_promo&gad_source=1&gclid=Cj0KCQjwtZK1BhDuARIsAAy2VzuyUGDCZCZdju0Hmh3kDIUeL48Kgd50rNAnKfRymMVJAaYTiX3mdlUaAl3xEALw_wcB"
page_response = requests.get(coursera_url)

if page_response.status_code == 200:
    parsed_page = BeautifulSoup(page_response.text, 'html.parser')
    image_tags = parsed_page.find_all('img')
    
    print("Extracted Image Data:")
    for image in image_tags:
        image_source = image.get('src', 'No source available')
        image_description = image.get('alt', 'No description available')
        print(f"Image Source: {image_source} - Alt Text: {image_description}")
else:
    print(f"Unable to retrieve content from {coursera_url}, HTTP Status: {page_response.status_code}") 