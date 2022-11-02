import datetime as dt

# Get timestamp string
timestamp = dt.datetime.utcnow()
print(timestamp)

# converted into time & date
date = timestamp.strftime("%d/%m/%Y")
time = timestamp.strftime("%H:%M:%S")
print(date, time)
