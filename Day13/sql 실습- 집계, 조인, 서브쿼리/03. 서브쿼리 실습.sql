#sql 서브쿼리 연습
# Q1. 현재 Fai Bale이 근무하는 부서의 전체 직원의 사번과 이름을 출력하세요.
#sol1) 두 쿼리를 이용하기
select d.dept_no
from employees e join dept_emp d using(emp_no)#이름, 부서
where d.to_date='9999-01-01'
  and e.first_name='Fai'
  and e.last_name='Bale'; #실행결과: 'd004'
  
select e.emp_no, concat(e.first_name, '  ', e.last_name) as name
from employees e join dept_emp d using(emp_no)
where d.to_date='9999-01-01'
  and d.dept_no = 'd004';
  
#sol2) 위 두 쿼리 합치기(단일 행렬이 나와서 가능)
select e.emp_no, concat(e.first_name, '  ', e.last_name) as name
from employees e join dept_emp d using(emp_no)
where d.to_date='9999-01-01'
  and d.dept_no = (select d.dept_no
from employees e join dept_emp d using(emp_no)#이름, 부서
where d.to_date='9999-01-01'
  and e.first_name='Fai'
  and e.last_name='Bale');
  
  

# 참고: where의 조건식에 서브쿼리를 사용하고 결과가 단일행인 경우: =, !=, >, <, >=, <= 이용

#Q2. 현재 전체 사원의 평균 연봉보다 적은 급여를 받는 사원들의 이름, 급여를 출력
select concat(e.first_name, '  ', e.last_name) as name, s.salary
from employees e join salaries s using(emp_no) #사원 이름, 급여
where s.to_date = '9999-01-01'
  and s.salary < (select avg(salary) from salaries where to_date='9999-01-01')
  order by salary desc;
  
  
#참고: where의 조건식에 서브쿼리를 사용하고 결과가 다중행행인 경우: 
-- in(not in)
-- any: =any(in 동일), >any, <any, <>any(!=any), <=any, >=any 
-- all: =all, >all, <all, <>all(!=all, not in), <=all, >=all 이용

#Q3. 현재 급여가 50000 이상인 직원의 이름과 급여를 출력
-- sol1) join using 이용
select concat(e.first_name, '  ', e.last_name) as name, s.salary
from employees e join salaries s using(emp_no) #사원 이름, 급여
where s.to_date = '9999-01-01'
  and s.salary > 50000
order by salary desc; #보기 좋게

-- sol2) subquery 멀티 행/렬: in사용
select concat(e.first_name, '  ', e.last_name) as name, s.salary
from employees e join salaries s using(emp_no) #사원 이름, 급여
where s.to_date = '9999-01-01'
  and (e.emp_no, s.salary) in (select emp_no, salary from salaries where to_date='9999-01-01' and salary>50000)
order by salary desc; #보기 좋게

-- sol3) subquery 멀티 행/렬: =any 사용(in 대신)
select concat(e.first_name, '  ', e.last_name) as name, s.salary
from employees e join salaries s using(emp_no) #사원 이름, 급여
where s.to_date = '9999-01-01'
  and (e.emp_no, s.salary) = any (select emp_no, salary from salaries where to_date='9999-01-01' and salary>50000)
order by salary desc; #보기 좋게

-- sol4) from에 subquery
select concat(a.first_name, '  ', a.last_name) as name, b.salary
from employees a, (select emp_no, salary from salaries where to_date='9999-01-01') b
where a.emp_no = b.emp_no
order by salary desc; #보기 좋게



#Q4. 현재 가장 적은 직책별 평균급여를 구하고 직책과 평균급여를 같이 출력
-- sol1) 가장 적은 걸 고르기 위해, order by와 limit 이용
select t.title, avg(salary)
from titles t join salaries s using (emp_no)
where t.to_date = '9999-01-01' and s.to_date = '9999-01-01'
group by t.title
order by avg(salary) asc #가장 작은것부터 큰 순서대로
limit 0,1; #index 0인 행만 출력

-- sol2) 
# 1.min(avg_salary)라는 단일 행렬 결과가 나오는 쿼리 작성 (현재 가장 적은 직책별 평균급여 구함)
select min(avg_salary) 
from(
select b.title, avg(salary) as avg_salary
from salaries a join titles b using(emp_no)
where a.to_date='9999-01-01' and b.to_date='9999-01-01' 
group by b.title
) a; #every derived table must have its own alias 

#2. 1번에서 구한 가장 적은 평균급여를 having절에서 이용(group by조건 이기 떄문)
select t.title, round(avg(salary)) as avg_salary #참고: round(반올림)해야지 값이 나옴!!
from titles t join salaries s using (emp_no)
where t.to_date = '9999-01-01' and s.to_date = '9999-01-01'
group by t.title
having avg_salary = (
  select min(avg_salary) 
  from(
    select b.title, round(avg(salary)) as avg_salary
    from salaries a join titles b using(emp_no)
    where a.to_date='9999-01-01' and b.to_date='9999-01-01' 
    group by b.title) a);
    
    
    
    
#Q5. 현재, 부서별로 최고급여를 받는 사원의 이름과 급여를 출력해 보세요.

-- 준비: 부서별 최고급여받는 사원번호 받기
select d.dept_no, max(salary) as max_salary
from dept_emp d join salaries s using (emp_no)
where d.to_date = '9999-01-01' and s.to_date = '9999-01-01'
group by d.dept_no;

-- 코드1: from절 subquery 
select b. dept_no, b.max_salary as salary, concat(a.first_name, '  ', a.last_name) as name
from employees a  join (select d.emp_no, d.dept_no, max(salary) as max_salary
                    from dept_emp d join salaries s using (emp_no)
                   where d.to_date = '9999-01-01' and s.to_date = '9999-01-01'
				group by d.dept_no) b using (emp_no)
order by salary desc;

-- 코드2: where절 subquery
select concat(a.first_name, '  ', a.last_name) as name, s.salary
from employees a join salaries s using (emp_no)
where s.to_date = '9999-01-01'
  and s.salary in (select max(salary) as max_salary
                   from dept_emp d join salaries s using (emp_no)
                   where d.to_date = '9999-01-01' and s.to_date = '9999-01-01'
                   group by d.dept_no);
from dept_emp d join salaries s using (emp_no)
where d.to_date = '9999-01-01' and s.to_date = '9999-01-01'
group by d.dept_no

