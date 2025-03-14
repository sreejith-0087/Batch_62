import time

t = time.localtime()
print(t)

print('-------------------')

# 0-Year, 1-Month, 2-dayofmonth, 3-hour, 4-Min, 5-Sec, 6-weekday, 7-dayofyear

print(f'Current Time: {t[3]}:{t[4]}:{t[5]}')
print(f'Current Date: {t[2]}/{t[1]}/{t[0]}')
