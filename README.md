# 🍕 Pizza App

A simple Django web app with a homepage, pizza menu, and built-in user authentication pages.

## What this project demonstrates

- Django project/app structure (`pizza_project` + `pizza_app`)
- Function-based views and URL routing
- Server-rendered templates with static CSS
- Built-in Django auth forms for registration and login
- Session-based authentication/logout flow

## Features (implemented)

- Homepage at `/` with auth-aware navigation
- Menu page at `/menu/` with a static pizza list and pricing
- User registration (`/register/`) using `UserCreationForm`
- User login (`/login/`) using `AuthenticationForm`
- User logout (`/logout/`) via POST
- Django admin route at `/admin/`

## Technology stack

- Python
- Django
- SQLite (default Django database)
- HTML templates
- CSS static assets

## Repository structure

```text
Pizza_app/
├── manage.py
├── pizza_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── pizza_app/
│   ├── static/pizza_app/css/style.css
│   ├── templates/pizza_app/
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── login.html
│   │   └── register.html
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── tests.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Prerequisites

- Python 3.10+
- Git

## Clone and environment setup

1. Clone the repository and enter it:

```bash
git clone https://github.com/N1ksata/Pizza_app.git
cd Pizza_app
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```bat
venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Database migrations

From the repository root (where `manage.py` is):

```bash
python manage.py migrate
```

## Run the development server

```bash
python manage.py runserver
```

Open:

- App: http://127.0.0.1:8000/
- Menu: http://127.0.0.1:8000/menu/

## Admin panel

The admin site is enabled at:

- http://127.0.0.1:8000/admin/

Create an admin user (optional):

```bash
python manage.py createsuperuser
```

## Tests

Run the Django test command:

```bash
python manage.py test
```

Current status: the repository includes the Django test scaffold (`pizza_app/tests.py`) and can be expanded with app-specific tests.

## Screenshots

No screenshots are currently included in the repository.

When adding screenshots, place image files in a folder such as `docs/screenshots/` and reference them here, for example:

```markdown
![Homepage](docs/screenshots/homepage.png)
![Menu](docs/screenshots/menu.png)
![Login](docs/screenshots/login.png)
```

## Planned future improvements

- Add database-backed pizza models instead of static menu markup
- Add CRUD management for menu items through admin/custom views
- Add automated tests for auth flows and page responses
- Improve URL configuration to avoid duplicate route includes

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

## Author

- GitHub: [@N1ksata](https://github.com/N1ksata)
