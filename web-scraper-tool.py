# importing necessary libraries
import requests
from bs4 import BeautifulSoup
import json

# defining the function to scrape the web page 
def scrape_web(url, file_name):
try:
# making a request to the url and getting the response
response = requests.get(url)

            # checking if the response was successful
    if response.status_code == 200:
        # parsing the response using BeautifulSoup 
        soup = BeautifulSoup(response.text, 'html.parser')

        # finding all the elements with tag 'a' 
        links = soup.find_all('a')

        # creating an empty list to store all the scraped data 
        data = []

        # looping through each link and extracting required information 
        for link in links:
            # extracting href attribute from each link 
            href = link.get('href')

            # extracting text from each link 
            text = link.text

            # appending extracted data into list 
            data.append({'href': href, 'text': text})
        
        # saving the data to a file
        with open(file_name, 'w') as file:
            # write the data to the file as json
            json.dump(data, file)
            print(f"Data saved to the file: {file_name}")
            
        return data
    else:
        # raise an error if the response status code is not 200
        raise Exception(f"Response status code: {response.status_code}")
except Exception as e:
    # print the error message
    print(f"An error occurred: {e}")
    return None

