-- MySQL Script generated by MySQL Workbench
-- Sun 29 Jan 2017 01:28:36 AM CET
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema scriptar
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `scriptar` ;

-- -----------------------------------------------------
-- Schema scriptar
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `scriptar` DEFAULT CHARACTER SET utf8 ;
USE `scriptar` ;

-- -----------------------------------------------------
-- Table `scriptar`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Users` (
`ID` INT NOT NULL AUTO_INCREMENT,
`username` VARCHAR(32) NOT NULL,
`email` VARCHAR(255) NOT NULL,
`password` VARCHAR(100) NOT NULL,
`create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`name` VARCHAR(100) NULL DEFAULT '',
UNIQUE INDEX `username_UNIQUE` (`username` ASC),
UNIQUE INDEX `email_UNIQUE` (`email` ASC),
PRIMARY KEY (`ID`),
UNIQUE INDEX `user_ID_UNIQUE` (`ID` ASC));


-- -----------------------------------------------------
-- Table `scriptar`.`Subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Subjects` (
`ID` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(100) NOT NULL DEFAULT '',
PRIMARY KEY (`ID`),
UNIQUE INDEX `subject_ID_UNIQUE` (`ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scriptar`.`Scripts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Scripts` (
`ID` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(100) NOT NULL DEFAULT '',
`link` VARCHAR(500) NULL DEFAULT NULL,
`create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`description` BLOB NULL,
`User_ID` INT NULL,
`Subject_ID` INT NULL,
PRIMARY KEY (`ID`),
UNIQUE INDEX `script_ID_UNIQUE` (`ID` ASC),
INDEX `fk_Script_User_idx` (`User_ID` ASC),
INDEX `fk_Script_Subject1_idx` (`Subject_ID` ASC),
CONSTRAINT `fk_Script_User`
FOREIGN KEY (`User_ID`)
REFERENCES `scriptar`.`Users` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Script_Subject1`
FOREIGN KEY (`Subject_ID`)
REFERENCES `scriptar`.`Subjects` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scriptar`.`Reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Reviews` (
`ID` INT NOT NULL AUTO_INCREMENT,
`rating` INT NOT NULL,
`comment` BLOB NULL,
`create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`Script_ID` INT NULL,
`User_ID` INT NULL,
PRIMARY KEY (`ID`),
UNIQUE INDEX `review_ID_UNIQUE` (`ID` ASC),
INDEX `fk_Review_Script1_idx` (`Script_ID` ASC),
INDEX `fk_Review_User1_idx` (`User_ID` ASC),
CONSTRAINT `fk_Review_Script1`
FOREIGN KEY (`Script_ID`)
REFERENCES `scriptar`.`Scripts` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Review_User1`
FOREIGN KEY (`User_ID`)
REFERENCES `scriptar`.`Users` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scriptar`.`Course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Courses` (
`ID` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(100) NOT NULL DEFAULT '',
`faculty` VARCHAR(100) NOT NULL DEFAULT '',
`city` VARCHAR(50) NOT NULL DEFAULT '',
`country` VARCHAR(50) NOT NULL DEFAULT '',
PRIMARY KEY (`ID`),
UNIQUE INDEX `course_ID_UNIQUE` (`ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scriptar`.`Course_has_Subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scriptar`.`Course_has_Subject` (
`Course_ID` INT NULL,
`Subject_ID` INT NOT NULL,
PRIMARY KEY (`Course_ID`, `Subject_ID`),
INDEX `fk_Course_has_Subject_Subject1_idx` (`Subject_ID` ASC),
INDEX `fk_Course_has_Subject_Course1_idx` (`Course_ID` ASC),
CONSTRAINT `fk_Course_has_Subject_Course1`
FOREIGN KEY (`Course_ID`)
REFERENCES `scriptar`.`Courses` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Course_has_Subject_Subject1`
FOREIGN KEY (`Subject_ID`)
REFERENCES `scriptar`.`Subjects` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

