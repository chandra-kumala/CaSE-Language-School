from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mz+6pou%g!l+!4)(nc(^b%@m=*enkxrag=!u6bwy5kih2-l2j-'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 



try:
    from .local import *
except ImportError:
    pass
