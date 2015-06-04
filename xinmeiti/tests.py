from django.test import TestCase
from datetime import date,timedelta
# Create your tests here.
print type(str((date.today())))
print type(date.today()+timedelta(days=-1))
