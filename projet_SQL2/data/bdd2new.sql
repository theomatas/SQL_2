-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 22 déc. 2018 à 00:20
-- Version du serveur :  5.7.21
-- Version de PHP :  5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bdd2new`
--

-- --------------------------------------------------------

--
-- Structure de la table `cours`
--

DROP TABLE IF EXISTS `cours`;
CREATE TABLE IF NOT EXISTS `cours` (
  `CodeC` varchar(50) NOT NULL,
  `H_debut` varchar(50) NOT NULL,
  `H_fin` varchar(50) NOT NULL,
  `CodeS` varchar(50) NOT NULL,
  `MatriculeP` varchar(50) DEFAULT NULL,
  `NomGRP` varchar(50) NOT NULL,
  `DateC` varchar(50) NOT NULL,
  PRIMARY KEY (`CodeC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `cours`
--

INSERT INTO `cours` (`CodeC`, `H_debut`, `H_fin`, `CodeS`, `MatriculeP`, `NomGRP`, `DateC`) VALUES
('MATH1', '10-00', '11-45', '1', '1', 'C6', '21-11-18');

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
CREATE TABLE IF NOT EXISTS `etudiant` (
  `MatriculeE` varchar(50) NOT NULL,
  `NomE` varchar(50) NOT NULL,
  `PrenomE` varchar(50) NOT NULL,
  `Date_naissanceE` varchar(50) NOT NULL,
  `Ville_naissanceE` varchar(50) NOT NULL,
  `Pays_naissanceE` varchar(50) NOT NULL,
  `Sexe` varchar(50) NOT NULL,
  `Date_inscription` varchar(50) NOT NULL,
  `Etablissement_precedent` varchar(50) NOT NULL,
  `Photo` varchar(50) DEFAULT NULL,
  `Adresse_rueE` varchar(50) NOT NULL,
  `Code_postalE` varchar(50) NOT NULL,
  `VilleE` varchar(50) NOT NULL,
  `Tel_domicileE` varchar(50) NOT NULL,
  `Tel_mobileE` varchar(50) NOT NULL,
  `EmailE` varchar(50) NOT NULL,
  PRIMARY KEY (`MatriculeE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `etudiant`
--

INSERT INTO `etudiant` (`MatriculeE`, `NomE`, `PrenomE`, `Date_naissanceE`, `Ville_naissanceE`, `Pays_naissanceE`, `Sexe`, `Date_inscription`, `Etablissement_precedent`, `Photo`, `Adresse_rueE`, `Code_postalE`, `VilleE`, `Tel_domicileE`, `Tel_mobileE`, `EmailE`) VALUES
('20180014', 'Pinart', 'Antoine', '13-08-96', 'bordeau', 'france', 'M', '25-12-17', 'Mine', 'null', '15 clerge', '75006', 'paris', '1', '6', 'antoine.pinart@efrei.net'),
('20180886', 'Matas', 'Theo', '21-11-96', 'courcouronne', 'france', 'M', '25-15-17', 'EPITA', 'null', '664 rue des 18 sous', '77176', 'Nandy', '173511996', '695569880', 'theo.matas@efrei.net');

-- --------------------------------------------------------

--
-- Structure de la table `grp`
--

DROP TABLE IF EXISTS `grp`;
CREATE TABLE IF NOT EXISTS `grp` (
  `ID` varchar(50) NOT NULL,
  `NomGRP` varchar(50) NOT NULL,
  `MatriculeE` varchar(50) NOT NULL,
  `TypeGRP` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `grp`
--

INSERT INTO `grp` (`ID`, `NomGRP`, `MatriculeE`, `TypeGRP`) VALUES
('1', 'C6', '20180886', 'group'),
('11', '2021', '20180014', 'PROMO'),
('2', 'C6', '20180014', 'group'),
('20', '2020', '20180886', 'terter'),
('3', 'D', '20180014', 'group'),
('31', '2031', '20180886', 'terter'),
('32', '2032', '20180886', 'terter'),
('4', 'C', '20180886', 'group'),
('6', '1', '20180014', 'group'),
('7', '2021', '1', 'PROMO'),
('8', '2021', '1', 'PROMO'),
('9', 'WINER', '20180886', 'GROUP');

-- --------------------------------------------------------

--
-- Structure de la table `professeur`
--

DROP TABLE IF EXISTS `professeur`;
CREATE TABLE IF NOT EXISTS `professeur` (
  `MatriculeP` varchar(50) NOT NULL,
  `NomP` varchar(50) NOT NULL,
  `PrenomP` varchar(50) NOT NULL,
  `Adresse_rueP` varchar(50) DEFAULT NULL,
  `Code_postalP` varchar(50) DEFAULT NULL,
  `VilleP` varchar(50) DEFAULT NULL,
  `Tel_domicileP` varchar(50) DEFAULT NULL,
  `Tel_mobileP` varchar(50) DEFAULT NULL,
  `EmailP` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MatriculeP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `responsable`
--

DROP TABLE IF EXISTS `responsable`;
CREATE TABLE IF NOT EXISTS `responsable` (
  `MatriculeR` varchar(50) NOT NULL,
  `NomR` varchar(50) NOT NULL,
  `PrenomR` varchar(50) NOT NULL,
  `Adresse_rueR` varchar(50) NOT NULL,
  `Code_postalR` int(11) NOT NULL,
  `VilleR` varchar(50) NOT NULL,
  `Tel_mobileR` varchar(50) NOT NULL,
  `Tel_domicileR` varchar(50) NOT NULL,
  PRIMARY KEY (`MatriculeR`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

DROP TABLE IF EXISTS `salle`;
CREATE TABLE IF NOT EXISTS `salle` (
  `CodeS` varchar(50) NOT NULL,
  `NomS` varchar(50) NOT NULL,
  `Nb_places` int(11) NOT NULL,
  `TypeS` enum('AMPHI','COURS','LABO','SOUTENANCE') NOT NULL,
  PRIMARY KEY (`CodeS`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `salle`
--

INSERT INTO `salle` (`CodeS`, `NomS`, `Nb_places`, `TypeS`) VALUES
('1', 'e24', 40, 'AMPHI'),
('10', 'E10', 10, 'AMPHI'),
('13', 'E13', 13, 'AMPHI'),
('2', 'UNO', 1, 'LABO'),
('501', 'E501', 700, 'AMPHI'),
('502', 'E502', 500, 'AMPHI'),
('503', 'E503', 500, 'AMPHI'),
('507', 'E507', 20, 'AMPHI'),
('508', 'E508', 23, 'AMPHI'),
('57', 'E57', 57, 'AMPHI'),
('700', 'E700', 500, 'AMPHI');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
