import requests
# Define the data for the new Product
data = {
    "name": "New Product Name",
    "description": "Product description goes here.",
    "category": "Sports",  # Replace with an existing category name
    "mrp": 29.99,
    "discount": 2.00
}

api_url = "http://127.0.0.1:8000/api/shop/" 
# Send a POST request to create the Product
response = requests.post(api_url, json=data)

print(response)