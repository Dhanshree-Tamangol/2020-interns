import json
from dateutil import parser
import matplotlib.pyplot as plot 
with open('data.json') as file:
    data = json.load(file)   
t1=parser.parse('2019-01-01')
t2=parser.parse('2019-01-31')
dates=[]
price=[]
for i in data['rates']:
    t3=parser.parse(i)
    if t3<=t2 and t3>=t1:
        dates.append(i)
        price.append(data['rates'][i]['INR'])
m=list(zip(dates,price))
r=sorted(m,key=lambda x:x[0])
dates=[]
price=[]
dates,price = zip(*r)
print("Open Graph window in Full Screen mode")
plot.scatter(dates,price,color='orange',alpha=0.7)
plot.xlabel('Dates of Jan 2019')
plot.xticks(rotation=33)
plot.ylabel('Rates from 1 Jan 2019 to 31 Jan 2019')
plot.title('INR against EUR')
plot.get_current_fig_manager().window.state('zoomed')
plot.show()