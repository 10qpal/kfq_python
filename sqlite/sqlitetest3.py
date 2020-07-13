import sqlite3, csv

input_file = 'sqlite/input.csv'

conn = sqlite3.connect('sqlite/suppliers.db')
c = conn.cursor()

# 데이터가 들어갈 테이블 생성
sql = '''
CREATE TABLE if not exists suppliers(
    supplier_name varchar(20),
    invoice_number varchar(20),
    part_number varchar(20),
    cost float,
    purchase_date date
)
'''
c.execute(sql)
conn.commit()

sql2 = 'DELETE FROM suppliers'        # 조건 없으면 모든 행 제거
c.execute(sql2)
conn.commit()

# csv 파일에서 데이터를 읽어서 테이블에 INSERT
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')

# 첫 라인을 읽음(제목행)
header = next(file_reader, None)
# print(type(file_reader))      # _csv.reader
print(header)

# header 이후의 2번째 행부터 끝까지 읽어들이며 INSERT
data = []
for row in file_reader:
    # print(type(row))      # list
    data.append(row)
# print(type(data))       # list
print(data)

sql3 = 'INSERT INTO suppliers VALUES (?,?,?,?,?)'
c.executemany(sql3, data)
conn.commit()

c.close()
conn.close()