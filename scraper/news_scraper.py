import requests
from bs4 import BeautifulSoup

def get_latest_news():
    # Burimi i të dhënave (Web Scraping) [cite: 12]
    url = "https://top-channel.tv/" 
    
    # Përdorim korrekt i headers [cite: 17]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Trajtim i gabimeve (timeouts) [cite: 16]
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Nxjerrje e saktë e titullit kryesor [cite: 15]
        # Shënim: Klasa 'entry-title' është shembull, mund të ndryshojë sipas faqes
        headline = soup.find('h2').get_text(strip=True)
        
        return headline
    except Exception as e:
        # Trajtim i faqeve të papritura [cite: 16]
        print(f"Gabim gjatë scraping: {e}")
        return None