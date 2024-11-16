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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Std_Id` int NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Email_Id` varchar(24) NOT NULL,
  `Date_Of_Birth` date NOT NULL,
  `Guardian_Name` varchar(30) NOT NULL,
  `Nationality` varchar(20) NOT NULL,
  `Gender` enum('M','F') NOT NULL,
  `Contact_Number` varchar(15) NOT NULL,
  `Address` varchar(35) NOT NULL,
  PRIMARY KEY (`Std_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Alice Smith','alice.smith@xyz.com','2002-01-15','John Smith','Indian','F','1234567890','123 Main St, Delhi'),(2,'Bob Johnson','bob.johnson@xyz.com','2003-03-20','Jane Johnson','Bhutan','M','2345678901','456 Oak St, Thimphu'),(3,'Carol Davis','carol.davis@xyz.com','2001-11-02','David Davis','Pakistani','F','3456789012','789 Pine St, Karachi'),(4,'David Harris','david.harris@xyz.com','2002-05-10','Emily Harris','Afghan','M','4567890123','101 Maple St, Kabul'),(5,'Eve Thompson','eve.thompson@xyz.com','2000-07-22','Frank Thompson','Nepali','F','5678901234','102 Birch St, Kathmandu'),(6,'Frank Walker','frank.walker@xyz.com','2001-09-18','George Walker','Indian','M','6789012345','103 Elm St, Mumbai'),(7,'Grace Lee','grace.lee@xyz.com','2003-12-29','Hannah Lee','Bangladeshi','F','7890123456','104 Cedar St, Dhaka'),(8,'Henry King','henry.king@xyz.com','2001-04-14','Isabella King','Bhutan','M','8901234567','105 Walnut St, Phuntsholing'),(9,'Ivy Green','ivy.green@xyz.com','2002-08-05','Jack Green','Afghan','F','9012345678','106 Chestnut St, Herat'),(10,'Jack White','jack.white@xyz.com','2003-10-23','Karen White','Indian','M','1234567890','107 Cypress St, Jaipur'),(11,'Kate Brown','kate.brown@xyz.com','2000-02-17','Leo Brown','Sri Lankan','F','2345678901','108 Spruce St, Colombo'),(12,'Leo Black','leo.black@xyz.com','2001-06-03','Mary Black','Nepali','M','3456789012','109 Willow St, Pokhara'),(13,'Maya Wilson','maya.wilson@xyz.com','2002-09-09','Nathan Wilson','Pakistani','F','4567890123','110 Cedar St, Lahore'),(14,'Noah Clark','noah.clark@xyz.com','2003-11-30','Olivia Clark','Bangladeshi','M','5678901234','111 Alder St, Chittagong'),(15,'Olivia Young','olivia.young@xyz.com','2000-03-25','Paul Young','Indian','F','6789012345','112 Dogwood St, Delhi'),(16,'Paul Scott','paul.scott@xyz.com','2001-08-15','Queen Scott','Sri Lankan','M','7890123456','113 Fir St, Kandy'),(17,'Quinn Hall','quinn.hall@xyz.com','2002-07-06','Ray Hall','Afghan','M','8901234567','114 Beech St, Mazar-i-Sharif'),(18,'Ryan Adams','ryan.adams@xyz.com','2000-12-12','Sara Adams','Indian','M','9012345678','115 Poplar St, Chennai'),(19,'Sophia Baker','sophia.baker@xyz.com','2003-05-04','Tom Baker','Nepali','F','1234567890','116 Ash St, Lalitpur'),(20,'Tom Carter','tom.carter@xyz.com','2001-10-19','Uma Carter','Bhutan','M','2345678901','117 Maple St, Thimphu');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
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
