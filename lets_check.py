#! /bin/python3

import requests, json 
from pprint import pprint
import shutil


# URL for the social-scan API endpoint
api_url = "https://social-scanner.p.rapidapi.com/social-scan/"

columns, rows = shutil.get_terminal_size()


# Add ANSI escape code to set text color to purple and bold
print("\033[41m\033[1m")

# Calculate the number of spaces needed to center the banner
num_spaces = int((columns - len("L       E       T       S       C       H       E       C       K")) / 2)

# Print the banner with leading whitespace to center it
print(" " * num_spaces + "    /\__/\\")
print(" " * num_spaces + "   /`    '\\")
print(" " * num_spaces + "  //  ~~~  \\\\")
print(" " * num_spaces + " / |       |  \\")
print(" " * num_spaces + "(  )       (  )")
print(" " * num_spaces + " \\/____   __\\/")
print(" " * num_spaces + "       \\ /")
print(" " * num_spaces + "       |=|")
print(" " * num_spaces + "       | |")
print(" " * num_spaces + "       \\_/")
print(" " * num_spaces + "L       E       T       S       C       H       E       C       K")

# Add ANSI escape code to reset text color
print("\033[0m")


# Prompt user for their username
username = input("please enter username:")

# Prompt user for target count (number of social media profiles to retrieve)
while True:
    try:
        # Prompt user for target count (number of social media profiles to retrieve)
        target_count = int(input(" enter target count (1-20): "))
        # Ensure the target count is within the acceptable range
        if 1 <= target_count <= 20:
            break
        else:
            print("Invalid target count. Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Format payload with user-specified username and target count
payload = "username={}&target_count={}".format(username, target_count) 

# Set headers for API request
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "c7bbf2821dmsh7ccae6a502b2694p168ae5jsn2a49425d4390",
    "X-RapidAPI-Host": "social-scanner.p.rapidapi.com"
}

# Send POST request to the API
try:
    response = requests.request("POST", api_url, data=payload, headers=headers)
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
    exit()

# Convert response to a dictionary
response_dict = json.loads(response.text)

# Print the dictionary
pprint(response_dict)

# Open a file to write the response to
json_file = open("data.json", "w")

# Write the response to the file
json_file.write(response.text)

# Close the file
json_file.close() 

# Open the file for reading
json_file = open("data.json", "r")

# Load the file contents into a variable
values = json.load(json_file)

# Close the file
json_file.close()

print("--------------------------------------------------------------------")

# Construct a URL based on the user's inputted username
website = "http://" + username + ".com"

# Define a function to check if a website exists
def website_check(website):
        try: 
                # Send a GET request to the website
                get_response = requests.get(website)
                # If the request is successful (status code 200), print that the website exists
                if get_response.status_code == 200:
                     print(website, "is a website")
                # If the request is unsuccessful, print that the website does not exist
                else: 
                     print (website, "is not a website")
        # If there is a connection error, print that the website does not exist
        except requests.ConnectionError as e:
                print(website, "is not a website")

# Call the website_check function with the constructed website URL
website_check(website)

