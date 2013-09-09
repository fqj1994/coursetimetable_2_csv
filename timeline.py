#!/usr/bin/env
from dateutil import parser
from datetime import timedelta
from sys import argv
start_date = parser.parse(argv[1])
end_date = parser.parse(argv[2])

for i in range((end_date - start_date).days + 1):
    now_date = start_date + timedelta(days=i)
    for j in range(3, len(argv)):
        p = j - 2
        start_time, end_time = map(parser.parse, argv[j].split('-'))
        print now_date.month, now_date.day, p, start_time.hour, start_time.minute, end_time.hour, end_time.minute
