#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:41:02 2023

@author: fujidai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:15:57 2023

@author: fujidai
"""

with open('/Users/fujidai/WMT22nodata/wmt22-news-systems/humaneval/DA/newstest2022-toen/ad-seg-scores-cs-en.csv', 'r') as f:# pseudo-pseudo-english　と　english の　cos_sim 　（en-jaのnegative-cossim）

    raberu = f.read()
raberu_lines = raberu.splitlines()#改行コードごとにリストに入れている
#print(raberu_lines)
#(len(raberu_lines))
data = []
for i in range(len(raberu_lines)):
    data.append(raberu_lines[i])#Negative en-ja cos_simをdataに入れている
    
    
twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'CUNI-DocTransformer.6'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'JDExploreAcademy.8'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-W.2'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-Y.4'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Lan-Bridge.1'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-B.0'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-G.9'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'SHOPLINE-PL.5'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'Online-A.10'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'CUNI-Transformer.7'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))




twice=[]
sw=[]
aq=[]
az=[]
for i in range(len(raberu_lines)):

    if 'ALMAnaCH-Inria.3'==data[i].split(" ")[0]:#なんの翻訳機なの指定

        aq.append(data[i].split(" ")[2])#スコアをリストに入れている
        #az.append(data[i].split(" ")[1])
        az.append(float(data[i].split(" ")[1]))#何番目の文章なのかが入っている
        sw.append(data[i].split(" "))

sukoanobasyo_aru = sorted(az, reverse=False)#sukoanobasyo_aru

strii = (sukoanobasyo_aru)

de=[]

for j in range(0,1449):# 元々のｓｒｃの文の個数に合わせる必要がある

    for k in range(len(sw)):

        if str(j)==sw[k][1]:
            print(sw[k][2])#ここがスコア
            #print(sw[k][1])
            de.append(sw[k][2])#個数確認よう


#print(len(de))









