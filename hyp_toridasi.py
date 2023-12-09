#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:56:21 2023

@author: fujidai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:15:57 2023

@author: fujidai
"""

with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/humaneval/DA/newstest2022-toen/ad-seg-scores-cs-en.csv', 'r') as f:# pseudo-pseudo-english　と　english の　cos_sim 　（en-jaのnegative-cossim）
#with open('/Users/fujidai/WMT22nodata/ad-seg-scores-ja-en.csv', 'r') as f:# pseudo-pseudo-english　と　english の　cos_sim 　（en-jaのnegative-cossim）

    raberu = f.read()
raberu_lines = raberu.splitlines()#改行コードごとにリストに入れている
#print(raberu_lines)
#(len(raberu_lines))
data = []
for i in range(len(raberu_lines)):
    data.append(raberu_lines[i])#Negative en-ja cos_simをdataに入れている
    
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'CUNI-DocTransformer.6'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.CUNI-DocTransformer.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'JDExploreAcademy.8'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.JDExploreAcademy.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-W.2'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Online-W.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-Y.4'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Online-Y.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Lan-Bridge.1'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Lan-Bridge.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-B.0'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Online-B.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-G.9'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Online-G.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'SHOPLINE-PL.5'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.SHOPLINE-PL.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-A.10'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.Online-A.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'CUNI-Transformer.7'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.CUNI-Transformer.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))




aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'ALMAnaCH-Inria.3'==data[i].split(" ")[0]:

        aq.append(data[i].split(" ")[0])

        az.append(float(data[i].split(" ")[1]))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

sukoanobasyo_nai = []
for num in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
    if num not in sukoanobasyo_aru:
        sukoanobasyo_nai.append(num)


with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/txt/system-outputs/generaltest2022.cs-en.hyp.ALMAnaCH-Inria.en', 'r') as f:
    raberu2 = f.read()
raberu_lines2 = raberu2.splitlines()#改行コードごとにリストに入れている

xc=[]
for j in range (len(sukoanobasyo_aru)):
    for k in range(1, 1449):# 元々のｓｒｃの文の個数に合わせる必要がある
        if sukoanobasyo_aru[j]==k:
            print(raberu_lines2[k-1])#ここで文取り出し


            xc.append(raberu_lines2[k-1])#個数確認よう
#print(len(xc))











