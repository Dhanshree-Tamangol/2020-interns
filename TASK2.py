import json
from dateutil import parser
import matplotlib.pyplot as plot 
with open('data.json') as file:
    data=json.load(file)    
t1=parser.parse('2019-01-01')
t2=parser.parse('2019-01-31')
date=[]
price_INR=[]
price_GBP=[]
for i in data['rates']:
    t3=parser.parse(i)
    if t3<=t2 and t3>=t1:
        date.append(i)
        price_INR.append(data['rates'][i]['INR'])
        price_GBP.append(data['rates'][i]['GBP'])
m=list(zip(date,price_INR,price_GBP))
r=sorted(m,key=lambda x:x[0])
date=[]
price_INR=[]
price_GBP=[]
date,price_INR,price_GBP=zip(*r)
plot.barh(date,price_INR,color='0.65',label='INR',)
plot.barh(date,price_GBP,color='g',label='GBP')
plot.xlabel('Rates from 1 Jan 2019 to 31 Jan 2019')
plot.xticks(rotation=0)
plot.ylabel('Dates of Jan 2019')
plot.title('INR and GBP against EUR')
plot.legend(loc='lower right')
plot.get_current_fig_manager().window.state('zoomed')
plot.show()