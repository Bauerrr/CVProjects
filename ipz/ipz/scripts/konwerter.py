# import camelot
# import sys

# import numpy as np
# import pandas as pd
# from zipfile import ZipFile

# # inFile = sys.argv[1]
# # outFile = sys.argv[2]
# #print(inFile.split(".")[-1])
# def convert(inFile, outFile):
#     # try:
#     if inFile.split(".")[-1] == "pdf":
#         tables = camelot.read_pdf(inFile, pages='2,3')
#         print("weszlo")
#         df1 = pd.DataFrame(data=tables[0].df)
#         df2 = pd.DataFrame(data=tables[1].df)
#         df3 = pd.concat([df1, df2[2:]], axis=0, ignore_index=True)
#         df3 = df3.replace('None','0')
#         df3 = df3.iloc[2:,:]
#         df3.columns = ['Player Name', 'Mins Played', 'Total Distance (m)','Top Speed (km/h)','Avg Speed (km/h)',
#                     'High Intensity Activity','Sprints (>25.20 km/h) Dist(m)','Sprints (>25.20 km/h) No',
#                     'HSR (19.81-25.20 km/h) Dist(m)', 'HSR (19.81-25.20 km/h) No', 'Distance (m) 14.41-19.80 km/h',
#                     'Distance (m) 7.21-14.40 km/h', 'Distance (m) 0.73-7.20 km/h', 'Distance (m) <0.72 km/h']
#         df3.iloc[:,2:] = df3.iloc[:,2:].astype(float)
#         outFile = outFile + ".csv"
#         print("weszlo2")
#         df3.to_csv(outFile, sep=';', decimal=',', encoding='utf-8', index=False)
#         print("weszlo3")
#         return outFile
#     elif inFile.split(".")[-1] == "zip":
#         pass
#     else:
#         raise Exception('zły typ pliku')
    # except Exception as err:
    #     print('Błąd: ', err)

# convert('../pdfs/ba2ec8ae559741fbafa6ab3ecb939807.pdf', '../csvs/ba2ec8ae559741fbafa6ab3ecb939807')
