
import pandas as pd
import os
import sys


'getcwd:      ', os.getcwd()
osfile, maindir =('__file__:    ', __file__)
filename = os.path.basename(sys.argv[0])
inpath = maindir.replace(filename,"Excels")
outpath = maindir.replace(filename,"BulkFile.xlsx")

for root, dirs, files in os.walk(inpath):
    print(files)
    for f in files:
        path = os.path.join(root, f)
        excelframe = pd.read_excel(path)
        dataframes = [excelframe]
        compactframes = pd.concat(dataframes)
        compactframes.to_excel(outpath)






