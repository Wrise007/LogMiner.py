from pattern_generator import get_substrate
import re

def hash(list):
	str = ''
	for item in list:
		str = str + '_' + item
	return str


fin = open('iikonet-full.log', 'r')
fout = open('iikonet_thread.log', 'w')

thread_pattern = r'(?P<date>\d{4}\-\d{2}\-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}\,\d{3}) \(\d*\) \[(?P<thread>\S*)\] (?P<type>[\w]{4,5})\ {1,2}\-\ (?P<main>.*)'
thread_parser = re.compile(thread_pattern)
while True:
    line = fin.readline()
    if line == '':
        break
    p_line = thread_parser.match(line)
    if p_line is None:
        continue
    fout.write(p_line.group('main')+'\n')

fin.close()
fout.close()

fin = open('iikonet_thread.log', 'r')

input()

list = []
dict = {}
while True:
	line = fin.readline()
	if line == '':
		break
	pattern = get_substrate(line)
	if hash(pattern['separator']) in list:
		dict[hash(pattern['separator'])].append(line)
	else:
		list.append(hash(pattern['separator']))
		dict[hash(pattern['separator'])] = [line]
print(len(list))
#for item in list:
#	print (item)
for i in range(0, len(list)):
	print('===Pattern '+ list[i])
	str_list = []
	for item in dict[list[i]]:
		if item not in str_list:
			str_list.append(item)
		
	for item in str_list:
		print (item)

		
#string = 'Create and open channel: 1 Call: 1 Close: 0 Abort: 0 Use POS server [True], settings changed [False] Use POS server [True], address []'