/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `cafe_blum` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `cafe_blum`;

CREATE TABLE IF NOT EXISTS `clientes` (
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_cedula` int(11) NOT NULL,
  `cliente_nombre` varchar(20) NOT NULL,
  `cliente_apellido` varchar(20) DEFAULT NULL,
  `cliente_numero` varchar(20) DEFAULT NULL,
  `cliente_direccion` text DEFAULT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `divisas` (
  `divisa_id` int(11) NOT NULL AUTO_INCREMENT,
  `divisa_nombre` varchar(20) DEFAULT NULL,
  `divisa_relacion` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`divisa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `facturas` (
  `factura_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) DEFAULT NULL,
  `factura_fecha` date DEFAULT NULL,
  PRIMARY KEY (`factura_id`),
  KEY `FK_facturas_clientes` (`cliente_id`),
  CONSTRAINT `FK_facturas_clientes` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `factura_detalles` (
  `detalles_id` int(11) NOT NULL AUTO_INCREMENT,
  `factura_id` int(11) NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `detalles_total` decimal(20,6) NOT NULL,
  PRIMARY KEY (`detalles_id`),
  KEY `FK_factura_detalles_facturas` (`factura_id`),
  KEY `FK_factura_detalles_divisas` (`divisa_id`),
  CONSTRAINT `FK_factura_detalles_divisas` FOREIGN KEY (`divisa_id`) REFERENCES `divisas` (`divisa_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_detalles_facturas` FOREIGN KEY (`factura_id`) REFERENCES `facturas` (`factura_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_nombre` varchar(20) NOT NULL DEFAULT '0',
  `producto_descripcion` varchar(100) NOT NULL DEFAULT '0',
  `producto_precio` decimal(20,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `roles` (
  `rol_id` int(11) NOT NULL,
  `rol_nombre` int(11) NOT NULL,
  `rol_cambiar_productos` int(11) NOT NULL,
  `rol_eliminar_clientes` int(11) NOT NULL,
  `rol_configuraciones` int(11) NOT NULL,
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci COMMENT='roles';

CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario_id` int(11) NOT NULL,
  `usuario_nombre` int(11) NOT NULL,
  `usuario_clave` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  KEY `FK__roles` (`rol_id`),
  CONSTRAINT `FK__roles` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
