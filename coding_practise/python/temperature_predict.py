import numpy as np
import datetime,time
from sklearn.linear_model import LinearRegression

# dummy inputs (one day)
data=[10.0,11.1,12.3,13.2,14.8,15.6,16.7,17.5,18.9,19.7,20.7,21.1,22.6,23.5,24.9,25.1,26.3,27.8,28.8,29.6,30.2,31.6,32.1,33.7]
startDate = '2013-01-01'
endDate = '2013-01-01'
p = 1
n = 1


x = np.array(range(len(data)))

lm = LinearRegression()
lm.fit(np.array(x).reshape(-1,1), data)


z = np.array(range(24, 50))
lm.predict(np.array(z).reshape(-1,1))








#####################################
###########################################
startDate = '2013-01-01'
endDate = '2013-01-01'
knownTimestamps = ['2013-01-01 07:00', '2013-01-01 08:00', '2013-01-01 09:00', '2013-01-01 10:00',
                      '2013-01-01 11:00', '2013-01-01 12:00']
humidity = [10.0, 11.1, 13.2, 14.8, 15.6, 16.7]
timestamps= ['2013-01-01 13:00', '2013-01-01 14:00']

datetime.datetime.strptime(knownTimestamps[0],"%Y-%m-%d %H:%M")
        

z = timestamps

x = [int(abs((
        datetime.datetime.utcfromtimestamp(0) - 
        datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")
        ).total_seconds())) for item in knownTimestamps]
y = humidity

lm = LinearRegression()
lm.fit(np.array(x).reshape(-1,1), humidity)

z = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in timestamps]
lm.predict(np.array(z).reshape(-1,1))



