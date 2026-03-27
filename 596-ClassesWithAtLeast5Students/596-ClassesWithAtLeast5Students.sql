-- Last updated: 3/28/2026, 12:54:32 AM
# Write your MySQL query statement below
select class from Courses group by class having count(student)>=5
