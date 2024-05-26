-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: scopus
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `scopus_distances`
--

DROP TABLE IF EXISTS `scopus_distances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scopus_distances` (
  `DOI` varchar(50) NOT NULL,
  `CitationsCount` int DEFAULT NULL,
  `Authors_Number` int DEFAULT NULL,
  `Affiliations_Number` int DEFAULT NULL,
  `Minimum_Geographical_Distance` float DEFAULT NULL,
  `Maximum_Geographical_Distance` float DEFAULT NULL,
  `Average_Geographical_Distance` float DEFAULT NULL,
  `Minimum_Organizational_Distance` int DEFAULT NULL,
  `Maximum_Organizational_Distance` int DEFAULT NULL,
  `Average_Organizational_Distance` int DEFAULT NULL,
  `Minimum_Cultural_Distance` float DEFAULT NULL,
  `Maximum_Cultural_Distance` float DEFAULT NULL,
  `Average_Cultural_Distance` float DEFAULT NULL,
  PRIMARY KEY (`DOI`),
  CONSTRAINT `scopus_distances_ibfk_1` FOREIGN KEY (`DOI`) REFERENCES `scopus_publications` (`DOI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scopus_distances`
--

LOCK TABLES `scopus_distances` WRITE;
/*!40000 ALTER TABLE `scopus_distances` DISABLE KEYS */;
/*!40000 ALTER TABLE `scopus_distances` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-10 20:36:04
