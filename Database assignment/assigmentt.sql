-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Apr 19, 2020 at 10:10 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assigmentt`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
CREATE TABLE IF NOT EXISTS `album` (
  `album_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `date_of_release` date DEFAULT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `album`
--

INSERT INTO `album` (`album_id`, `name`, `date_of_release`) VALUES
(1, 'BLOND', '2017-06-19'),
(2, 'IGOR', '2019-10-02'),
(3, 'To Pimp A Butterfly', '2016-02-10'),
(4, 'My Dark Twisted Fantasy', '2010-12-25');

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
CREATE TABLE IF NOT EXISTS `artist` (
  `artist_id` int(11) NOT NULL,
  `name` text NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `type_of_art` text,
  PRIMARY KEY (`artist_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`artist_id`, `name`, `date_of_birth`, `type_of_art`) VALUES
(1, 'Kendrick Lamar', '1988-10-08', 'rapper'),
(2, 'kanye west', '1980-06-22', 'record producer'),
(3, 'Kid cudi', '1989-02-18', 'songwriter'),
(4, 'franck ocean', '1990-12-14', 'singer'),
(5, 'Tyler, the Creator', '1991-07-01', 'rapper');

-- --------------------------------------------------------

--
-- Table structure for table `feature`
--

DROP TABLE IF EXISTS `feature`;
CREATE TABLE IF NOT EXISTS `feature` (
  `album_id` int(11) DEFAULT NULL,
  `artist_id` int(11) DEFAULT NULL,
  `feature_id` int(11) NOT NULL,
  PRIMARY KEY (`feature_id`),
  KEY `album_id` (`album_id`),
  KEY `artist_id` (`artist_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `feature`
--

INSERT INTO `feature` (`album_id`, `artist_id`, `feature_id`) VALUES
(1, 4, 1),
(1, 2, 2),
(2, 5, 3),
(2, 3, 4),
(3, 4, 5),
(1, 3, 7),
(3, 1, 8),
(3, 2, 9),
(3, 4, 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
