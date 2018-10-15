import helper

def computePerHead(data, columns):
	for row in data:
		count = 0
		for i in range(2, len(row)):
			count = count + 1 if row[i] > 0 else count
		row[-1] = row[1] / count
	return helper.convertToDataframe(data, columns)

def updateExpenditure(data, people):
	for index, row in data.iterrows():
		for person in people:
			if row[person] > 0:
				people[person] = people[person] + row['perHead']
	return people

def main():
	data = helper.getData()
	people=helper.getPeople(data)
	data = computePerHead(data.as_matrix(), data.columns)
	people = updateExpenditure(data, people)
	print(people)

if __name__ == '__main__':
	main()
