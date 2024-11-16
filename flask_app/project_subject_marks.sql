-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `subject_marks`
--

DROP TABLE IF EXISTS `subject_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject_marks` (
  `SR_No` int NOT NULL,
  `Std_Id` int NOT NULL,
  `Sub_Id` int DEFAULT NULL,
  `Marks` int NOT NULL,
  `Grade` varchar(7) NOT NULL,
  `Semester` varchar(5) NOT NULL,
  PRIMARY KEY (`SR_No`),
  KEY `Sub_Id` (`Sub_Id`),
  KEY `Std_Id` (`Std_Id`),
  CONSTRAINT `subject_marks_ibfk_1` FOREIGN KEY (`Sub_Id`) REFERENCES `subjects` (`Sub_Id`),
  CONSTRAINT `subject_marks_ibfk_2` FOREIGN KEY (`Std_Id`) REFERENCES `student` (`Std_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject_marks`
--

LOCK TABLES `subject_marks` WRITE;
/*!40000 ALTER TABLE `subject_marks` DISABLE KEYS */;
INSERT INTO `subject_marks` VALUES (1,1,1001,85,'A','first'),(2,1,1002,78,'B','first'),(3,1,1003,92,'A','first'),(4,1,1004,88,'A','first'),(5,1,1005,75,'B','first'),(6,1,1006,80,'B','first'),(7,1,1007,90,'A','first'),(8,1,1008,77,'B','first'),(9,1,1009,85,'A','first'),(10,1,1010,65,'C','first'),(11,2,1001,72,'B','first'),(12,2,1002,88,'A','first'),(13,2,1003,95,'A','first'),(14,2,1004,80,'B','first'),(15,2,1005,78,'B','first'),(16,2,1006,82,'A','first'),(17,2,1007,76,'B','first'),(18,2,1008,89,'A','first'),(19,2,1009,68,'C','first'),(20,2,1010,74,'B','first'),(21,3,1001,88,'A','first'),(22,3,1002,75,'B','first'),(23,3,1003,80,'B','first'),(24,3,1004,93,'A','first'),(25,3,1005,81,'B','first'),(26,3,1006,77,'B','first'),(27,3,1007,79,'B','first'),(28,3,1008,85,'A','first'),(29,3,1009,70,'B','first'),(30,3,1010,90,'A','first'),(31,4,1001,79,'B','first'),(32,4,1002,84,'A','first'),(33,4,1003,72,'B','first'),(34,4,1004,91,'A','first'),(35,4,1005,70,'B','first'),(36,4,1006,85,'A','first'),(37,4,1007,77,'B','first'),(38,4,1008,76,'B','first'),(39,4,1009,68,'C','first'),(40,4,1010,89,'A','first'),(41,5,1001,82,'A','first'),(42,5,1002,80,'B','first'),(43,5,1003,88,'A','first'),(44,5,1004,84,'A','first'),(45,5,1005,85,'A','first'),(46,5,1006,90,'A','first'),(47,5,1007,75,'B','first'),(48,5,1008,81,'B','first'),(49,5,1009,79,'B','first'),(50,5,1010,76,'B','first'),(51,6,1001,70,'B','first'),(52,6,1002,78,'B','first'),(53,6,1003,91,'A','first'),(54,6,1004,85,'A','first'),(55,6,1005,79,'B','first'),(56,6,1006,83,'A','first'),(57,6,1007,87,'A','first'),(58,6,1008,70,'B','first'),(59,6,1009,66,'C','first'),(60,6,1010,88,'A','first'),(61,7,1001,90,'A','first'),(62,7,1002,92,'A','first'),(63,7,1003,75,'B','first'),(64,7,1004,77,'B','first'),(65,7,1005,84,'A','first'),(66,7,1006,80,'B','first'),(67,7,1007,95,'A','first'),(68,7,1008,72,'B','first'),(69,7,1009,76,'B','first'),(70,7,1010,88,'A','first'),(71,8,1001,85,'A','first'),(72,8,1002,78,'B','first'),(73,8,1003,92,'A','first'),(74,8,1004,88,'A','first'),(75,8,1005,75,'B','first'),(76,8,1006,80,'B','first'),(77,8,1007,90,'A','first'),(78,8,1008,77,'B','first'),(79,8,1009,85,'A','first'),(80,8,1010,65,'C','first'),(81,9,1001,72,'B','first'),(82,9,1002,88,'A','first'),(83,9,1003,95,'A','first'),(84,9,1004,80,'B','first'),(85,9,1005,78,'B','first'),(86,9,1006,82,'A','first'),(87,9,1007,76,'B','first'),(88,9,1008,89,'A','first'),(89,9,1009,68,'C','first'),(90,9,1010,74,'B','first'),(91,10,1001,88,'A','first'),(92,10,1002,75,'B','first'),(93,10,1003,80,'B','first'),(94,10,1004,93,'A','first'),(95,10,1005,81,'B','first'),(96,10,1006,77,'B','first'),(97,10,1007,79,'B','first'),(98,10,1008,85,'A','first'),(99,10,1009,70,'B','first'),(100,10,1010,90,'A','first'),(101,11,1001,79,'B','first'),(102,11,1002,84,'A','first'),(103,11,1003,72,'B','first'),(104,11,1004,91,'A','first'),(105,11,1005,70,'B','first'),(106,11,1006,85,'A','first'),(107,11,1007,77,'B','first'),(108,11,1008,76,'B','first'),(109,11,1009,68,'C','first'),(110,11,1010,89,'A','first'),(111,12,1001,82,'A','first'),(112,12,1002,80,'B','first'),(113,12,1003,88,'A','first'),(114,12,1004,84,'A','first'),(115,12,1005,85,'A','first'),(116,12,1006,90,'A','first'),(117,12,1007,75,'B','first'),(118,12,1008,81,'B','first'),(119,12,1009,79,'B','first'),(120,12,1010,76,'B','first'),(121,13,1001,70,'B','first'),(122,13,1002,78,'B','first'),(123,13,1003,91,'A','first'),(124,13,1004,85,'A','first'),(125,13,1005,79,'B','first'),(126,13,1006,83,'A','first'),(127,13,1007,87,'A','first'),(128,13,1008,70,'B','first'),(129,13,1009,66,'C','first'),(130,13,1010,88,'A','first'),(131,14,1001,90,'A','first'),(132,14,1002,92,'A','first'),(133,14,1003,75,'B','first'),(134,14,1004,77,'B','first'),(135,14,1005,84,'A','first'),(136,14,1006,80,'B','first'),(137,14,1007,95,'A','first'),(138,14,1008,72,'B','first'),(139,14,1009,76,'B','first'),(140,14,1010,88,'A','first'),(141,15,1001,78,'B','first'),(142,15,1002,84,'A','first'),(143,15,1003,71,'B','first'),(144,15,1004,89,'A','first'),(145,15,1005,80,'B','first'),(146,15,1006,75,'B','first'),(147,15,1007,92,'A','first'),(148,15,1008,88,'A','first'),(149,15,1009,78,'B','first'),(150,15,1010,83,'A','first'),(151,16,1001,80,'B','first'),(152,16,1002,85,'A','first'),(153,16,1003,77,'B','first'),(154,16,1004,93,'A','first'),(155,16,1005,74,'B','first'),(156,16,1006,82,'A','first'),(157,16,1007,91,'A','first'),(158,16,1008,76,'B','first'),(159,16,1009,88,'A','first'),(160,16,1010,79,'B','first'),(161,17,1001,83,'A','first'),(162,17,1002,90,'A','first'),(163,17,1003,72,'B','first'),(164,17,1004,85,'A','first'),(165,17,1005,76,'B','first'),(166,17,1006,94,'A','first'),(167,17,1007,79,'B','first'),(168,17,1008,77,'B','first'),(169,17,1009,90,'A','first'),(170,17,1010,84,'A','first'),(171,18,1001,92,'A','first'),(172,18,1002,78,'B','first'),(173,18,1003,81,'B','first'),(174,18,1004,77,'B','first'),(175,18,1005,88,'A','first'),(176,18,1006,80,'B','first'),(177,18,1007,82,'A','first'),(178,18,1008,75,'B','first'),(179,18,1009,85,'A','first'),(180,18,1010,79,'B','first'),(181,19,1001,88,'A','first'),(182,19,1002,74,'B','first'),(183,19,1003,76,'B','first'),(184,19,1004,80,'B','first'),(185,19,1005,79,'B','first'),(186,19,1006,91,'A','first'),(187,19,1007,85,'A','first'),(188,19,1008,77,'B','first'),(189,19,1009,90,'A','first'),(190,19,1010,80,'B','first'),(191,20,1001,78,'B','first'),(192,20,1002,84,'A','first'),(193,20,1003,88,'A','first'),(194,20,1004,80,'B','first'),(195,20,1005,74,'B','first'),(196,20,1006,85,'A','first'),(197,20,1007,89,'A','first'),(198,20,1008,91,'A','first'),(199,20,1009,82,'A','first'),(200,20,1010,76,'B','first');
/*!40000 ALTER TABLE `subject_marks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13 11:17:09
