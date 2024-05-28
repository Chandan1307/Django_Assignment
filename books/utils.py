# books/utils.py
import requests
import pdb

def fetch_books(query):
    pdb.set_trace()  # Set a breakpoint here
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}')
    return response.json()
