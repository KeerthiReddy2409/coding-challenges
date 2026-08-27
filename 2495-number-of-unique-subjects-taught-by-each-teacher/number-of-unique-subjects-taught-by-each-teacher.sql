# Write your MySQL query statement below

select teacher_id, count(distinct subject_id) as cnt from teacher group by teacher_id;

-- SELECT teacher_id,
--        COUNT(*) AS cnt
-- FROM (
--     SELECT teacher_id, subject_id
--     FROM Teacher
--     GROUP BY teacher_id, subject_id
-- ) t
-- GROUP BY teacher_id;