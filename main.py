from scraper.news_scraper import get_latest_news
from api_engine.weather_service import get_weather_data
from security.encryptor import encrypt_message
import os

def run_pipeline():
    print("--- Duke nisur procesimin e te dhenave ---")

    # 1. Web Scraping (Burimi)
    news_title = get_latest_news()
    if not news_title:
        print("Deshtoi marrja e lajmeve.")
        return

    # 2. Integrim API (Pasurimi)
    # Po marrim motin per Tiranen si shembull
    weather_info = get_weather_data("Tirana")
    
    # Bashkimi i te dhenave (Data Transformation)
    final_report = f"Lajmi: {news_title} | Moti: {weather_info}"
    print(f"Te dhenat e paprocesuara: {final_report}")

    # 3. Siguria (Enkriptimi)
    encrypted_report = encrypt_message(final_report)
    print(f"Raporti i enkriptuar: {encrypted_report}")

    # 4. Storage (Ruajtja)
    with open("data_storage/final_results.txt", "wb") as f:
        f.write(encrypted_report)
    
    print("--- Procesi perfundoi me sukses! Raporti u ruajt i enkriptuar. ---")

if __name__ == "__main__":
    run_pipeline()