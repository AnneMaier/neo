import json 

def get_Json_data():
    filename = 'jumsu.json'
    myfile = open(filename, 'r', encoding='utf-8')
    print(type(myfile))
    print(myfile)
    print("-" * 50)

    myfile = myfile.read()
    print(type(myfile))
    print(myfile)
    print("-" * 50)

    json_data = json.loads(myfile)
    print(type(json_data))
    print(json_data)
    print("-" * 50)

    for oneitem in json_data:
        print(oneitem.keys())
        print(oneitem.values())
        print("-" * 50)
        kor = float(oneitem['kor'])
        eng = float(oneitem['eng'])
        math = float(oneitem['math'])
        total = kor + eng + math
        print('국어 : ', kor)
        print('영어 : ', eng)
        print('수학 : ', math)
        print('총합 : ', total)
        print("-" * 50)



if __name__ == '__main__':
    get_Json_data()

    