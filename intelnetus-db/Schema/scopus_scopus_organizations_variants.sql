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
-- Table structure for table `scopus_organizations_variants`
--

DROP TABLE IF EXISTS `scopus_organizations_variants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scopus_organizations_variants` (
  `Variant_1_ID` varchar(40) DEFAULT NULL,
  `Variant_2_ID` varchar(40) DEFAULT NULL,
  UNIQUE KEY `Variant_1_ID` (`Variant_1_ID`,`Variant_2_ID`),
  KEY `Variant_2_ID` (`Variant_2_ID`),
  CONSTRAINT `scopus_organizations_variants_ibfk_1` FOREIGN KEY (`Variant_1_ID`) REFERENCES `scopus_organizations` (`ID`),
  CONSTRAINT `scopus_organizations_variants_ibfk_2` FOREIGN KEY (`Variant_2_ID`) REFERENCES `scopus_organizations` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scopus_organizations_variants`
--

LOCK TABLES `scopus_organizations_variants` WRITE;
/*!40000 ALTER TABLE `scopus_organizations_variants` DISABLE KEYS */;
INSERT INTO `scopus_organizations_variants` VALUES ('05527b04-317c-4119-998f-07475b72f7e8','1f66797d-d52e-409d-803f-fe7a1ac38792'),('0e20c3b4-0fc0-4cc4-9378-e32c942176f8','9373b375-c8b8-4ad2-a954-e15e2b44cc9f'),('0efd78f4-9c7f-4e14-96b9-b140ca9019c9','4e0d5320-2df0-45f1-bc4c-28a541d452cc'),('173ca71e-2e62-4af7-8f3a-200d267cd693','cfcebd90-1db6-46d8-86fb-8b5ae6198696'),('24e589ec-9cec-47f0-91dc-f74a16a4d561','a57cf5b8-dfa0-49d7-9b95-6453ccd04f37'),('3e2c7bd8-9527-4f43-813f-b12e96e9b3f9','24bf4310-4e63-488e-b448-c98d4e3463f8'),('3e2c7bd8-9527-4f43-813f-b12e96e9b3f9','5da9a465-d2d0-42fb-a9a2-d1e0e4e52b87'),('42918a38-4e19-4b8b-8b41-85950201f83e','77b02140-b3dd-42af-a78d-17af3441c1f8'),('4e0d5320-2df0-45f1-bc4c-28a541d452cc','0efd78f4-9c7f-4e14-96b9-b140ca9019c9'),('4f9df3c5-c192-44ce-9d99-de67e85b4117','861e46cc-4ce0-4db5-a251-95eb74312e6c'),('516c269a-c845-411a-8c73-09c78184ab03','76d29b00-4774-4a21-ae47-70b55e046c91'),('57720dc4-2df9-4ae9-acdd-a08ef90f95fd','bae10a48-8350-498a-9e29-ffa4e7ac0bcb'),('5977b227-0187-4828-a7d2-d5c876d48179','b5bc9fd5-fb41-4bbf-a4a6-893039474787'),('5c6d2754-fad6-45f3-8b10-a93d77703a97','b92a5105-4892-4df2-b950-719696f58183'),('66ee8fd7-2b13-4a61-a323-18bcd1a45d24','cfcebd90-1db6-46d8-86fb-8b5ae6198696'),('68129638-2581-4e46-9a14-55518a871ba8','edaef741-c249-4b05-94c5-663df33f27cd'),('6ae99364-0b8d-4bf1-b7c9-053b3ea99afc','89d46a86-49bd-4084-8ae7-0a3f5525ac50'),('6bb15113-4091-4063-98c8-13d0e2576826','05b12dca-2efd-4caa-aafa-06e15a4ce27e'),('72e37bcd-0088-40ae-831e-054717efcc9b','8c8e7256-2304-48d3-ba02-5891a8f7f4a3'),('75ab5453-f764-4497-992b-34600fcfb171','b897c30b-a65f-4657-9582-1a4a561054ae'),('76c46c3c-aa56-476a-941a-448a41b7dc7d','2e2f969e-be2c-4651-8351-0ff4d5762882'),('76d29b00-4774-4a21-ae47-70b55e046c91','516c269a-c845-411a-8c73-09c78184ab03'),('7be5d472-af27-4c94-871d-7dded9edfb3d','cc9224e9-7375-4e7f-bc14-0f6b9322dd50'),('861e46cc-4ce0-4db5-a251-95eb74312e6c','4f9df3c5-c192-44ce-9d99-de67e85b4117'),('8c8e7256-2304-48d3-ba02-5891a8f7f4a3','72e37bcd-0088-40ae-831e-054717efcc9b'),('922125d5-0787-4505-9020-f77933d6f1e6','993eba35-d4d6-4659-8e50-45a5a32386b5'),('9373b375-c8b8-4ad2-a954-e15e2b44cc9f','0e20c3b4-0fc0-4cc4-9378-e32c942176f8'),('993eba35-d4d6-4659-8e50-45a5a32386b5','922125d5-0787-4505-9020-f77933d6f1e6'),('9bf17334-6d23-41ae-bbeb-fe2abc3f07b5','9d66f5c9-0923-4bb2-bf52-0848246d84bf'),('b897c30b-a65f-4657-9582-1a4a561054ae','75ab5453-f764-4497-992b-34600fcfb171'),('b9241e86-74cf-4f35-891a-1a7112f1948e','e6f9752f-db84-4aa4-a358-82a8513c76fc'),('bcd61b43-8946-4d8f-9b44-91b1002280ff','7910862e-800f-4a5a-9718-c14ef300b50e'),('bcd61b43-8946-4d8f-9b44-91b1002280ff','e96b6f37-94e2-433b-bfa1-e7cceca13173'),('c0cd7924-7eb8-4dbf-a4f5-5d1d09d2612f','7b54e65d-9d36-488d-976f-92073ad686ea'),('cb83cae0-a865-49aa-91cc-fc32bda9ee17','2b754e04-333f-45b7-b061-d04817431994'),('cc9224e9-7375-4e7f-bc14-0f6b9322dd50','7be5d472-af27-4c94-871d-7dded9edfb3d'),('cfcebd90-1db6-46d8-86fb-8b5ae6198696','173ca71e-2e62-4af7-8f3a-200d267cd693'),('e2f5dcb3-9948-4b08-baae-705c62c160ea','7921e80c-8f7b-4998-a4dc-32bc73cac181'),('e6f9752f-db84-4aa4-a358-82a8513c76fc','b9241e86-74cf-4f35-891a-1a7112f1948e'),('f0dfca2b-3fcf-4108-9cbd-ef098f213724','456ce012-e2e0-4fc6-bf74-c906f3652853');
/*!40000 ALTER TABLE `scopus_organizations_variants` ENABLE KEYS */;
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
