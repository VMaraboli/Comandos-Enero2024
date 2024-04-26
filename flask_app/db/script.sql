-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_proyecto_individual
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_proyecto_individual` ;

-- -----------------------------------------------------
-- Schema esquema_proyecto_individual
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_proyecto_individual` DEFAULT CHARACTER SET utf8 ;
USE `esquema_proyecto_individual` ;

-- -----------------------------------------------------
-- Table `esquema_proyecto_individual`.`tipo_usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_proyecto_individual`.`tipo_usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_proyecto_individual`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_proyecto_individual`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `telefono` INT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tipo_usuario` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_usuario_tipo_usuarios1_idx` (`tipo_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_usuario_tipo_usuarios1`
    FOREIGN KEY (`tipo_usuario`)
    REFERENCES `esquema_proyecto_individual`.`tipo_usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_proyecto_individual`.`servicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_proyecto_individual`.`servicios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_servicio` VARCHAR(255) NULL,
  `valor` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_proyecto_individual`.`citas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_proyecto_individual`.`citas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `estado` VARCHAR(45) NULL,
  `fecha` DATETIME NULL,
  `hora` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `servicio_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_appointments_servicios1_idx` (`servicio_id` ASC) VISIBLE,
  CONSTRAINT `fk_appointments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_proyecto_individual`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_appointments_servicios1`
    FOREIGN KEY (`servicio_id`)
    REFERENCES `esquema_proyecto_individual`.`servicios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
