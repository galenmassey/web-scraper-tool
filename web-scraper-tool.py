# Adding user interface to allow user input and view the scraped data:

# importing necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
from tkinter import filedialog

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

# Function to create the file dialog
def browse_file():
file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
# setting the file path to the entry widget
file_entry.delete(0, tk.END)
file_entry.insert(0, file_path)

# Function to scrape the data and save to a file
def start_scraping():
# getting the URL and file path from the entry widgets
url = url_entry.get()
file_path = file_entry.get()
# calling the scrape_web function
scraped_data = scrape_web(url, file_path)
# displaying the scraped data in the text widget
if scraped_data is not None:
result_text.config(state="normal")
result_text.delete("1.0", tk.END)
result_text.insert(tk.END, json.dumps(scraped_data, indent=2))
result_text.config(state="disabled")

# Creating the tkinter GUI
root = tk.Tk()
root.title("Web Scraper")

#URL label and entry widget
url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.


