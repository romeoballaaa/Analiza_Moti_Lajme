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

1. **Klononi repository-n**:
   ```bash
   git clone [https://github.com/romeoballaaa/Analiza_Moti_Lajme.git](https://github.com/romeoballaaa/Analiza_Moti_Lajme.git)
2. **Instalo libraritë**: 
   ```bash
   pip install -r requirements.txt
3. **Konfigurimi i mjedisit (.env)**:
Pasi skedari .env është i injoruar për arsye sigurie, ju duhet të krijoni një skedar të ri me emrin .env në rrënjën e projektit dhe të shtoni vlerat e mëposhtme:
```text
WEATHER_API_KEY=celes_i_openweathermap
ENCRYPTION_KEY=celes_i_gjeneruar_fernet

4. **Si të gjeneroni çelësat?**:
WEATHER_API_KEY: Regjistrohuni falas në https://openweathermap.org/ dhe merrni çelësin tuaj te seksioni "My API Keys".

ENCRYPTION_KEY: Për të gjeneruar një çelës të vlefshëm Fernet, ekzekutoni këtë komandë në terminal:
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

5. **Ekzekutimi i Programit**:
```bash
python main.py