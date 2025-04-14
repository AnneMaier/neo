import re

mylist = ['abc123', 'cd4#6', 'ef789a', 'abc1']

regex = '^[a,c]\w{4}'

pattern  = re.compile(regex)

print('# 문자 a , c로 시작하고, 이후에 숫자나 알파벳이 4개로 끝나는 패턴')
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
