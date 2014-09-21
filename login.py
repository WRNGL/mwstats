import requests
import urllib2


LOGIN_URL = 'https://mwomercs.com/do/login'
STATS_URL = 'https://mwomercs.com/profile/stats?type={0}'

login_data = {
	'email':raw_input('Enter email: '),
	'password':raw_input('Enter password: '),
	'submit':'login'
}

session = requests.session()
session.post(LOGIN_URL, data=login_data)
req = session.get('https://mwomercs.com/profile/stats?type={0}')
print req.content
