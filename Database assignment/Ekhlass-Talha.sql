-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 19, 2020 at 06:38 PM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gg`
--

-- --------------------------------------------------------

--
-- Table structure for table `apps`
--

CREATE TABLE `apps` (
  `app_id` int(11) NOT NULL,
  `name` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `apps`
--

INSERT INTO `apps` (`app_id`, `name`) VALUES
(1, 'linkedin'),
(2, 'medium'),
(3, 'quora'),
(4, 'openHub');

-- --------------------------------------------------------

--
-- Table structure for table `apps_users`
--

CREATE TABLE `apps_users` (
  `user_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  `user_name` text,
  `user_bio` text,
  `rate_of_usage` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `apps_users`
--

INSERT INTO `apps_users` (`user_id`, `app_id`, `user_name`, `user_bio`, `rate_of_usage`) VALUES
(1, 1, 'Ekhlass', 'human', '04:00:00'),
(2, 2, 'Aioub', 'human', '02:00:00'),
(1, 2, 'echo', 'human', '00:00:05'),
(1, 3, 'Humbty Dumbty ', 'human', '00:00:04'),
(4, 4, 'Luqman', 'human', '01:23:00'),
(4, 2, 'Luq22', 'human', '04:45:00'),
(6, 3, 'Ahm66', 'human', '03:11:00'),
(3, 4, 'Maya', 'human', '06:00:00'),
(5, 1, 'Ayoo', 'human', '04:34:00'),
(2, 1, 'Aioub', 'human', '03:30:00'),
(3, 1, 'Maria', 'human', '06:00:00'),
(4, 1, 'Luqman', 'human', '02:34:00'),
(5, 1, 'Ayaa00', 'human', '02:54:00'),
(6, 1, 'Ahmed7', 'human', '04:43:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` text,
  `age` int(11) DEFAULT NULL,
  `career` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `age`, `career`) VALUES
(1, 'Ekhlass', 19, 'developer'),
(2, 'Aioub', 25, 'translator'),
(3, 'Maria', 21, 'dentist'),
(4, 'Luqman', 26, 'translator'),
(5, 'Aya', 20, 'developer'),
(6, 'Ahmed', 23, 'designer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apps`
--
ALTER TABLE `apps`
  ADD PRIMARY KEY (`app_id`);

--
-- Indexes for table `apps_users`
--
ALTER TABLE `apps_users`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `app_id` (`app_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apps_users`
--
ALTER TABLE `apps_users`
  ADD CONSTRAINT `apps_users_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `apps_users_ibfk_2` FOREIGN KEY (`app_id`) REFERENCES `apps` (`app_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
