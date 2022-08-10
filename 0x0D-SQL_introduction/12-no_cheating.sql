-- change Bob score to 10
SELECT `name`, `score` FROM `second_table`
INSERT INTO `second_table` (`score`)
VALUES ('10') WHERE `name` = 'Bob'
ORDER BY `score` DESC;