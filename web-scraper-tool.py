#importing necessary libraries
import requests
from bs4 import BeautifulSoup

#defining the function to scrape the web page 
def scrape_web(url):

    #making a request to the url and getting the response 
    response = requests.get(url)

    #parsing the response using BeautifulSoup 
    soup = BeautifulSoup(response.text, 'html.parser')

    #finding all the elements with tag 'a' 
    links = soup.find_all('a')

    #creating an empty list to store all the scraped data 
    data = []

    #looping through each link and extracting required information 
    for link in links:

        #extracting href attribute from each link 
        href = link.get('href')

        #extracting text from each link 
        text = link.text

        #appending extracted data into list 
        data.append({'href': href, 'text': text})

    return data
