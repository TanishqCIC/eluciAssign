import pandas as pd
from pandas import ExcelWriter

def core(filePath):
	data = pd.ExcelFile(filePath)
	#reading data from  given path

	df = data.parse(data.sheet_names[0])
	#creating dataFrame 
	
	roundArray = []
	#initializes roundArray array

	for index in range(0, len(df)):
	#traversing every row of dataFrame

		target = df.iloc[index][1]
		newTarget = round(target)
		roundArray.append(newTarget)
		#appending Rounded values in roundArray array

	df['Retention Time Roundoff (in mins)'] = roundArray
	#adding column Retention Time Roundoff (in mins)

	writer = ExcelWriter('PythonExport.xlsx', engine='xlsxwriter')
	df.to_excel(writer, index=False, startrow=0, startcol=0)
	writer.save()
	#writing Excel Sheet

def meanCore(filePath):
	data = pd.ExcelFile(filePath)
	#reading data from  given path

	df = data.parse(data.sheet_names[0])
	#creating dataFrame from meanCore function of Roundy file

	roundArray = []
	#initializes roundArray array

	for i in range(0, len(df)):
		target = df.iloc[i][1]
		newTarget = round(target)
		roundArray.append(newTarget)

	df['Retention Time Roundoff (in mins)'] = roundArray
	#adds another column Retention Time Roundoff

	return df