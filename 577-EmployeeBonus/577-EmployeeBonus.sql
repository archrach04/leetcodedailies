-- Last updated: 3/28/2026, 12:54:35 AM
# Write your MySQL query statement below
select E.name, B.bonus FROM EMPLOYEE E LEFT JOIN BONUS B ON E.empId=B.empId where B.bonus<1000 or B.empId is null
