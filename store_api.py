import json

# Path to your JSON file
json_file_path = 'data.json'

# Read data from the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Extract product names into an array
product_names = [product['name'] for product in json_data]

# Function to check if a product is found
def is_product_found(product_name):
    return product_name in product_names

# Print the JSON data
# print("JSON Data:")
# print(json_data)

# # Print the product names
# print("\nProduct Names:")
# print(product_names)

# Example usage of the function
searched_product = 'Product 10'
if is_product_found(searched_product):
    print(f"\n{searched_product} is found in the product names.")
else:
    print(f"\n{searched_product} is not found in the product names.")
