-- phpMyAdmin SQL Dump
-- version 4.0.4.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2014 at 04:55 AM
-- Server version: 5.6.11
-- PHP Version: 5.5.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `softwaredevproject`
--
CREATE DATABASE IF NOT EXISTS `softwaredevproject` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `softwaredevproject`;

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE IF NOT EXISTS `content` (
  `slide_id` int(11) NOT NULL,
  `content_id` int(11) NOT NULL,
  `parentContent_id` int(11) DEFAULT NULL,
  `childContent_ids` varchar(255) NOT NULL,
  `layout_id` int(11) NOT NULL,
  `html` longtext NOT NULL,
  PRIMARY KEY (`slide_id`,`content_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `content`
--

INSERT INTO `content` (`slide_id`, `content_id`, `parentContent_id`, `childContent_ids`, `layout_id`, `html`) VALUES
(1, 1, NULL, '', 3, '<p>print("Hello World!");</p>');

-- --------------------------------------------------------

--
-- Table structure for table `layout`
--

CREATE TABLE IF NOT EXISTS `layout` (
  `layout_id` int(11) NOT NULL AUTO_INCREMENT,
  `layoutType` varchar(10) NOT NULL,
  PRIMARY KEY (`layout_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `layout`
--

INSERT INTO `layout` (`layout_id`, `layoutType`) VALUES
(1, 'L'),
(2, 'R'),
(3, 'F');

-- --------------------------------------------------------

--
-- Table structure for table `lessons`
--

CREATE TABLE IF NOT EXISTS `lessons` (
  `lesson_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `lessons`
--

INSERT INTO `lessons` (`lesson_id`, `title`, `description`) VALUES
(1, 'Hello World!', 'Outputting text'),
(2, 'Hello Universe!', 'Outputting more text');

-- --------------------------------------------------------

--
-- Table structure for table `lesssonsdone`
--

CREATE TABLE IF NOT EXISTS `lesssonsdone` (
  `email` varchar(100) NOT NULL,
  `lessson_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lesssonsdone`
--

INSERT INTO `lesssonsdone` (`email`, `lessson_id`) VALUES
('admin@admin.com', 1);

-- --------------------------------------------------------

--
-- Table structure for table `slides`
--

CREATE TABLE IF NOT EXISTS `slides` (
  `slide_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `slidePosition` int(11) NOT NULL,
  PRIMARY KEY (`slide_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `slides`
--

INSERT INTO `slides` (`slide_id`, `lesson_id`, `slidePosition`) VALUES
(1, 1, 1),
(2, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `firstName` varchar(60) NOT NULL,
  `lastName` varchar(60) NOT NULL,
  `joinDate` date NOT NULL,
  `birthday` date NOT NULL,
  `city` varchar(60) NOT NULL,
  `state` varchar(60) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `salt`, `is_admin`, `firstName`, `lastName`, `joinDate`, `birthday`, `city`, `state`) VALUES
('admin@admin.com', '3b5ce50041883bf41b7fe5946a1eecc89744efc7f5e551dca067dd3e9d1fe163', '821df218aa3a0fe113e745e868b2a90ec3361ffb29da27725fee1d588c823d5d', 1, 'ad', 'min', '2014-04-20', '2001-01-01', 'New York City', 'New York'),
('danfelizardo@gmail.com', '823b3e4dd59622c58a11184812b73396ffdd697f3c4bc35900d9d2fdc9a76b3f', 'c1cccf6609065ccfdae3ccc211732613366857e058fbc26fa33b126818b02159', 1, 'Dan', 'Felizardo', '2014-04-20', '1991-07-06', 'Danbury', 'Connecticut'),
('gulenak@gmail.com', 'c7b6a25bcc00bda531207db356db1d928ce5401ea7b5d94a6f339d12fd1e137e', '3745916f559c23f2451d817320e00e326f7f25857e404ff0bf8942ecc6779689', 1, 'Altan', 'Gulen', '2014-04-20', '1992-09-14', 'Framingham', 'Massachusetts'),
('tobias613.aaron@gmail.com', 'e457b7ca407f4cfa11649a23e978d3066042178b114ae499764355d299cd8487', '19287cc5d86e5425927e1e2618926dd7c68b2c8a681abcfa5d573d5772fd35f6', 1, 'Aaron', 'Tobias', '2014-04-20', '1992-03-10', 'Bridgeport', 'Connecticut');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `content`
--
ALTER TABLE `content`
  ADD CONSTRAINT `content_ibfk_1` FOREIGN KEY (`slide_id`) REFERENCES `slides` (`slide_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
