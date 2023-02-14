# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

# Defining the function to scrape the web page 
def scrape_web(url, file_name):
    try:
        # Making a request to the url and getting the response
        response = requests.get(url)

        # Checking if the response was successful
        if response.status_code == 200:
            # Parsing the response using BeautifulSoup 
            soup = BeautifulSoup(response.text, 'html.parser')

            # Finding all the elements with tag 'a' 
            links = soup.find_all('a')

            # Creating an empty list to store all the scraped data 
            data = []

            # Updating the progress bar to show the progress of the scraping process
            progress = 0
            progress_bar["maximum"] = len(links)

            # Looping through each link and extracting required information 
            for link in links:
                # Updating the progress bar
                progress += 1
                progress_bar["value"] = progress

                # Updating the label with the current progress
                progress_label["text"] = f"Scraping link {progress} of {len(links)}"
                root.update()

                # Extracting href attribute from each link 
                href = link.get('href')

                # Extracting text from each link 
                text = link.text

                # Appending extracted data into list 
                data.append({'href': href, 'text': text})

            # Saving the data to a file
            with open(file_name, 'w') as file:
                # Write the data to the file as json
                json.dump(data, file)
                print(f"Data saved to the file: {file_name}")

            return data
        else:
            # Raise an error if the response status code is not 200
            raise Exception(f"Response status code: {response.status_code}")
    except Exception as e:
        # Print the error message
        print(f"An error occurred: {e}")
        return None

# Function to create the file dialog
def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    # Setting the file path to the entry widget
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Function to scrape the data and save to a file
def start_scraping():
    # Getting the URL and file path from the entry widgets
    url = url_entry.get()
    file_path = file_entry.get()
    # Calling the scrape_web function
    scraped_data = scrape_web(url, file_path)
    # Displaying the scraped data in the text widget
    if scraped_data is not None:
        result_text.config
