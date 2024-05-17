import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the article titles
        article_titles = soup.find_all('h2', class_='article-title')
        
        # Extract and print the titles
        for title in article_titles:
            print(title.text.strip())
    else:
        print("Failed to fetch the page.")

# URL of the news website
url = 'https://example.com/news'

# Call the function to scrape articles
scrape_articles(url)
