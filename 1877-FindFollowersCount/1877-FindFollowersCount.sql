-- Last updated: 3/28/2026, 12:54:05 AM
# Write your MySQL query statement below
select user_id, count(user_id)as followers_count from Followers group by user_id order by user_id