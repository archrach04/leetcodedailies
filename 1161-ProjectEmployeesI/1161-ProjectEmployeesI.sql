-- Last updated: 3/28/2026, 12:54:19 AM
# Write your MySQL query statement below
select project_id, round(avg(experience_years),2) as average_years from Project P LEFT JOIN Employee E on P.employee_id=E.employee_id group by p.project_id