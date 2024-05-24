from bs4 import BeautifulSoup

# Assuming q is your string containing HTML content
q = "<h1>Welcome to my HTML Page</h1><p>This is a paragraph demonstrating basic HTML structure.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><href='https://www.example.com'>Visit Example Website</a>"

# Parse the HTML string using BeautifulSoup
parsed_html = BeautifulSoup(q, features="html.parser")

# Now you can work with the parsed HTML content
print(parsed_html)
