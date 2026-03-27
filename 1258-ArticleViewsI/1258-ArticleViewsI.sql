-- Last updated: 3/28/2026, 12:54:17 AM
# Write your MySQL query statement below
select distinct(author_id) as id from Views where viewer_id=author_id order by author_id