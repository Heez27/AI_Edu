#mysql 데이터베이스 연결 + insert

from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor


try:
    db = connect(user = 'webdb', password='webdb', host='localhost', port=3306, db='webdb', charset='utf8')
    print('ok')

    #cursor 생성(리스트처럼 생각)
    cursor = db.cursor(DictCursor)

    #SQL 실행(cursor이용)
    sql = 'insert into emaillist values(17, "Lee","jia", "jia@gmail.com")'
    count = cursor.execute(sql) #몇개 삽입

    #결과 받아오기
    results = cursor.fetchall()


    #insert, update, delete는 commit 필요
    #commit
    db.commit()

    #자원 정리
    cursor.close()
    db.close()

    #결과 보기
    print(f'실행결과: {count == 1}')

except OperationalError as e:
    print(f'error: {e}')