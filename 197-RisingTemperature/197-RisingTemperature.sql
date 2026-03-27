-- Last updated: 3/28/2026, 12:55:01 AM
# Write your MySQL query statement b
select W1.id from Weather W1 JOIN Weather W2 ON DATEDIFF(W1.recordDate, W2.recordDate)=1 where W1.temperature>W2.temperature