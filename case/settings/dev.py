from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mz+6pou%g!l+!4)(nc(^b%@m=*enkxrag=!u6bwy5kih2-l2j-'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

<<<<<<< HEAD
=======
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
>>>>>>> 30086d6f33b5fe4cf1c8e714c363070971901ee9


try:
    from .local import *
except ImportError:
    pass
