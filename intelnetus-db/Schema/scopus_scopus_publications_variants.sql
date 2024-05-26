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
-- Table structure for table `scopus_publications_variants`
--

DROP TABLE IF EXISTS `scopus_publications_variants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scopus_publications_variants` (
  `Variant_1_ID` varchar(40) DEFAULT NULL,
  `Variant_2_ID` varchar(40) DEFAULT NULL,
  UNIQUE KEY `Variant_1_ID` (`Variant_1_ID`,`Variant_2_ID`),
  UNIQUE KEY `Variant_1_ID_2` (`Variant_1_ID`,`Variant_2_ID`),
  KEY `Variant_2_ID` (`Variant_2_ID`),
  CONSTRAINT `scopus_publications_variants_ibfk_1` FOREIGN KEY (`Variant_1_ID`) REFERENCES `scopus_publications` (`ID`),
  CONSTRAINT `scopus_publications_variants_ibfk_2` FOREIGN KEY (`Variant_2_ID`) REFERENCES `scopus_publications` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scopus_publications_variants`
--

LOCK TABLES `scopus_publications_variants` WRITE;
/*!40000 ALTER TABLE `scopus_publications_variants` DISABLE KEYS */;
INSERT INTO `scopus_publications_variants` VALUES ('01aabcdd-6b12-4756-9496-548d67a298b3','84a65f22-d790-4cbc-9e00-ab4ffc794185'),('081de423-69b9-4f3c-8849-fd7dfa8b1b1c','f956ea38-ad71-4297-9797-f71e9bf15192'),('0a09a9be-61fc-44c7-ba5d-4d9970536513','87850658-93d0-4aa8-9ff8-c38bed115168'),('0a1cb7a8-9c4e-4a6f-8d97-3b8b74409bbe','7fb8ed13-0266-4444-ad8b-9dce42ed3bce'),('0a1cb7a8-9c4e-4a6f-8d97-3b8b74409bbe','c05cdec8-3dbc-48e8-a0b1-d3a44a5885df'),('0a1cb7a8-9c4e-4a6f-8d97-3b8b74409bbe','f1f7a775-8317-4588-a550-a7260c76173e'),('12e65c0d-9cac-4a48-afef-b8cb5d1dafd3','757173f0-d631-4999-9d8d-7572fb50afdc'),('235f3584-9840-4298-a18a-172fe0e4099f','862f134a-f713-427f-b07d-2472fb05ec88'),('32140c53-c5c5-43fa-a14e-d72ca2bb6f0d','7a9988a4-0d5b-4fa5-836a-738649bfb988'),('3c61c162-23be-42fc-95b8-b1eddc873e75','64c1c587-a41b-4ad8-b8d7-978ab44123d3'),('3d7de3be-d494-4ecb-84dd-b0459e8afab3','7499c48f-ea58-45e5-90f1-97a0d2a025ac'),('4a363b76-91bd-4494-8c56-752410556672','e5c59725-e208-44da-ab48-1401f428dd68'),('4d653484-9cf8-41d8-b80b-98db62d3dbd2','60bf1a81-64b9-42fd-a514-c0f196b2e1f0'),('60bf1a81-64b9-42fd-a514-c0f196b2e1f0','4d653484-9cf8-41d8-b80b-98db62d3dbd2'),('634a317c-4fcc-4962-b64f-1ce29432efa0','f09a22b2-fedc-42f7-9f0f-9bf04ffe4cde'),('64c1c587-a41b-4ad8-b8d7-978ab44123d3','3c61c162-23be-42fc-95b8-b1eddc873e75'),('6cd34856-c5c9-4093-bc99-4d010fe69abc','86045896-f97b-4d73-a75b-8d682bea3dc2'),('757173f0-d631-4999-9d8d-7572fb50afdc','12e65c0d-9cac-4a48-afef-b8cb5d1dafd3'),('7a9988a4-0d5b-4fa5-836a-738649bfb988','32140c53-c5c5-43fa-a14e-d72ca2bb6f0d'),('81b9fc96-21e5-494e-bf46-2b6f4df2cda1','f4325404-b226-4b4a-bc21-7b69324b7b8e'),('84a65f22-d790-4cbc-9e00-ab4ffc794185','01aabcdd-6b12-4756-9496-548d67a298b3'),('86045896-f97b-4d73-a75b-8d682bea3dc2','6cd34856-c5c9-4093-bc99-4d010fe69abc'),('862f134a-f713-427f-b07d-2472fb05ec88','235f3584-9840-4298-a18a-172fe0e4099f'),('87850658-93d0-4aa8-9ff8-c38bed115168','0a09a9be-61fc-44c7-ba5d-4d9970536513'),('87850658-93d0-4aa8-9ff8-c38bed115168','69951f37-df14-45e6-9d4e-e807f2d48569'),('931c8646-86af-4153-b4e2-b695485f4b9e','a59ade51-cc9c-4a31-9dd1-634569e61cc8'),('9b0ce36e-674b-4422-8afd-3595f67c1b72','dcbb1584-9c16-47da-84a3-b19ec6be9c06'),('a1275f7e-23ff-4ac5-8285-cfc6c10efb8d','d1e35eba-b933-4569-9890-de3917241944'),('a1275f7e-23ff-4ac5-8285-cfc6c10efb8d','d3e50257-0421-4aa1-806b-d2c1e3cd6426'),('a1275f7e-23ff-4ac5-8285-cfc6c10efb8d','ffa62723-a90c-4757-a4bc-a35791c9a90f'),('a59ade51-cc9c-4a31-9dd1-634569e61cc8','931c8646-86af-4153-b4e2-b695485f4b9e'),('a628c005-4615-4f68-b48a-a57e513e4aac','ae74648f-200f-4dbc-98af-d60213bf3736'),('ae74648f-200f-4dbc-98af-d60213bf3736','a628c005-4615-4f68-b48a-a57e513e4aac'),('c05cdec8-3dbc-48e8-a0b1-d3a44a5885df','0a1cb7a8-9c4e-4a6f-8d97-3b8b74409bbe'),('c05cdec8-3dbc-48e8-a0b1-d3a44a5885df','f1f7a775-8317-4588-a550-a7260c76173e'),('cedbc2c4-d172-4778-baa3-f0d4025bf63d','f6cd782d-c54c-4f90-b9e3-c3bc68c3bc62'),('d1e35eba-b933-4569-9890-de3917241944','a1275f7e-23ff-4ac5-8285-cfc6c10efb8d'),('d1e35eba-b933-4569-9890-de3917241944','d3e50257-0421-4aa1-806b-d2c1e3cd6426'),('d1e35eba-b933-4569-9890-de3917241944','ffa62723-a90c-4757-a4bc-a35791c9a90f'),('d3e50257-0421-4aa1-806b-d2c1e3cd6426','a1275f7e-23ff-4ac5-8285-cfc6c10efb8d'),('d3e50257-0421-4aa1-806b-d2c1e3cd6426','d1e35eba-b933-4569-9890-de3917241944'),('d3e50257-0421-4aa1-806b-d2c1e3cd6426','ffa62723-a90c-4757-a4bc-a35791c9a90f'),('dcbb1584-9c16-47da-84a3-b19ec6be9c06','9b0ce36e-674b-4422-8afd-3595f67c1b72'),('e5c59725-e208-44da-ab48-1401f428dd68','4a363b76-91bd-4494-8c56-752410556672'),('f09a22b2-fedc-42f7-9f0f-9bf04ffe4cde','634a317c-4fcc-4962-b64f-1ce29432efa0'),('f1f7a775-8317-4588-a550-a7260c76173e','0a1cb7a8-9c4e-4a6f-8d97-3b8b74409bbe'),('f1f7a775-8317-4588-a550-a7260c76173e','7fb8ed13-0266-4444-ad8b-9dce42ed3bce'),('f1f7a775-8317-4588-a550-a7260c76173e','c05cdec8-3dbc-48e8-a0b1-d3a44a5885df'),('f6cd782d-c54c-4f90-b9e3-c3bc68c3bc62','cedbc2c4-d172-4778-baa3-f0d4025bf63d'),('f956ea38-ad71-4297-9797-f71e9bf15192','081de423-69b9-4f3c-8849-fd7dfa8b1b1c'),('ffa62723-a90c-4757-a4bc-a35791c9a90f','a1275f7e-23ff-4ac5-8285-cfc6c10efb8d'),('ffa62723-a90c-4757-a4bc-a35791c9a90f','d1e35eba-b933-4569-9890-de3917241944'),('ffa62723-a90c-4757-a4bc-a35791c9a90f','d3e50257-0421-4aa1-806b-d2c1e3cd6426');
/*!40000 ALTER TABLE `scopus_publications_variants` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-10 20:36:03
