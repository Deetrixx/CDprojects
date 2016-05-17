#getting current time and date
from datetime import datetime
now=datetime.now()
print now

#extracting information
from datetime import datetime
now=datetime.now()
current_year=now.year
current_month=now.month
current_day=now.day

print now.year
print now.month
print now.day

#Hot Date
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

#pretty time
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)
