SELECT
    s.id,
    COALESCE(s2.student, s.student) AS student
FROM Seat s
LEFT JOIN Seat s2
    ON s2.id = CASE
                  WHEN MOD(s.id, 2) = 1 THEN s.id + 1
                  ELSE s.id - 1
               END
ORDER BY s.id;