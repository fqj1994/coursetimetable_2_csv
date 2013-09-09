#!/usr/bin/env python
import csv
from dateutil import parser
from datetime import timedelta, datetime
import sys

timeline = open(sys.argv[1]).read().split('\n')
if timeline[-1] == '':
    timeline = timeline[:-1]
timeline = [map(int, a.split(' ')) for a in timeline]

course = open(sys.argv[2]).read().split('\n')
if course[-1] == '':
    course = course[:-1]
course = [a.split('\t') for a in course]

first_day_in_the_first_week = parser.parse(sys.argv[3]) - timedelta(days=7)

switch_vocation = open(sys.argv[4], 'r').read().split('\n')
if switch_vocation[-1] == '':
    switch_vocation = switch_vocation[:-1]
switch_vocation = [map(int, i.split(' ')) for i in switch_vocation]


f = csv.writer(open(sys.argv[5], 'wb'))
f.writerow(['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location'])

for i in course:
    week_start, week_end = map(int, i[0].split('-'))
    for week in range(week_start, week_end + 1):
        today = first_day_in_the_first_week + timedelta(days=7 * week + int(i[1]))
        for k in switch_vocation:
            if k[0] == today.year and k[1] == today.month and k[2] == today.day:
                if k[3] == 0:
                    today = None
                    break
                else:
                    today = datetime(k[3], k[4], k[5])
                    break
        if not today:
            continue
        today_str = '-'.join(map(str, [today.year, today.month, today.day]))
        today_schedule = None
        for k in timeline:
            if k[0] == today.month and k[1] == today.day and k[2] == int(i[2]):
                today_schedule = k
                break
        if not today_schedule:
            print 'ERROR'
            sys.exit(1)
        today_start_time_str = ':'.join(map(lambda p: '%02d' % (p), today_schedule[3:5]))
        today_end_time_str = ':'.join(map(lambda p: '%02d' % (p), today_schedule[5:7]))
        f.writerow([i[4], today_str, today_start_time_str, today_str, today_end_time_str, i[3]])

