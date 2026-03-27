-- Last updated: 3/28/2026, 12:54:30 AM
# Write your MySQL query statement below
select * from Cinema where description <> 'boring' and (id%2)=1 order by rating desc