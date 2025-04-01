# Car Sales - Aplikacja Flask

## 📌 Opis projektu
Car Sales to aplikacja internetowa stworzona przy użyciu frameworka Flask, umożliwiająca użytkownikom przeglądanie ofert sprzedaży samochodów oraz korzystanie z usług takich jak naprawa, detailing i zakup części.

## 🛠️ Technologie
- Python (Flask)
- HTML, CSS (Bootstrap)
- SQLAlchemy

## 🚀 Instalacja
1. **Sklonuj repozytorium:**
   ```sh
   git clone https://github.com/CichyFlashy/carsales.git
   cd carsales
   ```
2. **Utwórz i aktywuj wirtualne środowisko:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. **Zainstaluj wymagane pakiety:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Uruchom aplikację Flask:**
   ```sh
   flask run
   ```
5. **Otwórz w przeglądarce:**
   - Przejdź do: `http://127.0.0.1:5000/`

## 📂 Struktura katalogów
```
/carsales
│-- /static          # Pliki statyczne (CSS, obrazy)
│-- /templates       # Szablony HTML
│-- app.py           # Główny plik aplikacji
│-- requirements.txt # Lista zależności
│-- README.md        # Dokumentacja
```

## 🔧 Konfiguracja
- Jeśli aplikacja wymaga bazy danych, uruchom migrację:
  ```sh
  flask db upgrade
  ```
- Możesz dostosować ustawienia w `config.py`.

## 🌟 Funkcje
- Wyświetlanie ofert samochodów
- Logowanie i rejestracja użytkowników
- Obsługa zapytań klientów (formularz kontaktowy)


