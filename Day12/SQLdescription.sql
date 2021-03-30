#select를 가장 간단히 사용하게 되면 table의 모든 데이터를 가져오게 됨
select * from employees;

#where 절을 이용해, 테이블에서 특정 row만 가져올 수 있다. (and, or 등과 함께 사용가능)
select * from employees where hire_date > '1999-11-21' and gender = "F";

#결과를 정렬하고 싶을 때는,  ORDER BY 절을 사용한다. (역순정렬 할 때는 DESC를 붙임)
select * from employees where hire_date > '1999-11-21' and gender = "F" order by hire_date desc;

#Null은 빈 값 또는 알 수없는 값임. 비교연산자(=, <, > 등)은 사용안되고, IS NULL 그리고  IS NOT NULL 연산자를 사용. 
select first_name from employees where hire_date is null;

#LIKE or NOT LIKE 비교 연산자를 사용해서 패턴매칭을 함. 기본적으로 영문자인 경우 대소문자 구별을 안함
#특수문자: _  는 한문자, % 여러문자열과 대응
select * from employees where first_name like "K%i"; #이름이 K로 시작, i로 끝나는 직원 조회
select * from employees where first_name like "_____"; #이름이 5글자인 직원 조회

#row counting: count()함수 사용(null이 아닌 결과의 수만 셈)
select count(*) from employees;

#distinct: 중복행을 제거
#alias: 나타날 컬럼에 대한 다른 이름 부여
#한글을 넣을땐, ""넣어주는게 좋음
select first_name as '이름', gender as '성별', hire_date as '입사일' from employees;
select distinct gender from employees;

#문자열 결합함수 concat 사용
select concat(first_name, '  ', last_name) as name from employees;

#between A and B 과 in
select * from employees where hire_date between '1990-01-01' and '1997-01-01'; #아래와 같은 문장
select * from employees where hire_date in ('1990-01-01' ,'1997-01-01');

#Upper(Ucase, 대문자로 만들어줌)와 Lower(Lcase, 소문자로 만들어줌)
#ucase('Employees')