# Storefront

A simple Django 5.2 project with a dark-themed UI (home, hello, about pages).

## Run the project

### Option A: Pipenv (recommended if you use it)

```powershell
cd c:\Users\fresh\Documents\projects\ths\storefront
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```

If you get **"No module named 'django'"**, you're not in the Pipenv environment. Use `pipenv shell` first, or run:

```powershell
pipenv run python manage.py runserver
```

### Option B: Plain Python + pip

```powershell
cd c:\Users\fresh\Documents\projects\ths\storefront
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

## If `pipenv install` fails (e.g. Permission denied)

- Run your terminal **as Administrator**, or
- Use **Option B** (venv + `pip install -r requirements.txt`) instead.
