from datetime import datetime
import pytz  #pip install pytz
from tzlocal import get_localzone  #pip install tzlocal

tz_n = pytz.timezone('America/New_York')
datetime_n = datetime.now(tz_n)
print(f'New York Time: {datetime_n.strftime('%H:%M:%S')}')

print('-'*25)

tz_l = pytz.timezone('Europe/London')
datetime_l = datetime.now(tz_l)
print(f'London Time: {datetime_l.strftime('%H:%M:%S')}')

print('-'*25)

tz_india = get_localzone()
print(f'Current Timezone: {tz_india}')
datetime_i = datetime.now(tz_india)
print(f'Indian Time: {datetime_i.strftime('%H:%M:%S')}')

