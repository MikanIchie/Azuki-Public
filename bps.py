#改行コード特定システム
#Backslash-N Positioning System
#Ver. 0.1 R2/3/20
######環境######
import re
import fitz
######Environment######
#PDFインプット
def pdf(file):
    f=fitz.open(file)
    v=''
    for x in range(0,len(f)):
        p=f.loadPage(x)
        v=v+p.getText()
    f.close()
    return v
#PDF inputter

#すべての改行コードを特定
def bnlocate(pdfvalue):
    bnf=re.finditer('\n',pdfvalue)
    bn=[]
    for bs in bnf:
        bn.append(bs.start())
    return bn
#Locate every \n in the given values

#改行コードに基づいて文字例を検索
def bnfind(words,string,bn,end=None):
    bn=bn
    keyf=re.finditer(words,string)
    key=[]
    
    for k in keyf:
        key.append(k.end())
    bnk=[]
    if end==True:
        for k in range(0,len(key)):
            for l in range(0,len(bn)):
                if bn[l-1]<key[k] and bn[l]>key[k]:
                    bnk.append(l)
                elif bn[l]==key[k]:
                    bnk.append(l)
    else:
        for k in range(0,len(key)):
            for l in range(0,len(bn)):
                if bn[l]<key[k] and bn[l+1]>key[k]:
                    bnk.append(l)
                elif bn[l]==key[k]:
                    bnk.append(l)
    return bnk
#Find any words based on the position of \n

#通常取得した位置を改行コード位置に変換
def bntrans(key,string,bn,end=None):
    bn=bn
    key=key
    bnk=[]
    if end==True:
        for k in range(0,len(key)):
            for l in range(0,len(bn)):
                if bn[l-1]<key[k] and bn[l]>key[k]:
                    bnk.append(l)
                elif bn[l]==key[k]:
                    bnk.append(l)
    else:
        for k in range(0,len(key)):
            for l in range(0,len(bn)):
                if bn[l]<key[k] and bn[l+1]>key[k]:
                    bnk.append(l)
                elif bn[l]==key[k]:
                    bnk.append(l)
    return bnk
#Transform normal position to BPS position