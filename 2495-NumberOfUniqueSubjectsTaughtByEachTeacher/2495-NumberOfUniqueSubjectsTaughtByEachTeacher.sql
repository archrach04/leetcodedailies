-- Last updated: 3/28/2026, 12:53:55 AM
# Write your MySQL query statement below
select teacher_id , count(distinct(subject_id)) as cnt from Teacher group by teacher_id