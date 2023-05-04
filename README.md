# Hirup

Hirup is a Django website of resume for school that want their students and company to be able to find eachothers cooperative training course or internship 

## Prerequisite

Python 3.10+
Pip 22+

## Installation

Creating the Virtual Environments (optionnal)
```bash 
python3 -m venv env_name

On Windows, run: 
.\env_name\Scripts\activate.bat

On Unix or MacOS, run:
source env_name/bin/activate
```

Installing packages
```bash
pip install -r requirements.txt
```

To create the database (by default it is sqlite) :
```bash
python3 .\manage.py migrate
```

You can then either start the server using :
```bash
python3 .\manage.py runserver
```
Or create the admin user using :
```bash
python3 .\manage.py createsuperuser
```
###which will askfor:
###email (required field it will be the username)
###adresse electronique (optionnal)
###password (required field)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
