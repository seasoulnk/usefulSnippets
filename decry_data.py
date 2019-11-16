#!/bin/bash
import pandas as pd
import zipfile


zf = zipfile.ZipFile("./data.zip")
xlsfiles = zf.infolist()
for xlsfile in xlsfiles:
    print(xlsfile.filename)
    df = pd.read_excel(zf.open(xlsfile, "r", pwd=bytes('tp9068','utf-8')))
    print(df)
