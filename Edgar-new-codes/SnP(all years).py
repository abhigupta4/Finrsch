import requests
from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

SP = {'1158449': 'AAP', '10456': 'BAX', '1530721': 'KORS', '352541': 'LNT', '1378946': 'PBCT', '73124': 'NTRS', '1162328': 'PFG', '1260221': 'TDG', '899866': 'ALXN', '36104': 'USB', '915389': 'EMN', '949039': 'DO', '1038357': 'PXD', '872589': 'REGN', '73309': 'NUE', '20286': 'CINF', '1365135': 'WU', '1035002': 'VLO', '72971': 'WFC', '1467373': 'ACN', '1451505': 'RIG', '85961': 'R', '821189': 'EOG', '1393744': 'ES', '21665': 'CL', '1041557': 'FRT', '59478': 'LLY', '1168054': 'XEC', '933136': 'WM', '1555280': 'ZTS', '64670': 'MDT', '29915': 'DOW', '42582': 'GT', '1324404': 'CF', '759944': 'CFG', '858877': 'CSCO', '27904': 'DAL', '50863': 'INTC', '1090012': 'DVN', '354950': 'HD', '858470': 'COG', '1467858': 'GM', '350698': 'AN', '728535': 'JBHT', '0001156039': 'ANTM', '72903': 'XEL', '20520': 'FTR', '78814': 'PBI', '916365': 'TSCO', '920522': 'ESS', '1040971': 'SLG', '315189': 'DE', '764478': 'BBY', '1026304': 'T', '1050915': 'PWR', '10795': 'BDX', '319201': 'KLAC', '40987': 'GPC', '51434': 'IP', '1418135': 'DPS', '104169': 'WMT', '6201': 'AAL', '891554': 'ADI', '754737': 'SCG', '1170010': 'KMX', '936340': 'DTE', '1037540': 'BXP', '884905': 'PX', '912242': 'MAC', '45012': 'HAL', '1571949': 'ICE', '915913': 'ALB', '1031296': 'FE', '0000039899': 'TGNA', '919482': 'TAP', '1393311': 'PSA', '55785': 'KMB', '884887': 'RCL', '1065088': 'EBAY', '100517': 'UAL', '927628': 'COF', '791907': 'LLTC', '0000865752': 'MNST', '30554': 'DD', '1492633': 'NLSN', '859737': 'HOLX', '1326801': 'FB', '791519': 'SPLS', '1136893': 'FIS', '0001564708': 'NWSA', '316709': 'SCHW', '1004434': 'AMG', '56873': 'KR', '1496048': 'GGP', '277948': 'CSX', '1524472': 'XYL', '914208': 'IVZ', '1174922': 'WYNN', '764180': 'MO', '1037038': 'RL', '797468': 'OXY', '91419': 'SJM', '1534701': 'PSX', '97745': 'TMO', '1410636': 'AWK', '718877': 'ATVI', '1156375': 'CME', '1043277': 'CHRW', '1124198': 'FLR', '40704': 'GIS', '47217': 'HPQ', '750556': 'STI', '1526520': 'TRIP', '1364742': 'BLK', '816761': 'TDC', '1636023': 'WRK', '1107565': 'O', '36270': 'MTB', '313616': 'DHR', '68505': 'MSI', '773840': 'HON', '46765': 'HP', '1275283': 'RAI', '31462': 'ECL', '1373835': 'SE', '20171': 'CB', '109198': 'TJX', '1396009': 'VMC', '0001646383': 'CSRA', '0001604778': 'QRVO', '1135152': 'FTI', '354908': 'FLIR', '882095': 'GILD', '707549': 'LRCX', '1359841': 'HBI', '77360': 'PNR', '1166691': 'CMCSA', '1164727': 'NEM', '107263': 'WMB', '885725': 'BSX', '1090727': 'UPS', '1067701': 'URI', '49826': 'ITW', '908255': 'BWA', '1002910': 'AEE', '935703': 'DLTR', '1090872': 'A', '833444': 'TYC', '0001140536': 'WLTW', '875045': 'BIIB', '103379': 'VFC', '804753': 'CERN', '946115': 'TGT', '35527': 'FITB', '38777': 'BEN', '58492': 'LEG', '39911': 'GPS', '1140859': 'ABC', '1012100': 'SEE', '12659': 'HRB', '704051': 'LM', '9389': 'BLL', '0001339947': 'VIAB', '1105705': 'TWX', '1100962': 'ENDP', '793952': 'HOG', '31791': 'PKI', '49071': 'HUM', '80661': 'PGR', '28412': 'CMA', '1390777': 'BK', '29534': 'DG', '1137789': 'STX', '1041061': 'YUM', '1121788': 'GRMN', '0001336917': 'UA', '1132694': 'IRM', '1144215': 'AYI', '63908': 'MCD', '1551182': 'ETN', '1385157': 'TEL', '47111': 'HSY', '916076': 'MLM', '1000228': 'HSIC', '63754': 'MKC', '1099219': 'MET', '1058290': 'CTSH', '1004980': 'PCG', '818479': 'XRAY', '106535': 'WY', '217346': 'TXT', '877890': 'CTXS', '813828': 'CBS', '54480': 'KSU', '898173': 'ORLY', '713676': 'PNC', '0000064040': 'SPGI', '773910': 'APC', '1567892': 'MNK', '829224': 'SBUX', '37785': 'FMC', '96223': 'LUK', '1101215': 'ADS', '109380': 'ZION', '55067': 'K', '1048695': 'FFIV', '717423': 'MUR', '106640': 'WHR', '310158': 'MRK', '1086222': 'AKAM', '203077': 'STJ', '62996': 'MAS', '812074': 'OI', '203527': 'VAR', '0000315293': 'AON', '1288776': 'GOOG', '1623613': 'MYL', '18230': 'CAT', '860730': 'HCA', '0000794367': 'M', '866787': 'AZO', '53669': 'JCI', '1403161': 'V', '1002047': 'NTAP', '64803': 'CVS', '63276': 'MAT', '9892': 'BCR', '1110803': 'ILMN', '1070750': 'HST', '798354': 'FISV', '731766': 'UNH', '75362': 'PCAR', '1437107': 'DISCA', '30625': 'FLS', '1022079': 'DGX', '14272': 'BMY', '723531': 'PAYX', '1141391': 'MA', '827052': 'EIX', '922224': 'PPL', '920760': 'LEN', '827054': 'MCHP', '1015780': 'ETFC', '745732': 'ROST', '850693': 'AGN', '1120193': 'NDAQ', '909832': 'COST', '0000865436': 'WFM', '93556': 'SWK', '51143': 'IBM', '93410': 'CVX', '57139': 'LB', '899051': 'ALL', '98246': 'TIF', '29989': 'OMC', '769397': 'ADSK', '1056239': 'LLL', '1058090': 'CMG', '766421': 'ALK', '59558': 'LNC', '0001652044': 'GOOGL', '1532063': 'ESRX', '4904': 'AEP', '766704': 'HCN', '1123360': 'GPN', '831259': 'FCX', '26172': 'CMI', '879101': 'KIM', '21344': 'KO', '1065280': 'NFLX', '89800': 'SHW', '24741': 'GLW', '1065696': 'LKQ', '820313': 'APH', '1084750': 'NAVI', '732712': 'VZ', '49196': 'HBAN', '927066': 'DVA', '1324424': 'EXPE', '79879': 'PPG', '1111711': 'NI', '1103982': 'MDLZ', '886158': 'BBBY', '0001659166': 'FTV', '1000697': 'WAT', '885639': 'KSS', '4977': 'AFL', '1358071': 'CXO', '48465': 'HRL', '352915': 'UHS', '65984': 'ETR', '1297996': 'DLR', '886982': 'GS', '4281': 'AA', '78239': 'PVH', '861878': 'SRCL', '4127': 'SWKS', '1137774': 'PRU', '1045810': 'NVDA', '100493': 'TSN', '315213': 'RHI', '1099800': 'EW', '50104': 'TSO', '899689': 'VNO', '77476': 'PEP', '1024124': 'TRV', '1051470': 'CCI', '1082114': 'L', '1043604': 'JNPR', '1021860': 'NOV', '1035267': 'ISRG', '796343': 'ADBE', '912615': 'URBN', '701221': 'CI', '740260': 'VTR', '1408146': 'EMC', '746515': 'EXPD', '1564708': 'NWS', '1087423': 'RHT', '8818': 'AVY', '318154': 'AMGN', '1001039': 'DIS', '315852': 'RRC', '100885': 'UNP', '1053507': 'AMT', '1013871': 'NRG', '851968': 'MHK', '723254': 'CTAS', '814453': 'NWL', '72207': 'NBL', '1633917': 'PYPL', '1014473': 'VRSN', '1551152': 'ABBV', '32604': 'EMR', '4447': 'HES', '6951': 'AMAT', '753308': 'NEE', '882184': 'DHI', '1138118': 'CBG', '320187': 'NKE', '0001308161': 'FOXA', '1274494': 'FSLR', '72333': 'JWN', '743988': 'XLNX', '87347': 'SLB', '66740': 'MMM', '33185': 'EFX', '60667': 'LOW', '1585364': 'PRGO', '1001250': 'EL', '1281761': 'RF', '899881': 'PLD', '702165': 'NSC', '875159': 'XL', '922864': 'AIV', '356028': 'CA', '891024': 'PDCO', '92380': 'LUV', '896878': 'INTU', '875320': 'VRTX', '850209': 'FL', '1011006': 'YHOO', '62709': 'MMC', '816284': 'CELG', '101778': 'MRO', '51253': 'IFF', '7332': 'SWN', '1018724': 'AMZN', '1109357': 'EXC', '1133421': 'NOC', '320193': 'AAPL', '37996': 'F', '1413329': 'PM', '1442145': 'VRSK', '12927': 'BA', '715957': 'D', '1285785': 'MOS', '804328': 'QCOM', '2969': 'APD', '849399': 'SYMC', '316206': 'HOT', '800459': 'HAR', '70858': 'BAC', '313927': 'CHD', '1289490': 'EXR', '5272': 'AIG', '1068002': 'FOX', '895421': 'MS', '354190': 'AJG', '78003': 'PFE', '0001136869': 'ZBH', '46080': 'HAS', '40545': 'GE', '1115222': 'DNB', '1047862': 'ED', '202058': 'HRS', '0001437107': 'DISCK', '1059556': 'MCO', '5513': 'UNM', '21076': 'CLX', '34088': 'XOM', '765880': 'HCP', '29905': 'DOV', '1063761': 'SPG', '1519751': 'FBHS', '764622': 'PNW', '1579241': 'ALLE', '91440': 'SNA', '874761': 'AES', '200406': 'JNJ', '874766': 'HIG', '1113169': 'TROW', '40533': 'GD', '940944': 'DRI', '1060391': 'RSG', '92122': 'SO', '832988': 'SIG', '1163165': 'COP', '1137411': 'COL', '1393612': 'DFS', '1130310': 'CNP', '18926': 'CTL', '4962': 'AXP', '912750': 'NFX', '906107': 'EQR', '320335': 'TMK', '1024478': 'ROK', '1601712': 'SYF', '723125': 'MU', '794323': 'LVLT', '101829': 'UTX', '1108524': 'CRM', '895126': 'CHK', '1075531': 'PCLN', '808362': 'BHI', '93751': 'STT', '106040': 'WDC', '92230': 'BBT', '108772': 'XRX', '19617': 'JPM', '1361658': 'WYN', '1071739': 'CNC', '721371': 'CAH', '1341439': 'ORCL', '96021': 'SYY', '822416': 'PHM', '1510295': 'MPC', '6769': 'APA', '721683': 'TSS', '927653': 'MCK', '1110783': 'MON', '831001': 'C', '1506307': 'KMI', '0001645590': 'HPE', '1430602': 'SNI', '16732': 'CPB', '811156': 'CMS', '1649338': 'AVGO', '277135': 'GWW', '1116132': 'COH', '1326160': 'DUK', '789019': 'MSFT', '52988': 'JEC', '7084': 'ADM', '882835': 'ROP', '788784': 'PEG', '51644': 'IPG', '1489393': 'LYB', '76334': 'PH', '310764': 'SYK', '815097': 'CCL', '1267238': 'AIZ', '1403568': 'ULTA', '920148': 'LH', '74208': 'UDR', '1452575': 'MJN', '8670': 'ADP', '33213': 'EQT', '815556': 'FAST', '1048286': 'MAR', '23217': 'CAG', '1122304': 'AET', '0001618921': 'WBA', '712515': 'EA', '1521332': 'DLPH', '1037868': 'AME', '1032208': 'SRE', '915912': 'AVB', '91576': 'KEY', '80424': 'PG', '16918': 'STZ', '0001637459': 'KHC', '1800': 'ABT', '1101239': 'EQIX', '936468': 'LMT', '1039684': 'OKE', '1048911': 'FDX', '820027': 'AMP', '97476': 'TXN', '1466258': 'IR', '1047122': 'RTN', '783325': 'WEC'}

def get_file(cur):
	base = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		if 'Archives' in link.get("href"):
			return (base+link.get("href"))
			break


def take_second_link(cur,cik):
	begin = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		temp = link.get("href")
		if 'edgar' in temp and 'index' in temp and 'headers' not in temp:
			fir = (begin + str(temp))
			break

	sec = ''
	for link in links:
		temp = link.get("href")
		if '.xlsx' in temp:
			sec = temp
			break

	return [fir, sec]	

def find_details(entire):
	begin = 'https://www.sec.gov/Archives/edgar/data/'
	for part in entire:
		if 'edgar' in part:
			temp = part.split('/')
			last = ''
			for ele in temp[-1]:
				if ele.isdigit():
					last += ele
	new = begin + temp[-2] + '/' + last
	for i in range(len(entire)):
		if 'edgar' in entire[i]:
			break

	for j in range(i-1,0,-1):
		if  entire[j] != '':
			break

	return [new,temp[-2],entire[j]]

def inside_index(link1, pref):
	r = requests.get(pref+link1)
	document = BeautifulSoup(r.content,"lxml")
	soup = document.get_text()
	lines = soup.split("\n")
	flag = 1
	for line in lines:
		# print(line)
		temp = line.split(" ")
		for i in range(len(temp)):
			if temp[i] == '10-Q' or temp[i] == '10-K' and temp[i-1] == '' and temp[i+1] == '':
				quarter = '2' #Take quarter from here
				
				new, name, filing = find_details(temp) 
				#Take name and filing data from here
				if name not in SP:
					break

				new_li, financial = take_second_link(new, temp[-2])
				# Take excel link from here
				
				docu = get_file(new_li) 
				#This will be url variable
				
				html = request.urlopen(docu).read().decode('utf8')  
				# This is unstripped text
				
				raw = BeautifulSoup(html,"lxml").get_text()  
				# This is actual text
				
				tokens = tokenizer.tokenize(raw)   
				#This is the tokens variable
				# Call your function here
				break
		
tokenizer = RegexpTokenizer(r'\w+')

main_link = 'https://www.sec.gov/Archives/edgar/daily-index/'

for year in range(2011,2018):
	for q in range(1,5):
		cur_link = main_link + str(year) + '/QTR' + str(q) + '/'
		# print(cur_link)
		try:
			r = requests.get(cur_link)

			document = BeautifulSoup(r.content,"lxml")
			links = document.find_all('a')
			for link in links:
				if 'company' in link.get("href") and '.idx' in link.get("href"):
					inside_index(link.get("href"), cur_link)
		except:
			pass
			