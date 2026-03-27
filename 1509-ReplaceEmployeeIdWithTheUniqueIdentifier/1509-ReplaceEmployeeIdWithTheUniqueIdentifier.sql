-- Last updated: 3/28/2026, 12:54:12 AM
# Write your MySQL query statement below
select EU.unique_id,E.name from Employees E LEFT JOIN EmployeeUNI EU ON EU.id=E.id