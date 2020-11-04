#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:32:16 2019

@author: qiangqiangfan
"""

from tkinter import *
import numpy as np
from numpy import *
import numpy.matlib
import numpy
import tkinter.messagebox
from tkinter.filedialog import *
import csv

top=Tk()
top.title('Normal2.0')
top.geometry('500x500')


y_mean=Entry()
y_mean.place(x=190,y=1,width=100,height=30)
Label(text='输入均值(x):',font=("Arial",12)).place(x=100,y=5)

x_sd=Entry()
x_sd.place(x=190,y=50,width=100,height=30)
Label(text='输入标准差(SD):',font=("Arial",12)).place(x=100,y=55)

x_digital=Entry()
x_digital.place(x=200,y=95,width=35,height=25)
Label(text='小数位数（0-3）:',font=("Arial",12)).place(x=100,y=100)

x_n=Entry()
x_n.place(x=300,y=95,width=50,height=25)
Label(text='例数(N):',font=("Arial",12)).place(x=250,y=100)

t=Text()

t.place(x=50,y=180,width=380,height=300)

def new_data():
   
    new_std=float(x_sd.get())
    new_mean=float(y_mean.get())
    new_digitals=int(x_digital.get())
    new_n=int(x_n.get())
    randomx=np.round(new_std*numpy.matlib.randn(new_n,1)+new_mean,new_digitals)
    x_mean=randomx.mean()
    x_std=randomx.std()
    deta_mean=abs(x_mean-new_mean)
    deta_std=abs(x_std-new_std)

    erro_digitals=1/power(10,new_digitals+1)
    mean_result= deta_mean<erro_digitals
    std_result= deta_std<erro_digitals
    result= mean_result and std_result
    global i
    i=0
    t.delete(1.0,tkinter.END)
    while (not result):
        i=i+1
        randomx=np.round(new_std*numpy.matlib.randn(new_n,1)+\
                         new_mean,new_digitals)
        x_mean=randomx.mean()
        x_std=randomx.std()
        deta_mean=abs(x_mean-new_mean)
        deta_std=abs(x_std-new_std)
        mean_result= deta_mean<erro_digitals
        std_result= deta_std<erro_digitals
        result= mean_result and std_result
        t.insert(INSERT, '-')
        
    if(i<1001):
        t.insert(INSERT,'\n在')
        t.insert(INSERT, i )
        t.insert(INSERT,'次运算之后，终于完成了\n')
        t.insert(INSERT,'均值为')
        t.insert('insert',np.round(randomx.mean(),new_digitals) )
    
        t.insert(INSERT,'\t标准差为:')
        t.insert('insert',np.round(randomx.std(),new_digitals) )
    
        t.insert(INSERT,'\t最大值为:')
        t.insert('insert',np.round(randomx.max(),new_digitals) )
    
        t.insert(INSERT,'\t最小值为:')
        t.insert('insert',np.round(randomx.min(),new_digitals) )
        t.insert(INSERT,'\n')
        messagebox.showinfo(message="数据已生成，保存为data.csv")
        
    else:
        messagebox.showinfo(message="已经运行了1000次，还未找到合适的参数，\
                            建议检查输入是否有误")
    
    randomy=array(randomx)
    with open('data.csv','w') as f:
        f_csv=csv.writer(f)
        f_csv.writerows(randomy)
  
b1=Button(text='Enter',command=new_data)
b1.place(x=200,y=130,width=65,height=35)

mainloop()
