# 課表到 Google Calendar CSV

## timeline.py

用於生成秋季和夏季不同的作息時間表

Usage:

`python timeline.py 開始日期 結束日期 第一節開始-結束 第二節開始到結束 ....`

秋季學期跨年處理，開始日期寫今年，結束日期寫明年，timeline.py 只會讀取月和日。

例如：

    python timeline.py 'Oct 1 2013' 'Apr 30 2014' '08:00-09:40' '10:10-11:50' '14:00-15:35' '15:55-17:30' '18:30-21:50' > timeline_hust
    python timeline.py 'May 1' 'Sep 30' '08:00-09:40' '10:10-11:50' '14:30-16:05' '16:25-18:00' '19:00-22:20' >> timeline_hust

## generate-csv.py 用來生成日曆 csv

Usage:

`python generate-csv.py 作息時間 課表 '第一週第一天' 假期調休表 輸出文件`

例如：

`python generate-csv.py data/timeline_hust input.txt 'Sep 1 2013' data/vocation_switch out.csv`

課表文件格式：

每行一個

週-週 星期 節 教室 課程

之間用 \t 分割


## LICENSE:

Apache License 2.0
