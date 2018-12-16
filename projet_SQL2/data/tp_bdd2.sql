







DROP TABLE IF EXISTS `cours`;
CREATE TABLE IF NOT EXISTS `cours` (
  `Code_cours` int(11) NOT NULL,
  `H_debut` time NOT NULL,
  `H_fin` time NOT NULL,
  `salle` varchar(50) DEFAULT NULL,
  `professeur` varchar(50) DEFAULT NULL,
  `grp` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Code_cours`),
  KEY `VFV` (`salle`),
  KEY `VFm` (`professeur`),
  KEY `VFo` (`grp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `cours`
--

INSERT INTO `cours` (`Code_cours`, `H_debut`, `H_fin`, `salle`, `professeur`, `grp`) VALUES
(33, '00:00:12', '00:00:14', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
CREATE TABLE IF NOT EXISTS `etudiant` (
  `MatriculeE` varchar(50) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Date_naissance` date NOT NULL,
  `Ville_naissance` varchar(50) NOT NULL,
  `Pays_naissance` varchar(50) NOT NULL,
  `Sexe` tinyint(1) NOT NULL,
  `Date_inscription` date NOT NULL,
  `Etablissement_precedent` varchar(50) NOT NULL,
  `Photo` varchar(50) NOT NULL,
  `Nom_rue` varchar(50) NOT NULL,
  `Numero` int(11) NOT NULL,
  `Code_postal` int(11) NOT NULL,
  `Ville` varchar(50) NOT NULL,
  `Tel_domicile` varchar(50) NOT NULL,
  `Tel_mobile` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `MatriculeR` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MatriculeE`),
  KEY `VFs` (`MatriculeR`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `grp`
--

DROP TABLE IF EXISTS `grp`;
CREATE TABLE IF NOT EXISTS `grp` (
  `Code_cours` int(11) NOT NULL,
  `MatriculeE` varchar(50) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Type` enum('PROMO','TD') NOT NULL,
  PRIMARY KEY (`Code_cours`,`MatriculeE`),
  KEY `Code_cours` (`Code_cours`),
  KEY `MatriculeE` (`MatriculeE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `professeur`
--

DROP TABLE IF EXISTS `professeur`;
CREATE TABLE IF NOT EXISTS `professeur` (
  `MatriculeP` varchar(50) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Code_postal` varchar(50) NOT NULL,
  `Nom_rue` varchar(50) NOT NULL,
  `Numero` int(11) NOT NULL,
  `Ville` varchar(50) NOT NULL,
  `Tel_domicile` varchar(50) NOT NULL,
  `Tel_mobile` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`MatriculeP`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `responsable`
--

DROP TABLE IF EXISTS `responsable`;
CREATE TABLE IF NOT EXISTS `responsable` (
  `MatriculeR` varchar(50) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Rue` varchar(50) NOT NULL,
  `Numero` int(11) NOT NULL,
  `Code_postal` int(5) NOT NULL,
  `Ville` varchar(50) NOT NULL,
  `MatriculeE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MatriculeR`),
  KEY `VFoi` (`MatriculeE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

DROP TABLE IF EXISTS `salle`;
CREATE TABLE IF NOT EXISTS `salle` (
  `Code` int(11) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Nb_places` int(11) NOT NULL,
  `Type` enum('AMPHI','LABO','COURS','SOUTENANCE') NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `salle`
--

INSERT INTO `salle` (`Code`, `Nom`, `Nb_places`, `Type`) VALUES
(4, 'E15', 25, 'COURS'),
(3, 'room', 500, 'COURS'),
(7, 'E25', 25, 'COURS'),
(6, 'room', 500, 'COURS'),
(45, 'mama', 500, 'AMPHI');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
