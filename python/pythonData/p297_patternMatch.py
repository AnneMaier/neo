import re

mylist = ['abc123', 'cd456', 'ef789', 'abc12']

regex = '[a-z]{2}\d{3}'

pattern  = re.compile(regex)

print('# 문자열 2개, 숫자 3개 패턴 찾기')
totallist = []
for item in mylist:
    match = pattern.search(item)
    if match:
        print("'%s' 은 조건에 적합." % item)
        totallist.append(item)
    else:
        print("'%s' 은 조건에 부적합." % item)
print("\n # 조건에 적합한 항목들!")        
print(totallist)
