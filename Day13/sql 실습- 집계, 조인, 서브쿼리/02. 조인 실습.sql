#SQL 조인 실습
#Q1. 현재 근무하고 있는 여직원의 이름과 직책을 직원 이름 순으로 출력하세요.
select concat(first_name,'  ',last_name) as name, t.title
from employees e, titles t 
where e.emp_no = t.emp_no   #join condition
 and t.to_date='9999-01-01' #select condition
 and e.gender = 'F'         #select condition   
order by name;

#Q2. 부서별로 현재 직책이 Engineer인 직원들에 대해서만 평균 급여를 구하세요. 
select d2.dept_name, avg(s.salary)
from salaries s, titles t, dept_emp d, departments d2 #참고: employees 테이블 필요없음!
where s.emp_no = t.emp_no
 and t.emp_no = d.emp_no
 and d.dept_no = d2.dept_no
 and s.to_date='9999-01-01' # select condition (4개의 테이블이라, 3개 조건문 있어야함)
 and t.to_date='9999-01-01'
 and d.to_date='9999-01-01'
 and t.title='Engineer'
group by d2.dept_name;

#Q3. 현재, 직책별로 급여의 총합을 구하되 Engineer 직책은 제외 하세요.
# 단, 총합이 2,000,000,000 이상인 직책만 나타내며 급여총합에 대해서는
# 내림차순(DESC)으로 정렬 하세요.
select t.title, sum(salary)
from titles t, salaries s #직책별, 급여
where t.emp_no = s.emp_no    #join condition
  and t.to_date='9999-01-01' #현재!!
  and s.to_date='9999-01-01'
  and t.title != 'Engineer'
group by t.title
having sum(s.salary)>2000000000
order by sum(s.salary) desc;

#Q4. 현재 근무하고 있는 여직원의 이름과 직책을 직원 이름 순으로 출력
#sol1) join~on 사용
select concat(first_name,' ',last_name) as name, t.title
from employees e join titles t on e.emp_no=t.emp_no #join condition
where t.to_date='9999-01-01'
  and e.gender='F'
order by name;
#sol2) natural join 사용
select concat(first_name,' ',last_name) as name, t.title
from employees e natural join titles t
where t.to_date='9999-01-01' #select condition
  and e.gender='F'			 #select condition
order by name;
#참고: natural join의 문제점: 특정한 칼럼으로만 조인하고 싶을 때
#sol3) join~ using 사용
select concat(first_name,' ',last_name) as name, t.title
from employees e join titles t using (emp_no)
where t.to_date='9999-01-01'
  and e.gender='F'
order by name;

#outer join (left join, right join)생략