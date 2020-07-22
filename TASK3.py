import json
from dateutil import parser
import matplotlib.pyplot as plot 
with open('data.json') as file:
    data=json.load(file)
with open('latest-rates.json') as file1:
    lat=json.load(file1)    

t1=parser.parse('2019-01-01')
t2=parser.parse('2019-01-31')

x_c=0 
date=[]
price_INR=[]
price_GBP=[]

for i in data['rates']:
    t3=parser.parse(i)
    if t3<=t2 and t3>=t1:
        date.append(i)
        price_INR.append(data['rates'][i]['INR'])
        price_GBP.append(data['rates'][i]['GBP'])
        x_c+=1
m=list(zip(date,price_INR,price_GBP))
r=sorted(m,key=lambda x: x[0])
date.clear()
price_INR.clear()
price_GBP.clear()
date,price_INR,price_GBP=zip(*r)
a=max(price_INR)
b=max(price_GBP)
y_coord=max(a,b)
plot.bar(date,price_INR,color='0.65',label='INR',width=0.5)
plot.bar(date,price_GBP,label='GBP',width=0.5)
plot.annotate('Current INR rate-'+str(lat['rates']['INR']),(x_c-20,y_coord),textcoords='offset points',xytext=(0,40),ha='center')
plot.annotate('Current GBP rate-'+str(lat['rates']['GBP']),(x_c-20,y_coord),textcoords='offset points',xytext=(0,30),ha='center')
plot.xlabel('Dates of Jan 2019')
plot.xticks(rotation=33)
plot.ylabel('Rates from 1 Jan 2019 to 31 Jan 2019')
plot.title('INR and GBP against EUR')
plot.legend()
plot.get_current_fig_manager().window.state('zoomed')
plot.show()