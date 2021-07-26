# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:27:49 2021

@author: 愛場　隆之
"""

import sympy
import numpy as np

def main():
    mode=int(input("操作を選択してください 1:暗号化・複合化　2:複合鍵生成"))
    
    if mode==1:
        code()
    elif mode==2:
        make_decode_key()
            

def code():
    key=make_key()
    data=[]
    temp=[]
    size=[]
    code=[]
    word=0
    rist=0     
    i=0
    j=0
    count=0
    mod=0

    while word!="end":
        
        word=(input("数値を入力してください、「end」で入力終了"))
                
        """数字が入力されたときのみリストに追加"""
        if word.isdigit()==True:
            temp.append(int(word))
            rist=rist+1
            print("odd_",rist) 
            
            if rist%2==0:
                data.append(temp)
                
                temp=[]
            
    if rist%2!=0:
        temp.append(0)
        data.append(temp)
        temp=[]
        rist=rist+1
        
    print(key)
    print(data)
    
    mod=int(input("mod?="))
    
    while i<rist//2:
        code.append((key[0][0]*data[i][0]+key[0][1]*data[i][1])%mod)
        code.append((key[1][0]*data[i][0]+key[1][1]*data[i][1])%mod)
        i=i+1
        
    print(code)
    
        



def make_key():
    a=int(input("a=?"))
    b=int(input("a=?"))
    c=int(input("a=?"))
    d=int(input("a=?"))
    key=[[a,b],[c,d]]
    arraykey=np.array(key)
    arraykey=arraykey.reshape(2,2)
            
   
    return key


def make_decode_key():
    code=[[0,0],[0,0]]
    a=int(input("a=?"))
    b=int(input("b=?"))
    c=int(input("c=?"))
    d=int(input("d=?"))
    data=[[a,b],[c,d]]
    print(data)
    mod=int(input("mod?="))
    ans=(data[0][0]*data[1][1]-data[0][1]*data[1][0])%mod
    print("ans=",ans)
    anser=[0,0,0]
    anser=sympy.gcdex(ans,mod)
    anser=anser[0]%mod
    print("anser=",anser)
    
    code[0][0]=(anser*data[1][1])%mod
    code[1][1]=(anser*data[0][0])%mod
    code[0][1]=(anser*data[0][1]*-1)%mod
    code[1][0]=(anser*data[1][0]*-1)%mod
    
    print(code[0])
    print(code[1])


main()