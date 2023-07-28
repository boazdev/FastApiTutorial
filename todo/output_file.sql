-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: factory_db
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `action`
--

DROP TABLE IF EXISTS `action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `action` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `max_actions` int NOT NULL,
  `date` date NOT NULL,
  `actions_allowed` int NOT NULL,
  `user_id` char(36) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `action_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action`
--

LOCK TABLES `action` WRITE;
/*!40000 ALTER TABLE `action` DISABLE KEYS */;
INSERT INTO `action` VALUES ('16158d7a-b671-4117-8161-532f00f3f731',10,'2023-07-27',4,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('2746013f-576b-43d5-884a-782a41aecb21',10,'2023-07-27',2,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('2d168ef7-23a0-4617-b2ec-d7c28038c068',25,'2023-07-27',24,'ad1fd84e-6242-4085-b3bc-ef5b4b177722'),('3ae598eb-fb7a-403a-bd73-565f38c9112c',25,'2023-07-27',23,'ad1fd84e-6242-4085-b3bc-ef5b4b177722'),('53426509-ad05-46ad-8945-da7ed9e638de',25,'2023-07-27',21,'ad1fd84e-6242-4085-b3bc-ef5b4b177722'),('57f4f5dc-7114-427d-b7e6-f2a317a88a1a',10,'2023-07-27',8,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('641fd813-5dad-4647-b695-3b16fdac93e7',25,'2023-07-27',22,'ad1fd84e-6242-4085-b3bc-ef5b4b177722'),('6db0cd39-6d0e-41f9-bc47-62fe3ee0afaa',10,'2023-07-27',9,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('81f13713-c120-4af0-8bc4-e59a71f1f9a3',25,'2023-07-27',20,'ad1fd84e-6242-4085-b3bc-ef5b4b177722'),('aa77200d-2b83-4604-8a61-42af21f085d7',10,'2023-07-27',6,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('efb39e43-d0ae-457e-86ca-4c6c2c3c35c1',10,'2023-07-27',3,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('f6c375b7-c070-4888-9963-ef47f62b4596',10,'2023-07-27',7,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('fda92406-d9ab-4161-aefb-c7f6309757c9',10,'2023-07-27',1,'27a3b14a-271e-11ee-8b1f-0242ac110002'),('fed37c02-5352-42ab-aae3-c6e238b899a2',10,'2023-07-27',5,'27a3b14a-271e-11ee-8b1f-0242ac110002');
/*!40000 ALTER TABLE `action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `name` varchar(255) NOT NULL,
  `manager_id` char(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_manager_id_employee` (`manager_id`),
  CONSTRAINT `fk_manager_id_employee` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('8db55833-295f-11ee-b7be-0242ac110002','Finance','4a303b7a-297a-11ee-b7be-0242ac110002'),('8db5afec-295f-11ee-b7be-0242ac110002','Human Resources','9d8ebbd6-297a-11ee-b7be-0242ac110002'),('8db5b2ac-295f-11ee-b7be-0242ac110002','Operations','f0b8b13a-2929-11ee-b7be-0242ac110002'),('ecf38167-295e-11ee-b7be-0242ac110002','Marketing','9d8eb834-297a-11ee-b7be-0242ac110002'),('ecf39088-295e-11ee-b7be-0242ac110002','Sales','9d8eba75-297a-11ee-b7be-0242ac110002'),('ecf39401-295e-11ee-b7be-0242ac110002','Engineering','4a303806-297a-11ee-b7be-0242ac110002');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `start_work_year` int NOT NULL,
  `department_id` char(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_department_id_department` (`department_id`),
  CONSTRAINT `fk_department_id_department` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('4a2de91d-297a-11ee-b7be-0242ac110002','Nathaniel','Hodgson',2015,'8db55833-295f-11ee-b7be-0242ac110002'),('4a303111-297a-11ee-b7be-0242ac110002','Elijah','Jordan',2022,'ecf38167-295e-11ee-b7be-0242ac110002'),('4a30348d-297a-11ee-b7be-0242ac110002','Nick','Cotton',2020,'8db5afec-295f-11ee-b7be-0242ac110002'),('4a303599-297a-11ee-b7be-0242ac110002','Ethan','York',2021,'8db5afec-295f-11ee-b7be-0242ac110002'),('4a303806-297a-11ee-b7be-0242ac110002','Connor','Tattersall',2022,'ecf39401-295e-11ee-b7be-0242ac110002'),('4a30388f-297a-11ee-b7be-0242ac110002','Harley','Alby',2021,'ecf39088-295e-11ee-b7be-0242ac110002'),('4a3038e3-297a-11ee-b7be-0242ac110002','Jesse','Breeden',2023,'8db5b2ac-295f-11ee-b7be-0242ac110002'),('4a30392c-297a-11ee-b7be-0242ac110002','Kyle','Livingstone',2020,'ecf39401-295e-11ee-b7be-0242ac110002'),('4a303b7a-297a-11ee-b7be-0242ac110002','Alfie','Watts',2022,'8db55833-295f-11ee-b7be-0242ac110002'),('4a304289-297a-11ee-b7be-0242ac110002','Sean','Owen',2021,'ecf39401-295e-11ee-b7be-0242ac110002'),('9d8e9d60-297a-11ee-b7be-0242ac110002','Evan','Dalton',2022,'ecf39401-295e-11ee-b7be-0242ac110002'),('9d8eb3cb-297a-11ee-b7be-0242ac110002','Elijah','Shelly',2023,'ecf38167-295e-11ee-b7be-0242ac110002'),('9d8eb834-297a-11ee-b7be-0242ac110002','James','Marsh',2021,'ecf38167-295e-11ee-b7be-0242ac110002'),('9d8eba75-297a-11ee-b7be-0242ac110002','Hugo','Camden',2022,'ecf39088-295e-11ee-b7be-0242ac110002'),('9d8ebb0f-297a-11ee-b7be-0242ac110002','Lewis','Lloyd',2020,'ecf39401-295e-11ee-b7be-0242ac110002'),('9d8ebb57-297a-11ee-b7be-0242ac110002','Arthur','Rayden',2023,'ecf39401-295e-11ee-b7be-0242ac110002'),('9d8ebb99-297a-11ee-b7be-0242ac110002','Isaac','Yates',2021,'ecf39088-295e-11ee-b7be-0242ac110002'),('9d8ebbd6-297a-11ee-b7be-0242ac110002','Hudson','Lambert',2022,'8db5afec-295f-11ee-b7be-0242ac110002'),('9d8ebc16-297a-11ee-b7be-0242ac110002','Charlie','Home',2020,'8db5b2ac-295f-11ee-b7be-0242ac110002'),('9d8ebc4f-297a-11ee-b7be-0242ac110002','Harri','Stapleton',2023,'8db55833-295f-11ee-b7be-0242ac110002'),('d5e62e78-5256-48c0-b2a1-ad0d9f90aa53','Tony','Charles',2043,'8db5afec-295f-11ee-b7be-0242ac110002'),('f0b879a0-2929-11ee-b7be-0242ac110002','John','Doe',2018,'8db5b2ac-295f-11ee-b7be-0242ac110002'),('f0b8a991-2929-11ee-b7be-0242ac110002','Jane','Smith',2019,'8db5b2ac-295f-11ee-b7be-0242ac110002'),('f0b8b13a-2929-11ee-b7be-0242ac110002','Michael','Johnson',2020,'8db5b2ac-295f-11ee-b7be-0242ac110002');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shift`
--

DROP TABLE IF EXISTS `shift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shift` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `date_time` date DEFAULT NULL,
  `starting_hour` int DEFAULT NULL,
  `ending_hour` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shift`
--

LOCK TABLES `shift` WRITE;
/*!40000 ALTER TABLE `shift` DISABLE KEYS */;
INSERT INTO `shift` VALUES ('046ed768-05eb-49bd-9440-9c083943eea2','2023-07-21',0,0),('59b57be4-27d5-11ee-837c-0242ac110002','2023-07-24',9,17),('59b5a511-27d5-11ee-837c-0242ac110002','2023-07-25',10,18),('59b5a99a-27d5-11ee-837c-0242ac110002','2023-07-26',8,16),('59b5ac01-27d5-11ee-837c-0242ac110002','2023-07-27',8,16),('59b5ac74-27d5-11ee-837c-0242ac110002','2023-07-28',9,17),('59b5acca-27d5-11ee-837c-0242ac110002','2023-07-29',11,19),('59b5ad23-27d5-11ee-837c-0242ac110002','2023-07-30',10,18),('bdfab1e8-177e-4fc1-8478-f375dd15feda','2023-08-25',5,10),('ce46236a-aad3-4f3f-9666-f1e0e6a48554','2023-07-29',17,23),('dc845ce8-b520-4c93-8daf-63533e2266e2','2023-07-31',2,10);
/*!40000 ALTER TABLE `shift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shift_employee`
--

DROP TABLE IF EXISTS `shift_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shift_employee` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `employee_id` char(36) NOT NULL,
  `shift_id` char(36) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `employee_id` (`employee_id`),
  KEY `shift_id` (`shift_id`),
  CONSTRAINT `shift_employee_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE,
  CONSTRAINT `shift_employee_ibfk_2` FOREIGN KEY (`shift_id`) REFERENCES `shift` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shift_employee`
--

LOCK TABLES `shift_employee` WRITE;
/*!40000 ALTER TABLE `shift_employee` DISABLE KEYS */;
INSERT INTO `shift_employee` VALUES ('01cc3e16-b5d8-433c-a094-0b94fc9c6e5b','4a303806-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('0203f729-9cd4-4859-815a-a249fbc31456','9d8ebbd6-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('0dfa5e76-7a1c-4864-b8c7-ccff72a91f1a','4a303599-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('0f4a82fc-d16a-49c3-86f7-23cd17fcca4e','9d8ebb57-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('19d1f936-8a39-42ee-8384-19eaf4ea28b0','9d8ebbd6-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('1b3cb24b-cd60-4fc6-9d72-d900ebb19f01','9d8e9d60-297a-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('1d8b8d45-37f4-41f5-81db-40482dcd737e','4a303599-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('1f841112-8b03-49a2-bcb5-8978c1b5d7af','d5e62e78-5256-48c0-b2a1-ad0d9f90aa53','59b5ad23-27d5-11ee-837c-0242ac110002'),('209f6b71-f168-45a1-86a6-07de742ea027','9d8e9d60-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('2103a0ed-e1d1-4826-a1ab-98df62553f00','9d8eb3cb-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('214898a3-d7ce-48b3-97d2-251766500099','4a304289-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('219310fc-9b32-4ae0-9b5e-dd2b838820f1','f0b8b13a-2929-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('230f3650-bd7a-4dfb-a571-1452c3ba9582','f0b8b13a-2929-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('24504816-6031-47e4-8947-00b31e8e4ff0','f0b8a991-2929-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('25599c56-dbca-4497-9673-de7f9eff9728','9d8ebb99-297a-11ee-b7be-0242ac110002','59b5ac01-27d5-11ee-837c-0242ac110002'),('264afad8-6861-44de-ad07-23b7c3198c78','9d8ebb99-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('29affdfa-e919-47aa-add9-1b910ed52d2d','9d8eb834-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('2a3d1da2-c838-4664-aebe-fd831f7bf1dd','9d8ebb99-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('2e464605-7e7d-4f21-931e-25c14fcc8ee1','9d8ebb0f-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('2f749dee-e065-4cc9-9f7d-1debbc83488c','9d8eba75-297a-11ee-b7be-0242ac110002','59b5ac01-27d5-11ee-837c-0242ac110002'),('32bf5de6-fa1e-4d7d-b323-5f0b26613ba4','9d8ebb57-297a-11ee-b7be-0242ac110002','59b5ac74-27d5-11ee-837c-0242ac110002'),('36d802fa-3cce-47a5-a305-d5d4df48c4d8','f0b879a0-2929-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('3957d226-87a6-40c0-a84f-04b87f3019e5','4a30348d-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('3a35a579-3666-410b-97e7-626104a81868','9d8ebb0f-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('3c42071b-411f-4bf8-a9c9-659492af7fbc','4a303b7a-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('3d38a206-d1c6-4079-9320-9cc78c2a66e8','4a3038e3-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('3e2438e4-30ad-4b55-983b-ccc95536e968','f0b879a0-2929-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('3e781af1-849e-49d1-8123-7113ff691874','f0b8a991-2929-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('3e8d3de4-0432-4050-97a4-1be7fa6e1166','f0b879a0-2929-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('3e942339-17bf-415d-b6e7-31aa160738ea','4a30348d-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('45dfa9ef-7419-4a9b-a809-ee81bec1cd2c','4a30392c-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('4753bf52-a538-44bf-9eba-af675bd3cceb','4a2de91d-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('4baa4cfc-4e60-43ec-a0f8-263badc72004','9d8ebc4f-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('4bc906d2-b5a3-4b50-9840-a15f3be0aaea','9d8ebc4f-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('4fa85d8d-108b-48d0-9b3e-555447bd854e','4a303806-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('505a71d1-ff44-427b-a985-d35681c85308','f0b8b13a-2929-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('518a5fff-185e-4be1-8b40-d91ffd25bcf8','4a303b7a-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('5266be2b-3e04-4646-86c1-57b3d031f8f5','f0b8a991-2929-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('56b453ad-2545-4ba4-a728-11b9772fac74','4a303599-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('5a897096-103f-4592-b323-7465411d45d2','4a2de91d-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('61506510-65b5-48ad-be1e-4e5ff945d43e','4a303111-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('6652ce61-c8c5-4fdf-8477-6fcfa2f0c09a','9d8eb3cb-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('6a806b4a-b5ce-4d5c-9e83-7af180e4ccb3','9d8eb834-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('6be181ff-68e8-4913-8696-584348fc8670','9d8eb834-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('7353631d-1692-49b7-b073-00cf23365369','9d8ebb57-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('7904196f-95a4-4b25-942f-53cee42c0b64','9d8ebb0f-297a-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('797829f8-d23b-407a-800c-d24f24120d21','4a303806-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('7c863013-e25d-4e5f-8e8a-f4c794795b2e','4a30392c-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('7e5fc476-6f56-4b81-b3be-c7814cc8be49','4a303b7a-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('815ee95f-eb4f-4365-8b08-b1f30080b97f','4a30348d-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('892a408d-bb36-46dd-aabf-c9e0f7eb3233','4a303111-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('8abec3ba-ce89-4731-9482-adf481781233','4a30388f-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('8e1b4f45-5e6f-44a6-8c0a-61751afdec90','9d8ebb0f-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('8fa08000-14b6-4584-9e59-5a08267f8b6d','9d8eba75-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('94526956-e2b6-48fb-917a-446a3057aabd','d5e62e78-5256-48c0-b2a1-ad0d9f90aa53','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('94d679a2-5a60-40f0-bff4-2b96a85de3f4','4a30388f-297a-11ee-b7be-0242ac110002','59b5ac74-27d5-11ee-837c-0242ac110002'),('9b8d0837-0ccd-4ea3-8335-30eb1473052a','4a303111-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('9c40d6a9-6833-442d-af18-c6f5bb03b81d','9d8eb834-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('9d5ee1ab-e4ca-4bc4-bc00-e4dfe6b7ce22','4a304289-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('9f5776f5-70c8-4e89-8601-2648ff5cfde7','9d8ebbd6-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('9ff2a961-57bb-4641-8dfd-dfbfd4adde36','d5e62e78-5256-48c0-b2a1-ad0d9f90aa53','046ed768-05eb-49bd-9440-9c083943eea2'),('ab3ee0f0-9368-4593-b8f0-465c74116b86','4a30392c-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('aed9e921-3038-4ae3-93b7-02a802946bda','9d8ebc16-297a-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('aee3730f-45f7-4950-9a47-d8b951e25dca','f0b8b13a-2929-11ee-b7be-0242ac110002','59b5ac74-27d5-11ee-837c-0242ac110002'),('afaef3a7-8db2-4da7-a06c-9a52183aded9','4a30388f-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('b1ba36e6-8409-4d6b-a071-7d3fa89d8f70','4a30392c-297a-11ee-b7be-0242ac110002','59b5ac01-27d5-11ee-837c-0242ac110002'),('b4442db9-6a68-45a5-a89b-96e51f1b6db5','9d8eba75-297a-11ee-b7be-0242ac110002','59b5ac74-27d5-11ee-837c-0242ac110002'),('b7d42f67-3721-460c-8a74-a12921d43d51','4a304289-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('ba319448-91cf-4cf0-8c1a-c09055344c50','d5e62e78-5256-48c0-b2a1-ad0d9f90aa53','59b5acca-27d5-11ee-837c-0242ac110002'),('c0c5d9e7-3e1f-49be-9365-cf6a31fd709f','4a303599-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('c396058d-ba9f-47d7-bf14-60735716e59f','9d8e9d60-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('ca3f6c5c-984d-40b8-965c-bd9aecb11d7a','4a3038e3-297a-11ee-b7be-0242ac110002','59b5ac01-27d5-11ee-837c-0242ac110002'),('cbc26dbd-d4de-4fbe-bb15-7ab9ef2aa818','4a2de91d-297a-11ee-b7be-0242ac110002','046ed768-05eb-49bd-9440-9c083943eea2'),('d14b3ae3-b04c-4f61-ae47-9594756021b7','9d8ebc16-297a-11ee-b7be-0242ac110002','59b5ad23-27d5-11ee-837c-0242ac110002'),('d3b4c1c2-8894-46db-b7c5-6eb11d93d979','9d8eb3cb-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('d7e5b91a-991a-40f4-aaa1-fe49913303e2','4a2de91d-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('da815f7d-a441-4b7f-bb13-522e4673c7b1','9d8ebc4f-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('db419c9c-8624-40b0-9542-0e494bd4293d','f0b8a991-2929-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('db7a2eca-a2ac-4f69-8241-baf0b5117eda','4a30348d-297a-11ee-b7be-0242ac110002','59b5a511-27d5-11ee-837c-0242ac110002'),('dd776f5c-dda2-4887-a07b-c37620dbcf8e','9d8ebc16-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('ddb6ac67-0883-4120-bf5e-f09526769949','4a303b7a-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('de578116-c0dc-4122-b87d-85b5624a5553','4a303111-297a-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554'),('deb4f298-9d50-4cd6-bbe5-20b29c29d5f4','9d8ebbd6-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('e06c2f63-ab5b-4d03-82c3-18aa6a11d8cb','4a30388f-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('e1358bb0-052e-46cf-96be-b7c7ad5b65a8','4a3038e3-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('e5673d60-0c2d-467a-a67e-a880056621d2','4a303806-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('e5f5c9e9-ad66-4e44-9feb-7537a77a449f','9d8e9d60-297a-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('e681d830-992d-4c6b-b33e-00ac4835b269','9d8ebb99-297a-11ee-b7be-0242ac110002','bdfab1e8-177e-4fc1-8478-f375dd15feda'),('eb04379a-54be-482d-ac4b-256ffd4adc17','9d8eb3cb-297a-11ee-b7be-0242ac110002','59b5ac01-27d5-11ee-837c-0242ac110002'),('ecade057-0cb8-4721-b73a-ed38714ada2e','9d8ebc16-297a-11ee-b7be-0242ac110002','dc845ce8-b520-4c93-8daf-63533e2266e2'),('f1a4b67a-e177-4fda-9194-9356247e02b6','9d8eba75-297a-11ee-b7be-0242ac110002','59b57be4-27d5-11ee-837c-0242ac110002'),('f88fb25b-970c-4e13-a14c-deb381dc5864','4a3038e3-297a-11ee-b7be-0242ac110002','59b5ac74-27d5-11ee-837c-0242ac110002'),('f8949d8c-c434-4ac5-8ba9-fe0e36873bb2','9d8ebb57-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('f984d02e-e9b0-4866-91ce-4bb8c50ec140','9d8ebc4f-297a-11ee-b7be-0242ac110002','59b5acca-27d5-11ee-837c-0242ac110002'),('fc725ef6-4ffa-4b55-8731-51e6a4626ae2','f0b879a0-2929-11ee-b7be-0242ac110002','59b5a99a-27d5-11ee-837c-0242ac110002'),('fe557341-6a63-45d6-92fd-8be4e5427afa','4a304289-297a-11ee-b7be-0242ac110002','ce46236a-aad3-4f3f-9666-f1e0e6a48554');
/*!40000 ALTER TABLE `shift_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `num_of_actions` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('27a3b14a-271e-11ee-8b1f-0242ac110002','john_doe','password123','John Doe',10),('27a435b0-271e-11ee-8b1f-0242ac110002','jane_smith','pass456','Jane Smith',5),('27a43cfa-271e-11ee-8b1f-0242ac110002','bob_johnson','secret123','Bob Johnson',15),('6215efee-22d5-4020-a2a5-1b8c1ccecb74','mable','mable123','mable carlson',20),('ac41a6ae-0cd0-407c-ac66-7912727a998b','test_user','test123','python tester',100000),('ad1fd84e-6242-4085-b3bc-ef5b4b177722','maxin','maxin123','Maxin Bax',25),('cba38ea8-4802-489b-8795-44387efd7b7f','john123','john123','John Silva',23),('ea828270-dc44-41f6-9825-ec47785a4ae4','test123','testpass','test test',22);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-27 12:55:04
