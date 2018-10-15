import pandas as pd
import config

def getData():
	if config.DIRECTION == 'local':
		df = pd.read_excel(config.FILE_NAME)
		df['perHead'] = 0
		df = df.fillna(0)
		return df

def convertToDataframe(data, columns):
	data = pd.DataFrame(data)
	data.columns = columns
	return data

def getPeople(data):
	people = {}
	for person in list(data.keys())[2:]:
		people[person] = 0
	return people
