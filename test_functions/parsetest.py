import re
from urllib import urlopen
import sqlite3

player = raw_input('Enter your ingame nickname: ')

my_address = 'http://team*******/profile.html'
html_page = urlopen(my_address)
html_text = html_page.read()
start_tag = '<tbody>'
end_tag = 'Death Ratio'
start_index = html_text.find(start_tag)
end_index = html_text.find(end_tag)
text_raw = html_text[start_index:end_index].replace(',','')
# text_raw = text_raw.replace(',','')
mah_list =  re.findall(r'\d+', text_raw)
# print type(mah_list)
# print mah_list
# print mah_list[0]

# player = raw_input('Enter your ingame nickname: ')
mc = mah_list[0]
kill = mah_list[1]
death = mah_list[2]
cbills = mah_list[3]
exp = mah_list[4]
win = mah_list[5]
lose = mah_list[6]

winlose_values = (
	player, mc, kill, death, cbills, exp, win, lose
	)

connection = sqlite3.connect('mwo.db')
c = connection.cursor()

c.execute("INSERT INTO BaseStats VALUES(?, ?, ?, ?, ?, ?, ?, ?)", winlose_values)
connection.commit()
print 'All your stats are belong to us, ', player, '!' 
