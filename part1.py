import sys
import time
from bs4 import BeautifulSoup
import requests

url = "https://www.cricbuzz.com/"
try:
    page = requests.get(url)
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print("Error from link:", url)
    print(error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
soup = BeautifulSoup(page.text, 'html.parser')

# Extract data
links = soup.find_all('div', attrs={"class": "cb-nws-intr"})

# Create an HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cricbuzz News</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f8f9fa;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .news-container {
            width: 80%;
            margin: auto;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .news-item {
            padding: 15px;
            border: 1px solid #ccc;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        }
        .news-item:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>Cricbuzz News Highlights</h1>
    <div class="news-container">
"""

# Add scraped data into the HTML structure
for i in links:
    html_content += f"""
        <div class="news-item">
            {i.text}
        </div>
    """

# Close the HTML tags
html_content += """
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open("cricbuzz_news.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Data has been saved to 'cricbuzz_news.html'")
