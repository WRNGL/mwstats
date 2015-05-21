import requests
import urllib2
import re
from urllib import urlopen
import sqlite3


LOGIN_URL = 'https://mwomercs.com/do/login'
# STATS_URL = 'https://mwomercs.com/profile/stats?type={0}'

login_data = {
	'email':'a3458795@trbvm.com',
	'password':'admin123',
	'submit':'login'
}

session = requests.session()
session.post(LOGIN_URL, data=login_data)
# req_nickname = session.get('https://mwomercs.com/profile')
# req.content

def GetName():
	req_nickname = session.get('https://mwomercs.com/profile')
	start_tag = '<h1>'
	end_tag = '</h1>'
	start_index = req_nickname.content.find(start_tag) + len(start_tag)
	end_index = req_nickname.content.find(end_tag)
	return req_nickname.content[start_index:end_index]


print GetName()