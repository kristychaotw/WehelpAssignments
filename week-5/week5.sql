CREATE DATABASE website;
SHOW DATABASES;
USE `website`;
CREATE TABLE `member`(
						`id` BIGINT PRIMARY KEY AUTO_INCREMENT,
						`name` VARCHAR(255) NOT NULL,
						`username` VARCHAR(255) NOT NULL,
						`PassWord` VARCHAR(255) NOT NULL,
						`follower_count` INT NOT NULL DEFAULT 0,
						`time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
DESCRIBE `member`;
SELECT `username` FROM `member`;
SELECT `password` FROM `member`;
INSERT INTO member ( name, username, password ) VALUES ('BB', 'bb', '1234');
INSERT INTO member ( name, username, password ) VALUES ('CC', 'cc', '5678');
INSERT INTO member ( name, username, password ) VALUES ('DD', 'dd', '0000');
INSERT INTO member ( name, username, password ) VALUES ('EE', 'ee', '1200');

SELECT * FROM `member`
ORDER BY `time` DESC;

SELECT * FROM `member`
ORDER BY `time` DESC
LIMIT 1,3;

SELECT * FROM `member`
WHERE username = 'test';

SELECT * FROM `member`
WHERE username = 'test' AND password = 'test';

SELECT * FROM `member`;

SET sql_safe_updates = 0;

UPDATE `member`
SET name='test2'
WHERE username ='test';

-- 原本follower都是零看不出算式效果，所以cc塞入200的值
UPDATE `member`
SET follower_count=200
WHERE name ='CC';

SELECT * FROM member;
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;

