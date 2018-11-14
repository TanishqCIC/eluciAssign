import pandas as pd
import roundy as rd
from pandas import ExcelWriter

def core(filePath):
	data = pd.ExcelFile(filePath)
	#reading data from  given path

	df = rd.meanCore(filePath)
	#creating dataFrame from meanCore function of Roundy file

	uniqueTime = []
	newTarget = []
	finalArray = []
	#initializing uniqueTime, newTarget and finalArray arrays

	for index in range(0, len(df)):
	#traversing every row of dataFrame

		target = df.iloc[index][1049]
		if target not in uniqueTime:
			uniqueTime.append(target)
	#uniqueTime is list of all unique Rendering Round Off times

	for key in uniqueTime:
	#goes through every unique Rendering time
		newTarget = []
		count = 0
		sum = 0
		newdf = df.drop('m/z', 1)
		newdf = newdf.drop('Retention time (min)', 1)
		newdf = newdf.drop('Accepted Compound ID', 1)
		for index in range(0, len(newdf)):
			target = newdf.iloc[index][len(newdf.columns)-1]
			if target == key:
				newTarget.append(newdf.iloc[index])
		newTarget = pd.DataFrame(newTarget, columns=newdf.columns)
		new = newTarget.iloc[:].mean()
		finalArray.append(new)
	#appends row if rendering time is same as uniqueTime's key

	finalArray = pd.DataFrame(finalArray, columns=newdf.columns)
	#converting arrays to pandas dataFrame

	writer = ExcelWriter('PythonExport.xlsx', engine='xlsxwriter')
	finalArray.to_excel(writer, index=False, startrow=0, startcol=0)
	writer.save()
	#writing Excel Sheet