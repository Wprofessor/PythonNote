import pprint
message = 'It was a bright cold day in April,and the colocks were striking thirteen.'
count = {}
for cha in message:
    count.setdefault(cha,0)        #如果该键不存在，则添加该键且赋值为0
    count[cha] += 1

pprint.pprint(count)                #按键排序输出
print(pprint.pformat(count))        #和第7行等价