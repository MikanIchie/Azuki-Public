#改行コード特定システム
#Backslash-N Positioning System
#Ver. 0.1 R2/3/20
######環境######
import re
######Environment######

#座標
def bnlocate(sp):
    bnf=re.finditer('\n',sp)
    bn=[]
    for bs in bnf:
        bn.append(bs.start())
    return bn

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
