# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:58:12 2018

@author: wd
"""
import codecs
import xlwt

def search(keywords ='Screen brightnesses' ,filename = './bugreport.txt'):
    result = []
    dark = ''
    dim = ''
    brightness = ''
    medium = ''
    file = codecs.open(filename,'r','utf-8')
    lines = file.readlines()
    num = len(lines)
    for i in range(num):
        if lines[i].find(keywords) != (-1):
            result.append(lines[i+1].replace('\n','').strip())
            if  lines[i+1].find("dim")!=(-1) or lines[i+1].find("dark")!=(-1) or lines[i+1].find("bright")!=(-1) or lines[i+1].find("medium")!=(-1):
                dark = lines[i+1].replace('\n','').strip()
            if  lines[i+2].find("dim")!=(-1) or lines[i+2].find("dark")!=(-1) or lines[i+2].find("bright")!=(-1) or lines[i+2].find("medium")!=(-1):
                dim = lines[i+2].replace('\n','').strip() 
            if  lines[i+3].find("dim")!=(-1) or lines[i+3].find("dark")!=(-1) or lines[i+3].find("bright")!=(-1) or lines[i+3].find("medium")!=(-1):
                brightness = lines[i+3].replace('\n','').strip()
            if  lines[i+4].find("dim")!=(-1) or lines[i+4].find("dark")!=(-1) or lines[i+4].find("bright")!=(-1) or lines[i+4].find("medium")!=(-1):
                medium = lines[i+4].replace('\n','').strip()
            book = xlwt.Workbook(encoding='utf-8',style_compression=0)#创建一个workbook
            sheet = book.add_sheet('bugreport',cell_overwrite_ok=True)#添加一个sheet，命名‘bugreport’
            sheet.write(0,0,lines[i].replace('\n','').strip())#（0,0）和（0,1）是坐标
            if dark == '' and dim == '' and brightness == '' and medium == '':
                sheet.write(0,1,'no value');
            else:
                sheet.write(0,1,dark + "\n"+ dim + "\n"+  brightness + "\n"+ medium);
            book.save('bug.xls')
    return result
result = search()
if len(result) :
    print("success")
else:
    print("fail")
