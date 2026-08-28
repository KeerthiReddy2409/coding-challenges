# Write your MySQL query statement below
select person_name from queue
WHERE turn = (
    SELECT MAX(turn)
    FROM (
        SELECT
            turn,
            SUM(weight) OVER (ORDER BY turn) AS tot_weight
        FROM Queue
    ) x
    WHERE tot_weight <= 1000
);