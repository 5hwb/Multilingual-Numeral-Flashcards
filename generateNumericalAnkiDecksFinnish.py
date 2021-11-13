from file_io import load_file_to_str, save_str_to_file

ones = [
	'tyhjä', # 0
	'yksi', # 1
	'kaksi', # 2
	'kolme', # 3
	'neljä', # 4
	'viisi', # 5
	'kuusi', # 6
	'seitsemän', # 7
	'kahdeksan', # 8
	'yhdeksän' # 9
]

def get1(i, isNoZero=False):
	if isNoZero and i == 0:
		return ''
	return ones[i]

def get10(ii, i, isNoZero=False):
	if ii == 0:
		return get1(i, isNoZero)
	elif ii == 1 and i == 0:
		return 'kymmenen'
	elif ii == 1:
		return get1(i, True) + 'toista'
	else:
		return get1(ii, True) + 'kymmentä' + ' ' + get1(i, True)

def get100(iii, ii, i, isNoZero=False):
	if iii == 0:
		return get10(ii, i, isNoZero)
	elif iii == 1:
		return 'sata' + ' ' + get10(ii, i, True)
	else:
		return get1(iii, True) + 'sataa' + ' ' + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	elif iv == 1:
		return 'tuhat' + ' ' + get100(iii, ii, i, True)
	else:
		return get1(iv, True) + 'tuhatta' + ' ' + get100(iii, ii, i, True)

# Generate numbers from 0 to 20
def getListOfNumerals(start, end):
	daList = ''
	for x in range(start, end+1):
		xStr = '{:04d}'.format(x)
		result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
		daList += '{}\t{}\n'.format(result, x)
	return daList

save_str_to_file('first_20_numerals_finnish.txt', getListOfNumerals(0, 20))
save_str_to_file('numerals_to_9999_finnish.txt', getListOfNumerals(21, 9999))
