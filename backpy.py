from pandas import ExcelWriter
import pandas as pd
import json
import os

def findEnd(key):
	tokens = [' PC', 'LPC', 'plasmalogen']
	#initializes tokens array
	for token in tokens:
		tokenLength = len(token)
		if key[-tokenLength:] == token:
			finalToken = token
	#finding if PC / LPC / plasmalogen is present in end of key
	#returning PC / LPC / plasmalogen if present
	return finalToken

def core(filePath):
	pcMat = []
	lpcMat = []
	plasmalogenMat = []
	#initializing pcMat, lpcMat and plasmalogen arrays

	data = pd.ExcelFile(filePath)
	#reading data from  given path

	df = data.parse(data.sheet_names[0])
	#creating dataFrame 

	for index in range(0, len(df)):
	#traversing every row of dataFrame
		
		target = df.iloc[index][2]
		try:
			returnObject = findEnd(target)
			if returnObject == " PC":
				pcMat.append(df.iloc[index])
				#if contains PC in end, add to pcMat
			elif returnObject == "LPC":
				lpcMat.append(df.iloc[index])
				#if contains LPC in end, add to lpcMat
			else:
				plasmalogenMat.append(df.iloc[index])
				#if contains Plasmalogen in end, add to plasmalogenMat
		except:
			pass
	
	pcDF = pd.DataFrame(pcMat, columns=df.columns)
	lpcDF = pd.DataFrame(lpcMat, columns=df.columns)
	plasmalogenDF = pd.DataFrame(plasmalogenMat, columns=df.columns)
	#converting arrays to pandas dataFrame

	writer = ExcelWriter('PythonExport.xlsx', engine='xlsxwriter')
	pcDF.to_excel(writer, index=False, startrow=0, startcol=0, sheet_name="PC_DataFrame")
	lpcDF.to_excel(writer, index=False, startrow=0, startcol=0, sheet_name="LPC_DataFrame")
	plasmalogenDF.to_excel(writer, index=False, startrow=0, startcol=0, sheet_name="Plasmalogen_DataFrame")
	writer.save()
	writer.close()
	#writing Excel Sheets with 3 sheets PC_DataFrame, LPC_DataFrame and Plasmalogen_DataFrame
