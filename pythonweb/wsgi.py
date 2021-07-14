import os
import sys
 
path = '/home/<PythonAnywhere-username>/phocode-site'
if path not in sys.path:
 sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'PhoCode.settings'
 
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
