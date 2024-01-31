# wit_pi_zjazd3

Wytyczne do projektu:

Należy przekształcić aplikacje z zadania 2  tak aby:
- Logike biznesową (CRUD) miała wystawiona w formie REST API
- UI i frontend jako osobna aplikacja typu Single Page Application (React, Angular, Vue, JQuery) 
- Wywołania  przez API używajac bibliotek typu fetch, axios lub podobnych.

Jak uruchomić projekt:

1. Skopiować projekt
2. Zainstalować Python https://www.python.org/downloads/
3. Uruchomić wirtualne środowisko poleceniem <wit_pi_zjazd3-venv\Scripts\activate.bat> (Windows). Dla Linuxa i MacOS wystarczy wpisać <activate>
4. Uruchomić polecenie <pip install -r requirements.txt>, które pomoże nam się upewnić że wszystkie niezbędne moduły są zainstalowane
5. Wejść do folderu "productlist" i uruchomić polecenie napisane niżej w takiej kolejności jak są podane
<python manage.py makemigrations>
<python manage.py migrate>
<python manage.py runserver>
6. Odwiedzić stronę http://127.0.0.1:8000/

Strona admina:
http://127.0.0.1:8000/admin

login i hasło: admin



Start nowego projektu:
python -m venv wit_pi_zjazd2-venv

wit_pi_zjazd2-venv\Scripts\activate.bat (Windows)
activate (Linux i MacOS)

python.exe -m pip install --upgrade pip

pip install django

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser


API request examples:
No token or authorization is needed
![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/d37cfd93-c015-4eb3-826c-5e70432eb86e)

![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/3ac56f5b-7849-46e5-8854-a7df87361411)

![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/20bd21d0-20ca-453e-8eaf-986aeb6b3439)

![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/5f69e5b2-dbee-4701-969d-ba4c7da101f1)

![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/be0c9da2-3914-4c5b-a732-19f72cdcc201)

![image](https://github.com/yevheniiskakun/wit_pi_zjazd3/assets/56674669/8d1491fc-2e23-43f0-a0e0-40b8e6ba7f97)
