# Analiza e Motit dhe Lajmeve - Projekti Laboratorik

## [cite_start]1. Arkitektura e Zgjidhjes [cite: 41]
[cite_start]Ky projekt është ndërtuar mbi një pipeline të strukturuar të ndarë në module[cite: 3, 5]:
- [cite_start]**Scraper**: Nxjerrja e të dhënave nga web-i duke përdorur BeautifulSoup[cite: 13].
- [cite_start]**API Engine**: Integrimi i API-së së OpenWeatherMap për pasurimin e të dhënave[cite: 18].
- [cite_start]**Security**: Implementimi i enkriptimit simetrik (Fernet/AES).
- [cite_start]**Storage**: Ruajtja e të dhënave të enkriptuara në format .txt[cite: 31].

## [cite_start]2. Rrjedha e të Dhënave [cite: 42]
1. [cite_start]`news_scraper` merr titullin e fundit nga portali i lajmeve[cite: 6].
2. [cite_start]`weather_service` shton kushtet atmosferike për qytetin e përzgjedhur[cite: 21].
3. [cite_start]Të dhënat bashkohen dhe enkriptohen përmes modulit `security`[cite: 26].
4. [cite_start]Rezultati ruhet në folderin `data_storage/`[cite: 7].

## [cite_start]3. Siguria [cite: 44]
- [cite_start]Përdoret biblioteka `cryptography` për enkriptim real të të dhënave[cite: 31].
- [cite_start]Çelësat dhe kredencialet menaxhohen përmes skedarit `.env` për të shmangur vlerat "hard-coded"[cite: 30, 37].

## [cite_start]4. Udhëzime për Ekzekutim [cite: 45]
1. [cite_start]Instalo libraritë: `pip install -r requirements.txt`[cite: 43].
2. Konfiguro `.env` me API_KEY dhe ENCRYPTION_KEY.
3. Ekzekuto: `python main.py`.