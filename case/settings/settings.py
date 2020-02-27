# SECURITY WARNING: keep the secret key used in production secret!
import os
from dotenv import load_dotenv


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',
                 'webapp-728957.pythonanywhere.com',
                 'www.casemedan.com']
