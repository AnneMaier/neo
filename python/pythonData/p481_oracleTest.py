import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series


cx_Oracle.init_oracle_client(lib_dir=r"/usr/local/OracleXE/instantclient_19_26")
plt.rcParams['font.family'] = 'NanumBarunGothic'


conn = None
cur = None

try:
    loginfo = 'hr/1234@192.168.1.144:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    print(type(conn))

    cur = conn.cursor()
    print(type(cur))

    sql = 'select * from country_summary_top_10'
    cur.execute(sql)

    # name = []
    # year = []
    # bindo = []

    # for result in cur:
    #     name.append(result[0])
    #     year.append(result[1])
    #     bindo.append(result[2])
    
    # myseries = Series(bindo, index=year, name=bindo)
    # print(myseries)

    # for idx in range(0,2):
    #     myframe = myseries.unstack(idx)
    #     print(myframe)
    #     myframe.plot(kind='bar', rot=0)
    #     plt.title("3개국 테러 발생 현황")

    #     filename = f'p481_oracleTest.png' 
    #     plt.savefig(filename, dpi=400, bbox_inches='tight')
    #     print(filename + ' saved')
    #     plt.show()

    data = []
    country = []

    for result in cur:
        data.append(result[1])
        country.append(result[0])
        mycolor = ['r', 'g', 'b', 'y', 'm',
            'c', '#FFF0F0', '#CCFFBB', '#05CCFF',
            '#11CCFF']

        chartData = Series(data,index=country)
        chartData.plot(kind='bar', rot=18,color=mycolor, grid=False, title='범죄빈도 Top 10 국가', alpha=0.7)
        plt.ylabel('빈도수', rotation=0)

        filename = 'p481_oracleChart01.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' file saved...')
        plt.show()

        myframe = pd.read_sql(sql, conn, index_col="COUNTRY_TXT")
        print(type(myframe))
        print(myframe)  
    


except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print("finished!")