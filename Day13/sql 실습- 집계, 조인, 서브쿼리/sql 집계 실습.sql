#Q1. salaries 테이블에서 현재 전체 직원의 평균급여와 최고급여 출력
select avg(salary), max(salary) 
from salaries 
where to_date = '9999-01-01'; #현재

#Q2. salaries 테이블에서 사번이 10060인 직원의 급여 평균과 총합계를 출력
select avg(salary), sum(salary)
from salaries
where emp_no=10060;

#Q3. 사번이 10060인 직원의 최저 임금을 받은 시기와 최대 임금을 "받은 시기"를 각각 출력
# select 절에 집계합수가 있으면 다른 컬럼은 올수 없다.
# 따라서 "받은 시기"는 조인이나 서브쿼리를 통해서 구해야 한다.
select *
from salaries
where emp_no=10060;

#Q4. dept_emp  테이블에서  d008에 현재 근무하는 인원수는?
select count(*)
from dept_emp
where dept_no = 'd008' and to_date='9999-01-01'; #현재!!

#Q5.각 사원별로 평균연봉 출력
select emp_no, avg(salary)
from salaries
group by emp_no;

#Q6. salaries 테이블에서 현재 전체 직원별로 평균급여가 35000 이상인 
#직원의 평균 급여를 큰 순서로 출력하세요. (***)
select emp_no, avg(salary) 
from salaries
where to_date='9999-01-01'
group by emp_no
having avg(salary)>=35000 #group에 대한 조건은 having절에!(where절x)
order by avg(salary) desc;

#Q7. 사원별로 몇 번의 직책 변경이 있었는지 조회해 보세요.
select emp_no, count(*)
from titles
group by emp_no;

#Q8. 현재 직책별로 직원수를 구하되, 직원수가 100명 이상인 직책만 출력
select title, count(*)
from titles
where to_date = '9999-01-01'
group by title
having count(*)>=100;