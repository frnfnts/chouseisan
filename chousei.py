import datetime

s = "2023/11/11"
d = "2023/12/1"
s_format = "%Y/%m/%d"
sd = datetime.datetime.strptime(s, s_format)
dd = datetime.datetime.strptime(d, s_format)

i = 0
while sd <= dd:
    print(sd.strftime('%-m/%-d(%a)'))
    sd += datetime.timedelta(days=1)
    i += 1
    if i >= 100:
        break
