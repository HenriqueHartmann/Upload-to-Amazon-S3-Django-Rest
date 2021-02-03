# Upload-to-Amazon-S3-Django-Rest

API developed with djangorestframework to upload files to a Amazon S3 instance.

## Instalation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies needed.

Create a new virtual environment:
```
python3.8 -m venv venv
```

Activate virtualenv (OBS: on Linux):
```
source venv/bin/activate
```

Install all dependencies from requirements.txt:
```
pip install -r requirements.txt
```

## Settings

Copy the content of .env.example and paste on .env:
```
cp backend/core/.env.example backend/core/.env
```

And the same in appupload:
```
cp backend/appupload/.env.example backend/appupload/.env
```

Inside the .env's files, we already have some default values set. Then you can change to your taste:
```
# /backend/core/
DEBUG=on
SECRET_KEY=YOUR_SECRET_KEY
SQLITE_URL=sqlite:///backend/your-database-name.sqlite3

# /backend/appupload/
REGION_NAME=YOUR_REGION
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
BUCKET=THE_DESTINY_BUCKET
```

## Running

Run the server:
```
backend/manage.py runserver
```

## Endpoints

#### /api/file-s3/

To test you can use postman or similars. Or just a simple python script like this:
```
import requests
test_file = open("some_file", "rb")
test_url = "http://localhost:port/api/file-s3/"
test_response = requests.post(test_url, files = {"file": test_file})
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
    print(test_response.text)
```
