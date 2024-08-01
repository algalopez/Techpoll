
-- Basic

USE techpoll;   

SELECT * FROM poll;
SELECT * FROM poll_question;
SELECT * FROM question_options;
SELECT * FROM poll_answer;

SELECT * FROM question_options WHERE question_uuid = 'f823b055-aed9-43e4-b42b-afae0d7d2ed3';
SELECT * FROM poll p JOIN poll_question pq ON p.`uuid`= pq.poll_uuid JOIN question_options qo ON pq.`uuid` = qo.question_uuid;


-- TRUNCATE TABLE poll_answer;




-- Get the latest data sent by all users

SELECT a.*
FROM poll_answer a
JOIN (
    SELECT poll_uuid, question_uuid, MAX(datetime) AS max_datetime
    FROM poll_answer
    GROUP BY poll_uuid, question_uuid
) b
ON a.poll_uuid = b.poll_uuid
AND a.question_uuid = b.question_uuid
AND a.datetime = b.max_datetime
ORDER BY a.poll_uuid, a.question_uuid, a.datetime;