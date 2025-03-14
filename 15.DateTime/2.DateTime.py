from datetime import datetime


n = datetime.now()
print(n)

current_time = n.strftime('%H:%M:%S')
print(f'Current Time: {current_time}')

current_date = n.date()
print(f'Current Date: {current_date}')

