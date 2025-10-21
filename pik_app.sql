-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: pik_app
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basics`
--

DROP TABLE IF EXISTS `basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basics` (
  `type` varchar(100) DEFAULT NULL,
  `srlNmb` varchar(100) DEFAULT NULL,
  `FN` int(100) NOT NULL,
  `mode` varchar(100) DEFAULT NULL,
  `GPSdt` datetime DEFAULT NULL,
  `VEMDfd` varchar(100) DEFAULT NULL,
  `GPSfd` varchar(100) DEFAULT NULL,
  `fd` varchar(100) DEFAULT NULL,
  `n1cycles` int(11) DEFAULT NULL,
  `n2cycles` int(11) DEFAULT NULL,
  `NRol` float DEFAULT NULL,
  `TRQol` float DEFAULT NULL,
  `Engol` float DEFAULT NULL,
  PRIMARY KEY (`FN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basics`
--

LOCK TABLES `basics` WRITE;
/*!40000 ALTER TABLE `basics` DISABLE KEYS */;
/*!40000 ALTER TABLE `basics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `clientID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pass` varchar(50) DEFAULT NULL,
  `company` int(11) DEFAULT NULL,
  PRIMARY KEY (`clientID`),
  KEY `company` (`company`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`company`) REFERENCES `company` (`compID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `compID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`compID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faildata`
--

DROP TABLE IF EXISTS `faildata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faildata` (
  `code` varchar(100) DEFAULT NULL,
  `FN` int(100) DEFAULT NULL,
  `occurrences` int(11) DEFAULT NULL,
  `n1r` float DEFAULT NULL,
  `n1l` float DEFAULT NULL,
  `nrr` float DEFAULT NULL,
  `nrl` float DEFAULT NULL,
  `n2r` float DEFAULT NULL,
  `n2l` float DEFAULT NULL,
  `t4a` float DEFAULT NULL,
  `t4b` float DEFAULT NULL,
  `oatr` float DEFAULT NULL,
  `oatl` float DEFAULT NULL,
  `tot1` float DEFAULT NULL,
  `tot2` float DEFAULT NULL,
  `tot3` float DEFAULT NULL,
  `tot4` float DEFAULT NULL,
  `trq1` float DEFAULT NULL,
  `trq2` float DEFAULT NULL,
  `trq3` float DEFAULT NULL,
  `trq4` float DEFAULT NULL,
  `po1` float DEFAULT NULL,
  `po2` float DEFAULT NULL,
  `po3` float DEFAULT NULL,
  `po4` float DEFAULT NULL,
  `genc1` int(11) DEFAULT NULL,
  `genc2` int(11) DEFAULT NULL,
  `genc3` int(11) DEFAULT NULL,
  `genc4` int(11) DEFAULT NULL,
  `bv1` float DEFAULT NULL,
  `bv2` float DEFAULT NULL,
  `bv3` float DEFAULT NULL,
  `bv4` float DEFAULT NULL,
  `startc` int(11) DEFAULT NULL,
  KEY `fk_faildata_failure_code` (`code`),
  KEY `FN` (`FN`),
  CONSTRAINT `faildata_ibfk_1` FOREIGN KEY (`FN`) REFERENCES `basics` (`FN`),
  CONSTRAINT `fk_faildata_failure_code` FOREIGN KEY (`code`) REFERENCES `failure` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faildata`
--

LOCK TABLES `faildata` WRITE;
/*!40000 ALTER TABLE `faildata` DISABLE KEYS */;
/*!40000 ALTER TABLE `faildata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `failure`
--

DROP TABLE IF EXISTS `failure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `failure` (
  `code` varchar(100) NOT NULL,
  `descr` varchar(255) DEFAULT NULL,
  `comp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `failure`
--

LOCK TABLES `failure` WRITE;
/*!40000 ALTER TABLE `failure` DISABLE KEYS */;
/*!40000 ALTER TABLE `failure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `helicopter`
--

DROP TABLE IF EXISTS `helicopter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `helicopter` (
  `SerialNumber` int(11) NOT NULL,
  `owner` int(11) DEFAULT NULL,
  PRIMARY KEY (`SerialNumber`),
  KEY `owner` (`owner`),
  CONSTRAINT `helicopter_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `company` (`compID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `helicopter`
--

LOCK TABLES `helicopter` WRITE;
/*!40000 ALTER TABLE `helicopter` DISABLE KEYS */;
/*!40000 ALTER TABLE `helicopter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-21 20:40:06
