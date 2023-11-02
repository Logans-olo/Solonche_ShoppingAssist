import requests
import json
import tkinter as tk

# Define a callback function to send the API request
def requestAPI():
    search_term = x.get()
    params = {
        'api_key': '6C705EB1F4C5457DB994C733005B6D00',
        'type': 'search',
        'search_term': search_term,
        'sort_by': 'best_seller'
    }

    # Make the HTTP GET request to the RedCircle API
    api_result = requests.get('https://api.redcircleapi.com/request', params)

    # Print the JSON response from the RedCircle API
    api_string = json.dumps(api_result.json(), indent=2)
    print(api_string)

    # If you want to save the response to a file
    with open("myfile.txt", "a") as file1:
        file1.write(api_string)

# Create the main tkinter window
master = tk.Tk()
master.title('Input Window')

# Create a StringVar to hold the product name
x = tk.StringVar()

# Create a label and an entry field for the product name
tk.Label(master, text='Product Name').grid(row=0)
e1 = tk.Entry(master, textvariable=x)
e1.grid(row=0)

# Create a button to generate the report
tk.Button(master, text='Generate Report', width=25, command=requestAPI).grid(row=1)

# Create a button to display the results (you can add functionality to it)
tk.Button(master, text='Display Results', width=25).grid(row=2)

# Start the tkinter main loop
master.mainloop()
