# Analiza e Motit dhe Lajmeve - Projekti Laboratorik

## 1. Arkitektura e Zgjidhjes
Ky projekt është ndërtuar mbi një pipeline të strukturuar të ndarë në module:
- **Scraper**: Nxjerrja e të dhënave nga web-i duke përdorur BeautifulSoup.
- **API Engine**: Integrimi i API-së së OpenWeatherMap për pasurimin e të dhënave.
- **Security**: Implementimi i enkriptimit simetrik (Fernet/AES).
- **Storage**: Ruajtja e të dhënave të enkriptuara në format .txt.

## 2. Rrjedha e të Dhënave
1. `news_scraper` merr titullin e fundit nga portali i lajmeve.
2. `weather_service` shton kushtet atmosferike për qytetin e përzgjedhur (Tirana).
3. Të dhënat bashkohen dhe enkriptohen përmes modulit `security`.
4. Rezultati ruhet i enkriptuar në folderin `data_storage/`.

## 3. Siguria
- Përdoret biblioteka `cryptography` për enkriptim real të të dhënave (Fernet).
- Çelësat dhe kredencialet menaxhohen përmes skedarit `.env` për të shmangur vlerat "hard-coded", duke garantuar sigurinë e kodit në GitHub.

## 4. Udhëzime për Ekzekutim
1. **Instalo libraritë**: 
   ```bash
   pip install -r requirements.txt