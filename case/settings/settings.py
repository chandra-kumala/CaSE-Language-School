# SECURITY WARNING: keep the secret key used in production secret!
import os
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['127.0.0.1', 'webapp-728957.pythonanywhere.com', 'www.casemedan.com']
