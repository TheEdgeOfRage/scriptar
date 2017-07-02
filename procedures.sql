/*
 * procedures.sql
 * Copyright (C) 2017 pavle <pavle@hydrogen>
 *
 * Distributed under terms of the BSD 2-Clause license.
 */

USE `scriptar`;
DELIMITER $$

CREATE PROCEDURE `createUser`(
    IN p_username VARCHAR(32),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(100),
    IN p_name VARCHAR(100)
)
BEGIN
    IF (SELECT exists(SELECT 1
        FROM Users
        WHERE username = p_username))
        THEN
        SELECT 'Username already exists';
    ELSEIF (SELECT exists(SELECT 1
        FROM Users
        WHERE email = p_email))
        THEN
        SELECT 'Email already exists';
    ELSE
        INSERT INTO Users
        (
            username,
            email,
            password,
            name
        )
        VALUES
        (
            p_username,
            p_email,
            p_password,
            p_name
        );
    END IF;
END $$

CREATE PROCEDURE getUser(IN `p_username` VARCHAR(32), OUT `p_ID` INT, OUT `p_password` VARCHAR(100))
BEGIN
    SELECT ID, password
    INTO p_ID, p_password
    FROM Users
    WHERE username = p_username;
END $$

DELIMITER ;

-- vim:et
