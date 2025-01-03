class NumeralGenerator:
	'''
	Base class for all NumeralGenerators for each language
	'''
	def __init__(self, name):
		self.name = name
	
	def get1(self, i, isNoZero=False):
		return ''
	
	def get10(self, ii, i, isNoZero=False):
		return ''
	
	def get100(self, iii, ii, i, isNoZero=False):
		return ''
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		return ''

class NumeralGeneratorArmenianRomanised(NumeralGenerator):
	'''
	Numeral generator for Armenian (romanised)
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'armenian_r')	
		self.ones = [
			'zro', # 0
			'mek', # 1
			'yerku', # 2
			'yerek\'', # 3
			'ch\'ors', # 4
			'hing', # 5
			'vets\'', # 6
			'yot\'', # 7
			'ut\'', # 8
			'iny' # 9
		]
		self.tens = [
			'', # 0
			'tasy', # 10
			'k\'san', # 20
			'yeresun', # 30
			'k\'arrasun', # 40
			'hisun', # 50
			'vat\'sun', # 60
			'yot\'anasun', # 70
			'ut\'sun', # 80
			'inisun' # 90
		]
		self.teen = 'tasn'
		self.hundred = 'haryur'
		self.thousand = 'hazar'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teen + self.get1(i, isNoZero)
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			return self.tens[ii] + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		theTens = ' ' + self.get10(ii, i, True)
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif iii == 1: # 100-199
			return self.hundred + theTens
		else: # 200+
			return self.get1(iii, True) + ' ' + self.hundred + theTens
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		theHundred = ' ' + self.get100(iii, ii, i, True)
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1: # 1001-1999
			return self.thousand + theHundred
		else: # >= 1100
			return self.get1(iv, True) + ' ' + self.thousand + theHundred

class NumeralGeneratorChineseHanzi(NumeralGenerator):
	'''
	Numeral generator for Chinese (hanzi)
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'chinese_hanzi')
		self.ones = [
			'零', # 0
			'一', # 1
			'二', # 2
			'三', # 3
			'四', # 4
			'五', # 5
			'六', # 6
			'七', # 7
			'八', # 8
			'九' # 9
		]
		self.twoAlt = '两'
		self.oneTen = '十'
		self.oneHundred = '百'
		self.oneThousand = '千'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + self.get1(i, True)
		else:
			return self.get1(ii, True) + self.oneTen + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 2:
			return self.twoAlt + self.oneHundred + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + self.oneHundred + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 2:
			return self.twoAlt + self.oneThousand + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + self.oneThousand + self.get100(iii, ii, i, True)

class NumeralGeneratorChineseMandarin(NumeralGenerator):
	'''
	Numeral generator for Chinese (Mandarin)
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'chinese_mandarin')		
		self.ones = [
			'líng', # 0
			'yī', # 1
			'èr', # 2
			'sān', # 3
			'sì', # 4
			'wǔ', # 5
			'liù', # 6
			'qī', # 7
			'bā', # 8
			'jiǔ' # 9
		]
		self.twoAlt = 'liǎng'
		self.oneTen = 'shí'
		self.oneHundred = 'bǎi'
		self.oneThousand = 'qiān'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + ' ' + self.get1(i, True)
		else:
			return self.get1(ii, True) + ' ' + self.oneTen + ' ' + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 2:
			return self.twoAlt + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 2:
			return self.twoAlt + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorEnglish(NumeralGenerator):
	'''
	Numeral generator for English
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'english')	
		self.ones = [
			'zero', # 0
			'one', # 1
			'two', # 2
			'three', # 3
			'four', # 4
			'five', # 5
			'six', # 6
			'seven', # 7
			'eight', # 8
			'nine' # 9
		]
		self.teens = [
			'', # 10
			'eleven', # 11
			'twelve', # 12
			'thirteen', # 13
			'fourteen', # 14
			'fifteen', # 15
			'sixteen', # 16
			'seventeen', # 17
			'eighteen', # 18
			'nineteen' # 19
		]
		self.tens = [
			'', # 0
			'ten', # 10
			'twenty', # 20
			'thirty', # 30
			'forty', # 40
			'fifty', # 50
			'sixty', # 60
			'seventy', # 70
			'eighty', # 80
			'ninety' # 90
		]
		self.hundred = 'hundred'
		self.thousand = 'thousand'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			return self.tens[ii] + '-' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i == 0: # 100, 200...
			return self.get1(iii, True) + ' ' + self.hundred
		else: # 101-199, 201-299...
			return self.get1(iii, True) + ' ' + self.hundred + ' and ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iii == 0 and not (ii == 0 and i == 0): # 1001-1099, 2001-2099...
			return self.get1(iv, True) + ' ' + self.thousand + ' and ' + self.get100(iii, ii, i, True)
		else: # >= 1100
			return self.get1(iv, True) + ' ' + self.thousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorFinnish(NumeralGenerator):
	'''
	Numeral generator for Finnish
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'finnish')	
		self.ones = [
			'nolla', # 0
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
		self.oneTen = 'kymmenen'
		self.teens = 'toista'
		self.twoOrMoreTens = 'kymmentä'
		self.oneHundred = 'sata'
		self.twoOrMoreHundreds = 'sataa'
		self.oneThousand = 'tuhat'
		self.twoOrMoreThousands = 'tuhatta'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0:
			return self.oneTen
		elif ii == 1:
			return self.get1(i, True) + self.teens
		else:
			return self.get1(ii, True) + self.twoOrMoreTens + ' ' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 1:
			return self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + self.twoOrMoreHundreds + ' ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1:
			return self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + self.twoOrMoreThousands + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorFrench(NumeralGenerator):
	'''
	Numeral generator for French
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'french')	
		self.ones = [
			'zéro', # 0
			'un', # 1
			'deux', # 2
			'trois', # 3
			'quatre', # 4
			'cinq', # 5
			'six', # 6
			'sept', # 7
			'huit', # 8
			'neuf' # 9
		]
		self.teens = [
			'', # 10
			'onze', # 11
			'douze', # 12
			'treize', # 13
			'quatorze', # 14
			'quinze', # 15
			'seize', # 16
			'dix-sept', # 17
			'dix-huit', # 18
			'dix-neuf' # 19
		]
		self.tens = [
			'', # 0
			'dix', # 10
			'vingt', # 20
			'trente', # 30
			'quarante', # 40
			'cinquante', # 50
			'soixante', # 60
			'soixante', # 70
			'quatre-vingt', # 80
			'quatre-vingt' # 90
		]
		self.altOne = 'et-un'
		self.altEleven = 'et-onze'
		self.eighty = 'quatre-vingts'
		self.hundred = 'cent'
		self.hundreds = 'cents'
		self.thousand = 'mille'
	
	def get1(self, i, isNoZero=False, useAltOne=False):
		if isNoZero and i == 0:
			return ''
		if useAltOne and i == 1:
			return self.altOne
		return self.ones[i]

	def getTeens(self, i, isNoZero=False, useAltEleven=False):
		if isNoZero and i == 0:
			return ''
		if useAltEleven and i == 1:
			return self.altEleven
		return self.teens[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.getTeens(i)
		elif (ii == 7 or ii == 9) and i == 0: # 70, 90 
			return self.tens[ii-1] + '-' + self.tens[1]
		elif ii == 8 and i == 0: # 80 
			return self.eighty
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		elif i == 1 and ii != 8: # == 21, 31, 41... special case for 81
			theAltOne = self.getTeens(i, True, ii == 7) if (ii == 7 or ii == 9) else self.altOne
			return self.tens[ii] + '-' + theAltOne
		else: # 22, 45, etc
			theOne = self.getTeens(i, True, ii == 7) if (ii == 7 or ii == 9) else self.get1(i, True)
			return self.tens[ii] + '-' + theOne
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		else: # 100, 200, 300, 400...
			theNumHundred = '' if iii == 1 else self.get1(iii, True) + '-'
			theHundred = self.hundreds if (iii != 1 and (ii == 0 and i == 0)) else self.hundred
			theTen = '' if (ii == 0 and i == 0) else '-' + self.get10(ii, i, True)
			return theNumHundred + theHundred + theTen
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		else: # >= 1100
			theNumThousand = '' if iv == 1 else self.get1(iv, True) + '-'
			theHundred = '' if (iii == 0 and ii == 0 and i == 0) else '-' + self.get100(iii, ii, i, True)
			return theNumThousand + self.thousand + theHundred

class NumeralGeneratorGeorgian(NumeralGenerator):
	'''
	Numeral generator for Georgian
	'''
	def __init__(self, name='georgian'):
		NumeralGenerator.__init__(self, name)
		self.ones = [
			'ნულ', # 0
			'ერთ', # 1
			'ორ', # 2
			'სამ', # 3
			'ოთხ', # 4
			'ხუთ', # 5
			'ექვს', # 6
			'შვიდ', # 7
			'რვა', # 8
			'ცხრა' # 9
		]
		self.teens = [
			'ათ', # 10
			'თერთმეტ', # 11
			'თორმეტ', # 12
			'ცამეტ', # 13
			'თოთხმეტ', # 14
			'თხუთმეტ', # 15
			'თექვსმეტ', # 16
			'ჩვიდმეტ', # 17
			'თვრამეტ', # 18
			'ცხრამეტ' # 19
		]
		self.twenties = [
			'', # 0
			'ოც', # 20
			'ორმოც', # 40
			'სამოც', # 60
			'ოთხმოც', # 80
		]
		self.hundred = 'ას'
		self.thousand = 'ათას'
		self.theI = 'ი'
		self.theDa = 'და'

	def get1(self, i, isNoZero=False, showI=True):
		if isNoZero and i == 0:
			return ''
		return self.ones[i] + ('' if i == 8 or i == 9 else self.theI if showI else '')

	def getTeens(self, i, isNoZero=False, showI=True):
		onesAndTeens = self.ones + self.teens
		if isNoZero and i == 0:
			return ''
		return onesAndTeens[i] + ('' if i == 8 or i == 9 else self.theI if showI else '')

	def get10(self, ii, i, isNoZero=False):
		if ii <= 1: # < 20
			return self.getTeens((ii*10) + i, isNoZero)
		elif i == 0 and ii % 2 == 0: # even number = mult of 20
			return self.twenties[ii // 2] + self.theI
		else:
			return self.twenties[ii // 2] + self.theDa + self.getTeens(((ii % 2)*10) + i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		isPlainHundred = (ii == 0 and i == 0) # true for 100, 200, 300 etc
		suffix = self.theI if (isPlainHundred) else ' ' + self.get10(ii, i, True)
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif iii == 1: # 100
			return self.hundred + suffix
		else: # 200+
			return self.get1(iii, True, showI=False) + self.hundred + suffix

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		isPlainThousand = (iii == 0 and ii == 0 and i == 0) # true for 1000, 2000, 3000 etc
		suffix = self.theI if (isPlainThousand) else ' ' + self.get100(iii, ii, i, True)
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1: # 1000
			return self.thousand + suffix
		else: # 2000+
			return self.get1(iv, True) + ' ' + self.thousand + suffix

class NumeralGeneratorGeorgianRomanised(NumeralGeneratorGeorgian):
	'''
	Numeral generator for Georgian (romanised)
	'''
	def __init__(self):
		NumeralGeneratorGeorgian.__init__(self, 'georgian_r')
		self.ones = [
			'nul', # 0
			'ert', # 1
			'or', # 2
			'sam', # 3
			'otkh', # 4
			'khut', # 5
			'ekvs', # 6
			'švid', # 7
			'rva', # 8
			'tskhra' # 9
		]
		self.teens = [
			'at', # 10
			'tertmet\'', # 11
			'tormet\'', # 12
			'tsamet\'', # 13
			'totkhmet\'', # 14
			'tkhutmet\'', # 15
			'tekvsmet\'', # 16
			'čvidmet\'', # 17
			'tvramet\'', # 18
			'tskhramet\'' # 19
		]
		self.twenties = [
			'', # 0
			'ots', # 20
			'ormots', # 40
			'samots', # 60
			'otkhmots', # 80
		]
		self.hundred = 'as'
		self.thousand = 'atas'
		self.theI = 'i'
		self.theDa = 'da'

class NumeralGeneratorGerman(NumeralGenerator):
	'''
	Numeral generator for German
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'german')	
		self.ones = [
			'null', # 0
			'eins', # 1
			'zwei', # 2
			'drei', # 3
			'vier', # 4
			'fünf', # 5
			'sechs', # 6
			'sieben', # 7
			'acht', # 8
			'neun' # 9
		]
		self.teens = [
			'', # 10
			'elf', # 11
			'zwölf', # 12
			'dreizehn', # 13
			'vierzehn', # 14
			'fünfzehn', # 15
			'sechzehn', # 16
			'siebzehn', # 17
			'achtzehn', # 18
			'neunzehn' # 19
		]
		self.tens = [
			'', # 0
			'zehn', # 10
			'zwanzig', # 20
			'dreißig', # 30
			'vierzig', # 40
			'fünfzig', # 50
			'sechzig', # 60
			'siebzig', # 70
			'achtzig', # 80
			'neunzig' # 90
		]
		self.altOne = 'ein'
		self.hundred = 'hundert'
		self.thousand = 'tausend'
	
	def get1(self, i, isNoZero=False, useAltOne=False):
		if isNoZero and i == 0:
			return ''
		if useAltOne and i == 1:
			return self.altOne
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			return self.get1(i, True, useAltOne=True) + 'und' + self.tens[ii]
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i == 0: # 100, 200...
			return self.get1(iii, True, useAltOne=True) + self.hundred
		else: # 101-199, 201-299...
			return self.get1(iii, True, useAltOne=True) + self.hundred + ' ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		else: # >= 1001
			return self.get1(iv, True, useAltOne=True) + self.thousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorIndonesian(NumeralGenerator):
	'''
	Numeral generator for Indonesian
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'indonesian')	
		self.ones = [
			'kosong', # 0
			'satu', # 1
			'dua', # 2
			'tiga', # 3
			'empat', # 4
			'lima', # 5
			'enam', # 6
			'tujuh', # 7
			'delapan', # 8
			'sembilan' # 9
		]
		self.teens = [
			'', # 10
			'sebelas', # 11
			'dua belas', # 12
			'tiga belas', # 13
			'empat belas', # 14
			'lima belas', # 15
			'enam belas', # 16
			'tujuh belas', # 17
			'delapan belas', # 18
			'sembilan belas' # 19
		]
		self.tens = [
			'', # 0
			'sepuluh', # 10
			'dua puluh', # 20
			'tiga puluh', # 30
			'empat puluh', # 40
			'lima puluh', # 50
			'enam puluh', # 60
			'tujuh puluh', # 70
			'delapan puluh', # 80
			'sembilan puluh' # 90
		]
		self.hundred = 'seratus'
		self.hundreds = 'ratus'
		self.thousand = 'seribu'
		self.thousands = 'ribu'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		if ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40 ... 90
			return self.tens[ii]
		else: # >= 21
			return self.tens[ii] + ' ' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		theTens = '' if (ii == 0 and i == 0) else ' ' + self.get10(ii, i, True)
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif iii == 1: # 100-199
			return self.hundred + theTens
		else: # 200+
			return self.get1(iii, True) + ' ' + self.hundreds + theTens

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		theHundreds = '' if (iii == 0 and ii == 0 and i == 0) else ' ' + self.get100(iii, ii, i, True)
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1: # 1001-1999
			return self.thousand + theHundreds
		else: # 2000+
			return self.get1(iv, True) + ' ' + self.thousands + theHundreds

class NumeralGeneratorItalian(NumeralGenerator):
	'''
	Numeral generator for Italian
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'italian')	
		self.ones = [
			'zero', # 0
			'uno', # 1
			'due', # 2
			'tre', # 3
			'quattro', # 4
			'cinque', # 5
			'sei', # 6
			'sette', # 7
			'otto', # 8
			'nove' # 9
		]
		self.teens = [
			'', # 10
			'undici', # 11
			'dodici', # 12
			'tredici', # 13
			'quattordici', # 14
			'quindici', # 15
			'sedici', # 16
			'diciassette', # 17
			'diciotto', # 18
			'diciannove' # 19
		]
		self.tens = [
			'', # 0
			'dieci', # 10
			'venti', # 20
			'trenta', # 30
			'quaranta', # 40
			'cinquanta', # 50
			'sessanta', # 60
			'settanta', # 70
			'ottanta', # 80
			'novanta' # 90
		]
		self.altThree = 'tré'
		self.hundred = 'cento'
		self.thousand = 'mille'
		self.thousands = 'mila'
	
	def get1(self, i, isNoZero=False, useAltThree=False):
		if isNoZero and i == 0:
			return ''
		if useAltThree and i == 3:
			return self.altThree
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			# Need to trim the last vowel from the tens when 1 or 8 is after it
			theTen = self.tens[ii][:-1] if (i == 1 or i == 8) else self.tens[ii]
			return theTen + self.get1(i, True, useAltThree=True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		# Need to trim the last vowel from the hundreds when 80-89 is after it
		theHundred = self.hundred[:-1] if (ii == 8) else self.hundred
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif iii == 1: # 100-199
			return theHundred + self.get10(ii, i, True)
		else: # 200+
			return self.get1(iii, True) + theHundred + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1: # 1001-1999
			return self.thousand + self.get100(iii, ii, i, True)
		else: # 2000+
			return self.get1(iv, True) + self.thousands + self.get100(iii, ii, i, True)

class NumeralGeneratorTagalog(NumeralGenerator):
	'''
	Numeral generator for Tagalog
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'tagalog')	
		self.ones = [
			'wala', # 0
			'isa', # 1
			'dalawa', # 2
			'tatlo', # 3
			'apat', # 4
			'lima', # 5
			'anim', # 6
			'pito', # 7
			'walo', # 8
			'siyam' # 9
		]
		self.teens = [
			'', # 10
			'labing-isa', # 11
			'labindalawa', # 12
			'labintatlo', # 13
			'labing-apat', # 14
			'labinlima', # 15
			'labing-anim', # 16
			'labimpito', # 17
			'labingwalo', # 18
			'labinsiyam' # 19
		]
		self.tens = [
			'', # 0
			'sampu', # 10
			'dalawampu', # 20
			'tatlumpu', # 30
			'apatnapu', # 40
			'limampu', # 50
			'animnapu', # 60
			'pitumpu', # 70
			'walumpu', # 80
			'siyamnapu' # 90
		]
		self.hundred = 'daan'
		self.altHundred = 'raan'
		self.thousand = 'libo'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		if ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19
			return self.teens[i]
		elif i == 0: # 20, 30, 40 ... 90
			return self.tens[ii]
		else: # >= 21
			return self.tens[ii] + '\'t ' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		theOne = self.get1(iii, True)
		theTens = '' if (ii == 0 and i == 0) else ' at ' + self.get10(ii, i, True)
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		if iii == 4 or iii == 6 or iii == 9: # 400, 600, 900
			return theOne + ' na ' + self.altHundred + theTens
		else: # 200+
			return theOne + 'ng ' + self.hundred + theTens
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		theHundreds = '' if (iii == 0 and ii == 0 and i == 0) else '\'t ' + self.get100(iii, ii, i, True)
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		if iv == 4 or iv == 6 or iv == 9: # 4000, 6000, 9000
			return self.get1(iv, True) + ' na ' + self.thousand + theHundreds
		else: # 2000+
			return self.get1(iv, True) + 'ng ' + self.thousand + theHundreds

class NumeralGeneratorTurkish(NumeralGenerator):
	'''
	Numeral generator for Turkish
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'turkish')
		self.ones = [
			'sıfır', # 0
			'bir', # 1
			'iki', # 2
			'üç', # 3
			'dört', # 4
			'beş', # 5
			'altı', # 6
			'yedi', # 7
			'sekiz', # 8
			'dokuz' # 9
		]
		self.tens = [
			'', # 0
			'on', # 1
			'yirmi', # 2
			'otuz', # 3
			'kırk', # 4
			'elli', # 5
			'altmış', # 6
			'yetmiş', # 7
			'seksen', # 8
			'doksan' # 9
		]
		self.oneHundred = 'yüz'
		self.oneThousand = 'bin'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif i == 0:
			return self.tens[ii]
		else:
			return self.tens[ii] + ' ' + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 1:
			return self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1:
			return self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorVietnamese(NumeralGenerator):
	'''
	Numeral generator for Vietnamese
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'vietnamese')
		# 1000 = một nghìn
		# 1001 = một nghìn - không trăm - linh một
		# 1009 = một nghìn - không trăm - linh chín
		# 1010 = một nghìn - không trăm - mười
		# 1020 = một nghìn - không trăm - hai mươi
		# compare with:
		# 1109 = một nghìn - một trăm - linh chín
		# 1110 = một nghìn - một trăm - mười
		# 1120 = một nghìn - một trăm - hai mươi
		self.ones = [
			'không', # 0
			'một', # 1
			'hai', # 2
			'ba', # 3
			'bốn', # 4
			'năm', # 5
			'sáu', # 6
			'bảy', # 7
			'tám', # 8
			'chín' # 9
		]
		self.zeroAlt = 'linh'
		self.oneAlt = 'mốt' # for 21-91
		self.fiveAlt = 'lăm' # for 15-95, e.g. 35 = ba mươi lăm and 535 = năm trăm ba mươi lăm
		self.oneTen = 'mười'
		self.oneTenAlt = 'mươi' # for 20-90
		self.oneHundred = 'trăm'
		self.oneThousand = 'nghìn'

	def get1(self, i, isNoZero=False, isAltOne=False, isAltFive=False):
		if isNoZero and i == 0:
			return ''
		if isAltOne and i == 1:
			return self.oneAlt
		if isAltFive and i == 5:
			return self.fiveAlt
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + ' ' + self.get1(i, True, isAltFive=True)
		else:
			return self.get1(ii, True) + ' ' + self.oneTenAlt + ' ' + self.get1(i, True, isAltOne=True, isAltFive=True)

	def get100(self, iii, ii, i, isNoZero=False, hasZeroOrdinal=False):
		if iii == 0 and not hasZeroOrdinal:
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i != 0:
			return self.get1(iii, not hasZeroOrdinal) + ' ' + self.oneHundred + ' ' + self.zeroAlt + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, not hasZeroOrdinal) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		else:
			isZeroOrdinal = (iii == 0 and not (ii == 0 and i == 0))
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True, hasZeroOrdinal=isZeroOrdinal)
