# First call a datetime library in Python
# Secondly create a variable calling function now() in the library.
from datetime import datetime
now = datetime.now()

print now.day
print now.month
print now.year

# Output not well format, isn't it ?=>
'''
12
2
2018
'''
# **Hot date**

# Return print the current date as mm/dd/yyyy
print '%s/%s/%s' % (now.month, now.day, now.year)
# Return print the current date as dd/mm/yyyy
print '%s/%s/%s' % (now.day, now.month, now.year)

# **Pretty Time **
# Format hh:mm:ss.
print '%s:%s:%s' % (now.hour, now.minute, now.second)

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.

print 'Today is : %s/%s/%s It\'s: %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
# Output => Today is : 2018/2/12 It's: 13:54:11