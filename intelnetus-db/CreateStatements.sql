-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema scopus
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema scopus
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `scopus` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `scopus` ;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_authors` (
  `ID` VARCHAR(40) NOT NULL,
  `Scopus_ID` VARCHAR(15) NULL DEFAULT NULL,
  `ORCID_ID` VARCHAR(20) NULL DEFAULT NULL,
  `First_Name` VARCHAR(50) NULL DEFAULT NULL,
  `Last_Name` VARCHAR(50) NULL DEFAULT NULL,
  `Fields_Of_Study` VARCHAR(5000) NULL DEFAULT NULL,
  `Affiliations` VARCHAR(5000) NULL DEFAULT NULL,
  `hIndex` INT NULL DEFAULT NULL,
  `Citations_Count` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `Scopus_ID` (`Scopus_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `scopus`.`scopus_organizations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_organizations` (
  `ID` VARCHAR(40) NOT NULL,
  `Scopus_ID` VARCHAR(15) NULL DEFAULT NULL,
  `Name` VARCHAR(600) NULL DEFAULT NULL,
  `Type_1` VARCHAR(15) NULL DEFAULT NULL,
  `Type_2` VARCHAR(25) NULL DEFAULT NULL,
  `Address` VARCHAR(270) NULL DEFAULT NULL,
  `City` VARCHAR(50) NULL DEFAULT NULL,
  `Country` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `Scopus_ID` (`Scopus_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_authors_organizations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_authors_organizations` (
  `Author_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Organization_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Year` INT NULL DEFAULT NULL,
  UNIQUE INDEX `Author_ID` (`Author_ID` ASC, `Organization_ID` ASC, `Year` ASC) VISIBLE,
  INDEX `Organization_ID` (`Organization_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_authors_organizations_ibfk_1`
    FOREIGN KEY (`Author_ID`)
    REFERENCES `scopus`.`scopus_authors` (`ID`),
  CONSTRAINT `scopus_authors_organizations_ibfk_2`
    FOREIGN KEY (`Organization_ID`)
    REFERENCES `scopus`.`scopus_organizations` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_authors_variants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_authors_variants` (
  `Variant_1_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Variant_2_ID` VARCHAR(40) NULL DEFAULT NULL,
  UNIQUE INDEX `Variant_1_ID` (`Variant_1_ID` ASC, `Variant_2_ID` ASC) VISIBLE,
  INDEX `Variant_2_ID` (`Variant_2_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_authors_variants_ibfk_1`
    FOREIGN KEY (`Variant_1_ID`)
    REFERENCES `scopus`.`scopus_authors` (`ID`),
  CONSTRAINT `scopus_authors_variants_ibfk_2`
    FOREIGN KEY (`Variant_2_ID`)
    REFERENCES `scopus`.`scopus_authors` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_publications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_publications` (
  `ID` VARCHAR(40) NOT NULL,
  `DOI` VARCHAR(50) NULL DEFAULT NULL,
  `Year` VARCHAR(4) NULL DEFAULT NULL,
  `Title` VARCHAR(510) NULL DEFAULT NULL,
  `Journal` VARCHAR(510) NULL DEFAULT NULL,
  `Abstract` VARCHAR(5000) NULL DEFAULT NULL,
  `Keywords` VARCHAR(681) NULL DEFAULT NULL,
  `Fields` VARCHAR(400) NULL DEFAULT NULL,
  `Fields_Abbreviations` VARCHAR(100) NULL DEFAULT NULL,
  `Citations_Count` INT NULL DEFAULT NULL,
  `Number_Of_Authors` INT NULL DEFAULT NULL,
  `Number_Of_Affiliations` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `DOI` (`DOI` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_organizations_variants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_organizations_variants` (
  `Variant_1_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Variant_2_ID` VARCHAR(40) NULL DEFAULT NULL,
  UNIQUE INDEX `Variant_1_ID` (`Variant_1_ID` ASC, `Variant_2_ID` ASC) VISIBLE,
  INDEX `Variant_2_ID` (`Variant_2_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_organizations_variants_ibfk_1`
    FOREIGN KEY (`Variant_1_ID`)
    REFERENCES `scopus`.`scopus_organizations` (`ID`),
  CONSTRAINT `scopus_organizations_variants_ibfk_2`
    FOREIGN KEY (`Variant_2_ID`)
    REFERENCES `scopus`.`scopus_organizations` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_publications_authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_publications_authors` (
  `Publication_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Author_ID` VARCHAR(40) NULL DEFAULT NULL,
  INDEX `Publication_ID` (`Publication_ID` ASC) VISIBLE,
  INDEX `Author_ID` (`Author_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_publications_authors_ibfk_1`
    FOREIGN KEY (`Publication_ID`)
    REFERENCES `scopus`.`scopus_publications` (`ID`),
  CONSTRAINT `scopus_publications_authors_ibfk_2`
    FOREIGN KEY (`Author_ID`)
    REFERENCES `scopus`.`scopus_authors` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_publications_organizations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_publications_organizations` (
  `Publication_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Organization_ID` VARCHAR(40) NULL DEFAULT NULL,
  UNIQUE INDEX `Publication_ID` (`Publication_ID` ASC, `Organization_ID` ASC) VISIBLE,
  INDEX `Organization_ID` (`Organization_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_publications_organizations_ibfk_1`
    FOREIGN KEY (`Publication_ID`)
    REFERENCES `scopus`.`scopus_publications` (`ID`),
  CONSTRAINT `scopus_publications_organizations_ibfk_2`
    FOREIGN KEY (`Organization_ID`)
    REFERENCES `scopus`.`scopus_organizations` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `scopus`.`scopus_publications_variants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scopus`.`scopus_publications_variants` (
  `Variant_1_ID` VARCHAR(40) NULL DEFAULT NULL,
  `Variant_2_ID` VARCHAR(40) NULL DEFAULT NULL,
  UNIQUE INDEX `Variant_1_ID` (`Variant_1_ID` ASC, `Variant_2_ID` ASC) VISIBLE,
  UNIQUE INDEX `Variant_1_ID_2` (`Variant_1_ID` ASC, `Variant_2_ID` ASC) VISIBLE,
  INDEX `Variant_2_ID` (`Variant_2_ID` ASC) VISIBLE,
  CONSTRAINT `scopus_publications_variants_ibfk_1`
    FOREIGN KEY (`Variant_1_ID`)
    REFERENCES `scopus`.`scopus_publications` (`ID`),
  CONSTRAINT `scopus_publications_variants_ibfk_2`
    FOREIGN KEY (`Variant_2_ID`)
    REFERENCES `scopus`.`scopus_publications` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
