-- Last updated: 3/28/2026, 12:54:07 AM
# Write your MySQL query statement below
select A.machine_id, ROUND(AVG(B.timestamp-A.timestamp),3) as processing_time FROM Activity A JOIN ACTIVITY B on A.machine_id=B.machine_id where A.activity_type='start' and B.activity_type='end' and A.process_id=B.process_id group by machine_id