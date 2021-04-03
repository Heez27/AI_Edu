from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def findall():
    try:
        #db와 연결
        db = conn()

        # cursor 생성(리스트처럼 생각)
        cursor = db.cursor(DictCursor)

        # SQL 실행(cursor이용)
        sql = 'select no, first_name, last_name, email from emaillist order by no desc'
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error: {e}')

def insert(firstname, lastname, email):
    try:
        #db 연결
        db = conn()

        # cursor 생성(리스트처럼 생각)
        cursor = db.cursor(DictCursor)

        # SQL 실행(cursor이용)
        sql = 'insert into emaillist values(null,%s, %s, %s)'
        count = cursor.execute(sql, (firstname, lastname, email))  # cursor.execute(위의 sql문장, tuple(row)) #바인딩

        # insert, update, delete는 commit 필요
        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        #결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')

def deletebyemail(email2):
    try:
        #db 연결
        db = conn()

        # cursor 생성(리스트처럼 생각)
        cursor = db.cursor(DictCursor)

        print(type(email2))
        # SQL 실행(cursor이용)
        sql = "delete from emaillist where email = %s"
        count = cursor.execute(sql, (email2,))  #위의 sql문장 실행

        # insert, update, delete는 commit 필요
        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        #결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')
def conn(): #db와 연결함수 (참고: 비번 바뀌면 여기서 바꾸면 됨)
    return connect(user='webdb', password='webdb', host='localhost', port=3306, db='webdb', charset='utf8')
