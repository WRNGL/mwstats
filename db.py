import sqlite3
from urllib2 import urlopen

'''
<tr>
<td>Kills / Death</td>
<td>1,964 / 1,303</td>
</tr>							

<tr>
<td>Wins / Losses</td>
<td>1,254 / 897</td>
</tr>
'''

my_address = 'http://team.alpha-legion.pro/profile.html'
html_page = urlopen(my_address)

html_text = html_page.read()

start_kill = 'Death</td><td>'
end_kill = 


player = raw_input('Enter your ingame nickname: ')
kill = 1967
death = 1305
win = 1256
lose = 899

'''
kill = 0
death = 0
win = 0
lose = 0
'''

winlose_values = (
	player, kill, death, win, lose)



connection = sqlite3.connect('mwo.db')
c = connection.cursor()
#c.execute('CREATE TABLE WinLose(Name TEXT, Kill INT, Death INT, Win INT, Lose INT)')

c.execute("INSERT INTO WinLose VALUES(?, ?, ?, ?, ?)", winlose_values)
connection.commit()
print 'All your stats are belong to us, ', player, '!' 