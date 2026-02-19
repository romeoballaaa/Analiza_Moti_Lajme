import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://top-channel.tv/" 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Provojmë të gjejmë titullin në disa vende të mundshme (fallback logic)
        news_element = soup.find('h2') or soup.find('h1') or soup.find('a', class_='title')
        
        if news_element:
            return news_element.get_text(strip=True)
        
        return "Nuk u gjet asnje titull lajmi" # Trajtimi i mungesës së të dhënave
        
    except Exception as e:
        print(f"Gabim gjatë scraping: {e}") # Trajtimi i gabimeve
        return None