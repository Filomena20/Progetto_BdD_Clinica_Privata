-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Giu 12, 2025 alle 16:28
-- Versione del server: 10.11.11-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinica`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add user', 3, 'add_user'),
(10, 'Can change user', 3, 'change_user'),
(11, 'Can delete user', 3, 'delete_user'),
(12, 'Can view user', 3, 'view_user'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add amministratore_ clinica', 6, 'add_amministratore_clinica'),
(22, 'Can change amministratore_ clinica', 6, 'change_amministratore_clinica'),
(23, 'Can delete amministratore_ clinica', 6, 'delete_amministratore_clinica'),
(24, 'Can view amministratore_ clinica', 6, 'view_amministratore_clinica'),
(25, 'Can add evento', 7, 'add_evento'),
(26, 'Can change evento', 7, 'change_evento'),
(27, 'Can delete evento', 7, 'delete_evento'),
(28, 'Can view evento', 7, 'view_evento'),
(29, 'Can add paziente', 8, 'add_paziente'),
(30, 'Can change paziente', 8, 'change_paziente'),
(31, 'Can delete paziente', 8, 'delete_paziente'),
(32, 'Can view paziente', 8, 'view_paziente'),
(33, 'Can add personale', 9, 'add_personale'),
(34, 'Can change personale', 9, 'change_personale'),
(35, 'Can delete personale', 9, 'delete_personale'),
(36, 'Can view personale', 9, 'view_personale'),
(37, 'Can add cartella_ clinica', 10, 'add_cartella_clinica'),
(38, 'Can change cartella_ clinica', 10, 'change_cartella_clinica'),
(39, 'Can delete cartella_ clinica', 10, 'delete_cartella_clinica'),
(40, 'Can view cartella_ clinica', 10, 'view_cartella_clinica'),
(41, 'Can add iscrizione', 11, 'add_iscrizione'),
(42, 'Can change iscrizione', 11, 'change_iscrizione'),
(43, 'Can delete iscrizione', 11, 'delete_iscrizione'),
(44, 'Can view iscrizione', 11, 'view_iscrizione'),
(45, 'Can add gestione', 12, 'add_gestione'),
(46, 'Can change gestione', 12, 'change_gestione'),
(47, 'Can delete gestione', 12, 'delete_gestione'),
(48, 'Can view gestione', 12, 'view_gestione'),
(49, 'Can add trattamento', 13, 'add_trattamento'),
(50, 'Can change trattamento', 13, 'change_trattamento'),
(51, 'Can delete trattamento', 13, 'delete_trattamento'),
(52, 'Can view trattamento', 13, 'view_trattamento'),
(53, 'Can add svolgimento', 14, 'add_svolgimento'),
(54, 'Can change svolgimento', 14, 'change_svolgimento'),
(55, 'Can delete svolgimento', 14, 'delete_svolgimento'),
(56, 'Can view svolgimento', 14, 'view_svolgimento'),
(57, 'Can add recensione', 15, 'add_recensione'),
(58, 'Can change recensione', 15, 'change_recensione'),
(59, 'Can delete recensione', 15, 'delete_recensione'),
(60, 'Can view recensione', 15, 'view_recensione'),
(61, 'Can add prenotazione', 16, 'add_prenotazione'),
(62, 'Can change prenotazione', 16, 'change_prenotazione'),
(63, 'Can delete prenotazione', 16, 'delete_prenotazione'),
(64, 'Can view prenotazione', 16, 'view_prenotazione');

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_amministratore_clinica`
--

CREATE TABLE `clinica_amministratore_clinica` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `codice_fiscale` varchar(16) NOT NULL,
  `cellulare` varchar(20) NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_amministratore_clinica`
--

INSERT INTO `clinica_amministratore_clinica` (`id`, `email`, `password`, `nome`, `cognome`, `codice_fiscale`, `cellulare`, `data_nascita`) VALUES
(1, 'amministratore@clinica.it', 'ee9be523dd11cd9eaf53926c987a2ea9', 'Giulia', 'Ambrosio', 'MBRGLU86R51F205', '393401234567', '1986-10-11');

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_cartella_clinica`
--

CREATE TABLE `clinica_cartella_clinica` (
  `id` bigint(20) NOT NULL,
  `data_apertura` date NOT NULL,
  `diagnosi` longtext NOT NULL,
  `prescrizioni` longtext DEFAULT NULL,
  `data_chiusura` date DEFAULT NULL,
  `paziente_id` bigint(20) NOT NULL,
  `trattamento_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_cartella_clinica`
--

INSERT INTO `clinica_cartella_clinica` (`id`, `data_apertura`, `diagnosi`, `prescrizioni`, `data_chiusura`, `paziente_id`, `trattamento_id`) VALUES
(10, '2025-06-12', 'Il paziente presenta una postura scorretta caratterizzata da iperlordosi lombare, spalle anteposte e inclinazione anteriore del bacino. Si evidenziano dolori muscolari ricorrenti nella regione cervicale e lombare, rigidità articolare e affaticamento posturale. La sintomatologia è compatibile con un\'alterazione degli equilibri mio-fasciali, probabilmente dovuta a sedentarietà prolungata e abitudini posturali scorrette. È indicato un trattamento di riabilitazione posturale volto al riequilibrio muscolare e al miglioramento della propriocezione.', '– Ciclo di 10 sedute di riabilitazione posturale con frequenza bisettimanale\r\n– Esercizi di allungamento per catene muscolari posteriori (ischiocrurali, paravertebrali)\r\n– Esercizi di rinforzo per addominali profondi (core stability)\r\n– Tecniche di respirazione diaframmatica e rilassamento muscolare\r\n– Educazione posturale con correzione delle abitudini quotidiane (posizione da seduto, uso del PC, ecc.)\r\n– Controllo posturale a 30 giorni con rivalutazione clinica', NULL, 1, 4),
(11, '2025-06-12', 'Il paziente presenta deviazione del setto nasale con ostruzione respiratoria cronica, accentuata durante le ore notturne e in presenza di allergeni. Si evidenziano inoltre irregolarità morfologiche del dorso e della punta del naso, con impatto estetico significativo e compromissione della qualità di vita. L’intervento chirurgico di rinoplastica, associato a settoplastica funzionale, è indicato per il ripristino della normale pervietà delle vie aeree superiori e il miglioramento dell’armonia estetica del profilo nasale.', '– Riposo domiciliare per almeno 7 giorni, con testa sollevata durante il sonno per ridurre l’edema\r\n– Applicazione di impacchi freddi sulle guance (evitando il naso) nelle prime 48 ore\r\n– Antibioticoterapia per 5-7 giorni secondo prescrizione medica (es. amoxicillina/acido clavulanico)\r\n– Analgesici al bisogno (es. paracetamolo o ibuprofene) evitando farmaci anticoagulanti\r\n– Evitare soffi nasali, starnuti violenti e attività fisica intensa per almeno 3 settimane\r\n– Pulizia delicata delle narici con soluzione fisiologica due volte al giorno\r\n– Rimozione dei tamponi nasali secondo indicazione del chirurgo (di solito dopo 48-72 ore)\r\n– Controllo ambulatoriale a 7 e 30 giorni dall’intervento\r\n– Evitare l’esposizione diretta al sole e l’uso di occhiali per almeno 4 settimane', NULL, 5, 5);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_evento`
--

CREATE TABLE `clinica_evento` (
  `id` bigint(20) NOT NULL,
  `data` date NOT NULL,
  `titolo` varchar(200) NOT NULL,
  `descrizione` longtext NOT NULL,
  `presenze_effettive` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_evento`
--

INSERT INTO `clinica_evento` (`id`, `data`, `titolo`, `descrizione`, `presenze_effettive`) VALUES
(1, '2025-06-15', 'Giornata della Prevenzione', 'Evento gratuito con screening medici e consulenze specialistiche.', 1),
(2, '2025-07-01', 'Incontro sul Benessere Mentale', 'Conferenza con psicologi e terapeuti per promuovere la salute mentale.', 1),
(3, '2025-08-20', 'Open Day Nutrizione', 'Sessioni informative con nutrizionisti su alimentazione equilibrata.', 0),
(4, '2025-09-10', 'Seminario sul Dolore Cronico', 'Approfondimento su trattamenti innovativi per la gestione del dolore.', 1),
(5, '2025-10-05', 'Corso di Primo Soccorso', 'Formazione pratica su tecniche di primo soccorso aperta al pubblico.', 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_gestione`
--

CREATE TABLE `clinica_gestione` (
  `id` bigint(20) NOT NULL,
  `cartella_id` bigint(20) NOT NULL,
  `personale_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_gestione`
--

INSERT INTO `clinica_gestione` (`id`, `cartella_id`, `personale_id`) VALUES
(7, 10, 2),
(8, 11, 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_iscrizione`
--

CREATE TABLE `clinica_iscrizione` (
  `id` bigint(20) NOT NULL,
  `data_iscrizione` date NOT NULL,
  `presente` tinyint(1) NOT NULL,
  `stato` varchar(50) NOT NULL,
  `evento_id` bigint(20) NOT NULL,
  `paziente_id` bigint(20) DEFAULT NULL,
  `personale_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_iscrizione`
--

INSERT INTO `clinica_iscrizione` (`id`, `data_iscrizione`, `presente`, `stato`, `evento_id`, `paziente_id`, `personale_id`) VALUES
(28, '2025-06-07', 0, 'annullato', 3, 1, NULL),
(29, '2025-06-08', 1, 'iscritto', 1, 5, NULL),
(32, '2025-06-08', 0, 'annullato', 3, 5, NULL),
(35, '2025-06-08', 0, 'iscritto', 2, 5, NULL),
(36, '2025-06-08', 0, 'annullato', 4, 5, NULL),
(37, '2025-06-08', 0, 'annullato', 5, 5, NULL),
(39, '2025-06-08', 0, 'annullato', 2, 1, NULL),
(40, '2025-06-08', 0, 'annullato', 4, 1, NULL),
(41, '2025-06-08', 0, 'iscritto', 5, 1, NULL),
(42, '2025-06-08', 0, 'annullato', 1, 1, NULL),
(43, '2025-06-08', 0, 'annullato', 1, NULL, 1),
(44, '2025-06-08', 0, 'annullato', 2, NULL, 1),
(45, '2025-06-08', 0, 'annullato', 3, NULL, 1),
(46, '2025-06-08', 0, 'iscritto', 4, NULL, 1),
(47, '2025-06-08', 0, 'annullato', 5, NULL, 1),
(48, '2025-06-08', 0, 'annullato', 1, NULL, 2),
(49, '2025-06-08', 0, 'annullato', 2, NULL, 2),
(50, '2025-06-08', 0, 'iscritto', 3, NULL, 2),
(51, '2025-06-08', 0, 'iscritto', 4, NULL, 2),
(52, '2025-06-08', 0, 'annullato', 5, NULL, 2);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_paziente`
--

CREATE TABLE `clinica_paziente` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `codice_fiscale` varchar(16) NOT NULL,
  `patologie` longtext DEFAULT NULL,
  `allergie` longtext DEFAULT NULL,
  `cellulare` varchar(20) NOT NULL,
  `indirizzo` varchar(255) NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_paziente`
--

INSERT INTO `clinica_paziente` (`id`, `email`, `password`, `nome`, `cognome`, `codice_fiscale`, `patologie`, `allergie`, `cellulare`, `indirizzo`, `data_nascita`) VALUES
(1, 'paziente1@clinica.it', '56be6ffab16b923169d596dab2d1704c', 'Anna', 'Bianchi', 'BNCHAN85B41H501X', 'Asma', 'Polline', '3331234567', 'Via Roma 10, Milano', '1985-05-15'),
(5, 'paziente2@clinica.it', 'ab66263da1f85140a1e9ccaa9b311751', 'Giovanni', 'Vastola', 'VSTGNN21D04H501Y', 'Diabete', '', '3381234567', 'Via Roma 45, Salerno', '2001-04-04'),
(12, 'paziente3@clinica.it', '0dead8b7984694ef56b3beb8f655a104', 'Lara', 'Ammirati', 'AMMLRA04C51F205', '', 'Acari', '3215869741', 'Via delle Orate 5, Biella', '2004-03-11');

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_personale`
--

CREATE TABLE `clinica_personale` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `ruolo` enum('Medico','Operatore Sanitario') NOT NULL,
  `codice_fiscale` varchar(16) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `data_nascita` date NOT NULL,
  `orario_lavoro` varchar(100) NOT NULL,
  `cellulare` varchar(20) NOT NULL,
  `specializzazione` varchar(100) DEFAULT NULL,
  `reparto` varchar(100) DEFAULT NULL,
  `qualifica` varchar(100) DEFAULT NULL,
  `mansione` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_personale`
--

INSERT INTO `clinica_personale` (`id`, `email`, `password`, `ruolo`, `codice_fiscale`, `nome`, `cognome`, `data_nascita`, `orario_lavoro`, `cellulare`, `specializzazione`, `reparto`, `qualifica`, `mansione`) VALUES
(1, 'medico1@clinica.it', 'd893c7b6552de034609ef33f5f0b3211', 'Medico', 'RSSMRA80A01H501U', 'Mario', 'Rossi', '1980-01-01', '08:00-20:00', '3457281943', 'Chirurgia estetica e generale', 'Chirurgia', NULL, NULL),
(2, 'operatore1@clinica.it', '87d9fd452c81d4baa9e031539c3bccd3', 'Operatore Sanitario', 'VRDLGI90B12F205X', 'Luigi', 'Verdi', '1990-02-12', '8:00-20:00', '3339876543', NULL, NULL, 'Fisioterapista', 'Riabilitazione Motoria');

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_prenotazione`
--

CREATE TABLE `clinica_prenotazione` (
  `id` bigint(20) NOT NULL,
  `data` date NOT NULL,
  `ora` time(6) NOT NULL,
  `durata` int(10) UNSIGNED NOT NULL CHECK (`durata` >= 0),
  `stato` varchar(30) NOT NULL,
  `paziente_id` bigint(20) NOT NULL,
  `personale_id` bigint(20) DEFAULT NULL,
  `trattamento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_prenotazione`
--

INSERT INTO `clinica_prenotazione` (`id`, `data`, `ora`, `durata`, `stato`, `paziente_id`, `personale_id`, `trattamento_id`) VALUES
(7, '2025-06-10', '12:30:00.000000', 30, 'cancellata', 5, 1, 5),
(8, '2025-06-20', '11:30:00.000000', 30, 'cancellata', 1, 2, 4),
(9, '2025-06-14', '16:00:00.000000', 30, 'confermata', 1, 2, 4),
(10, '2025-06-26', '09:30:00.000000', 30, 'confermata', 5, 1, 5),
(11, '2025-06-16', '09:00:00.000000', 30, 'richiesta', 12, 1, 14);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_recensione`
--

CREATE TABLE `clinica_recensione` (
  `id` bigint(20) NOT NULL,
  `testo` longtext NOT NULL,
  `valutazione` smallint(5) UNSIGNED NOT NULL CHECK (`valutazione` >= 0),
  `paziente_id` bigint(20) NOT NULL,
  `trattamento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_recensione`
--

INSERT INTO `clinica_recensione` (`id`, `testo`, `valutazione`, `paziente_id`, `trattamento_id`) VALUES
(5, 'Personale professionale e qualificato.', 5, 1, 4);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_svolgimento`
--

CREATE TABLE `clinica_svolgimento` (
  `id` bigint(20) NOT NULL,
  `personale_id` bigint(20) NOT NULL,
  `trattamento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_svolgimento`
--

INSERT INTO `clinica_svolgimento` (`id`, `personale_id`, `trattamento_id`) VALUES
(4, 2, 4),
(5, 1, 5);

-- --------------------------------------------------------

--
-- Struttura della tabella `clinica_trattamento`
--

CREATE TABLE `clinica_trattamento` (
  `id` bigint(20) NOT NULL,
  `tipo` enum('Ricovero','Riabilitazione') NOT NULL,
  `costo` decimal(8,2) NOT NULL,
  `note` longtext DEFAULT NULL,
  `data_inizio` date DEFAULT NULL,
  `data_fine` date DEFAULT NULL,
  `stanza` varchar(10) DEFAULT NULL,
  `durata` int(11) DEFAULT NULL,
  `gestore_id` bigint(20) DEFAULT NULL,
  `paziente_id` bigint(20) DEFAULT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clinica_trattamento`
--

INSERT INTO `clinica_trattamento` (`id`, `tipo`, `costo`, `note`, `data_inizio`, `data_fine`, `stanza`, `durata`, `gestore_id`, `paziente_id`, `nome`) VALUES
(4, 'Riabilitazione', 200.00, 'Sovvenzione SSN', NULL, NULL, NULL, 1, 1, 5, 'Riabilitazione Posturale'),
(5, 'Ricovero', 300.00, 'Rinoplastica', '2025-06-26', '2025-06-27', '5', NULL, 1, NULL, 'Ricovero Chirurgico'),
(13, 'Ricovero', 80.00, 'Sovvenzione SSN', NULL, NULL, '', NULL, 1, NULL, 'Riabilitazione Ortopedica'),
(14, 'Ricovero', 800.00, 'Check-up completo (una settimana)', NULL, NULL, '', NULL, 1, NULL, 'Ricovero Ordinario');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(3, 'auth', 'user'),
(6, 'Clinica', 'amministratore_clinica'),
(10, 'Clinica', 'cartella_clinica'),
(7, 'Clinica', 'evento'),
(12, 'Clinica', 'gestione'),
(11, 'Clinica', 'iscrizione'),
(8, 'Clinica', 'paziente'),
(9, 'Clinica', 'personale'),
(16, 'Clinica', 'prenotazione'),
(15, 'Clinica', 'recensione'),
(14, 'Clinica', 'svolgimento'),
(13, 'Clinica', 'trattamento'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Clinica', '0001_initial', '2025-06-06 14:53:18.974303'),
(2, 'contenttypes', '0001_initial', '2025-06-06 14:53:19.025463'),
(3, 'contenttypes', '0002_remove_content_type_name', '2025-06-06 14:53:19.059813'),
(4, 'auth', '0001_initial', '2025-06-06 14:53:19.272506'),
(5, 'auth', '0002_alter_permission_name_max_length', '2025-06-06 14:53:19.306538'),
(6, 'auth', '0003_alter_user_email_max_length', '2025-06-06 14:53:19.322447'),
(7, 'auth', '0004_alter_user_username_opts', '2025-06-06 14:53:19.329572'),
(8, 'auth', '0005_alter_user_last_login_null', '2025-06-06 14:53:19.352094'),
(9, 'auth', '0006_require_contenttypes_0002', '2025-06-06 14:53:19.354474'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2025-06-06 14:53:19.359614'),
(11, 'auth', '0008_alter_user_username_max_length', '2025-06-06 14:53:19.376223'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2025-06-06 14:53:19.391301'),
(13, 'auth', '0010_alter_group_name_max_length', '2025-06-06 14:53:19.406495'),
(14, 'auth', '0011_update_proxy_permissions', '2025-06-06 14:53:19.416444'),
(15, 'auth', '0012_alter_user_first_name_max_length', '2025-06-06 14:53:19.433397'),
(16, 'sessions', '0001_initial', '2025-06-06 14:53:19.453698'),
(17, 'Clinica', '0002_trattamento_nome', '2025-06-07 16:02:50.752975'),
(18, 'Clinica', '0003_alter_trattamento_paziente', '2025-06-08 15:39:54.565968'),
(19, 'Clinica', '0004_alter_iscrizione_stato', '2025-06-09 09:28:01.652700'),
(20, 'Clinica', '0005_alter_prenotazione_stato', '2025-06-09 18:42:22.205124');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indici per le tabelle `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indici per le tabelle `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indici per le tabelle `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indici per le tabelle `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `clinica_amministratore_clinica`
--
ALTER TABLE `clinica_amministratore_clinica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `codice_fiscale` (`codice_fiscale`);

--
-- Indici per le tabelle `clinica_cartella_clinica`
--
ALTER TABLE `clinica_cartella_clinica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `paziente_id` (`paziente_id`),
  ADD KEY `Clinica_cartella_cli_trattamento_id_35fede4b_fk_Clinica_t` (`trattamento_id`);

--
-- Indici per le tabelle `clinica_evento`
--
ALTER TABLE `clinica_evento`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `clinica_gestione`
--
ALTER TABLE `clinica_gestione`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_gestione_cartella_id_a842f799_fk_Clinica_c` (`cartella_id`),
  ADD KEY `Clinica_gestione_personale_id_507c26e0_fk_Clinica_personale_id` (`personale_id`);

--
-- Indici per le tabelle `clinica_iscrizione`
--
ALTER TABLE `clinica_iscrizione`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_iscrizione_evento_id_278044ab_fk_Clinica_evento_id` (`evento_id`),
  ADD KEY `Clinica_iscrizione_paziente_id_c320ef35_fk_Clinica_paziente_id` (`paziente_id`),
  ADD KEY `Clinica_iscrizione_personale_id_f625fac8_fk_Clinica_personale_id` (`personale_id`);

--
-- Indici per le tabelle `clinica_paziente`
--
ALTER TABLE `clinica_paziente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `codice_fiscale` (`codice_fiscale`);

--
-- Indici per le tabelle `clinica_personale`
--
ALTER TABLE `clinica_personale`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `codice_fiscale` (`codice_fiscale`);

--
-- Indici per le tabelle `clinica_prenotazione`
--
ALTER TABLE `clinica_prenotazione`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_prenotazione_paziente_id_6194becd_fk_Clinica_paziente_id` (`paziente_id`),
  ADD KEY `Clinica_prenotazione_personale_id_7090e90c_fk_Clinica_p` (`personale_id`),
  ADD KEY `Clinica_prenotazione_trattamento_id_2421b49d_fk_Clinica_t` (`trattamento_id`);

--
-- Indici per le tabelle `clinica_recensione`
--
ALTER TABLE `clinica_recensione`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_recensione_paziente_id_6f32db74_fk_Clinica_paziente_id` (`paziente_id`),
  ADD KEY `Clinica_recensione_trattamento_id_bc10f473_fk_Clinica_t` (`trattamento_id`);

--
-- Indici per le tabelle `clinica_svolgimento`
--
ALTER TABLE `clinica_svolgimento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_svolgimento_personale_id_5d4dbde8_fk_Clinica_p` (`personale_id`),
  ADD KEY `Clinica_svolgimento_trattamento_id_c6e47e3b_fk_Clinica_t` (`trattamento_id`);

--
-- Indici per le tabelle `clinica_trattamento`
--
ALTER TABLE `clinica_trattamento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Clinica_trattamento_gestore_id_bd6e1219_fk_Clinica_a` (`gestore_id`),
  ADD KEY `Clinica_trattamento_paziente_id_c929b79a_fk_Clinica_paziente_id` (`paziente_id`);

--
-- Indici per le tabelle `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indici per le tabelle `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT per la tabella `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `clinica_amministratore_clinica`
--
ALTER TABLE `clinica_amministratore_clinica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT per la tabella `clinica_cartella_clinica`
--
ALTER TABLE `clinica_cartella_clinica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT per la tabella `clinica_evento`
--
ALTER TABLE `clinica_evento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT per la tabella `clinica_gestione`
--
ALTER TABLE `clinica_gestione`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT per la tabella `clinica_iscrizione`
--
ALTER TABLE `clinica_iscrizione`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT per la tabella `clinica_paziente`
--
ALTER TABLE `clinica_paziente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT per la tabella `clinica_personale`
--
ALTER TABLE `clinica_personale`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `clinica_prenotazione`
--
ALTER TABLE `clinica_prenotazione`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT per la tabella `clinica_recensione`
--
ALTER TABLE `clinica_recensione`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `clinica_svolgimento`
--
ALTER TABLE `clinica_svolgimento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `clinica_trattamento`
--
ALTER TABLE `clinica_trattamento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT per la tabella `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT per la tabella `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Limiti per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Limiti per la tabella `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limiti per la tabella `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limiti per la tabella `clinica_cartella_clinica`
--
ALTER TABLE `clinica_cartella_clinica`
  ADD CONSTRAINT `Clinica_cartella_cli_paziente_id_20522147_fk_Clinica_p` FOREIGN KEY (`paziente_id`) REFERENCES `clinica_paziente` (`id`),
  ADD CONSTRAINT `Clinica_cartella_cli_trattamento_id_35fede4b_fk_Clinica_t` FOREIGN KEY (`trattamento_id`) REFERENCES `clinica_trattamento` (`id`);

--
-- Limiti per la tabella `clinica_gestione`
--
ALTER TABLE `clinica_gestione`
  ADD CONSTRAINT `Clinica_gestione_cartella_id_a842f799_fk_Clinica_c` FOREIGN KEY (`cartella_id`) REFERENCES `clinica_cartella_clinica` (`id`),
  ADD CONSTRAINT `Clinica_gestione_personale_id_507c26e0_fk_Clinica_personale_id` FOREIGN KEY (`personale_id`) REFERENCES `clinica_personale` (`id`);

--
-- Limiti per la tabella `clinica_iscrizione`
--
ALTER TABLE `clinica_iscrizione`
  ADD CONSTRAINT `Clinica_iscrizione_evento_id_278044ab_fk_Clinica_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `clinica_evento` (`id`),
  ADD CONSTRAINT `Clinica_iscrizione_paziente_id_c320ef35_fk_Clinica_paziente_id` FOREIGN KEY (`paziente_id`) REFERENCES `clinica_paziente` (`id`),
  ADD CONSTRAINT `Clinica_iscrizione_personale_id_f625fac8_fk_Clinica_personale_id` FOREIGN KEY (`personale_id`) REFERENCES `clinica_personale` (`id`);

--
-- Limiti per la tabella `clinica_prenotazione`
--
ALTER TABLE `clinica_prenotazione`
  ADD CONSTRAINT `Clinica_prenotazione_paziente_id_6194becd_fk_Clinica_paziente_id` FOREIGN KEY (`paziente_id`) REFERENCES `clinica_paziente` (`id`),
  ADD CONSTRAINT `Clinica_prenotazione_personale_id_7090e90c_fk_Clinica_p` FOREIGN KEY (`personale_id`) REFERENCES `clinica_personale` (`id`),
  ADD CONSTRAINT `Clinica_prenotazione_trattamento_id_2421b49d_fk_Clinica_t` FOREIGN KEY (`trattamento_id`) REFERENCES `clinica_trattamento` (`id`);

--
-- Limiti per la tabella `clinica_recensione`
--
ALTER TABLE `clinica_recensione`
  ADD CONSTRAINT `Clinica_recensione_paziente_id_6f32db74_fk_Clinica_paziente_id` FOREIGN KEY (`paziente_id`) REFERENCES `clinica_paziente` (`id`),
  ADD CONSTRAINT `Clinica_recensione_trattamento_id_bc10f473_fk_Clinica_t` FOREIGN KEY (`trattamento_id`) REFERENCES `clinica_trattamento` (`id`);

--
-- Limiti per la tabella `clinica_svolgimento`
--
ALTER TABLE `clinica_svolgimento`
  ADD CONSTRAINT `Clinica_svolgimento_personale_id_5d4dbde8_fk_Clinica_p` FOREIGN KEY (`personale_id`) REFERENCES `clinica_personale` (`id`),
  ADD CONSTRAINT `Clinica_svolgimento_trattamento_id_c6e47e3b_fk_Clinica_t` FOREIGN KEY (`trattamento_id`) REFERENCES `clinica_trattamento` (`id`);

--
-- Limiti per la tabella `clinica_trattamento`
--
ALTER TABLE `clinica_trattamento`
  ADD CONSTRAINT `Clinica_trattamento_gestore_id_bd6e1219_fk_Clinica_a` FOREIGN KEY (`gestore_id`) REFERENCES `clinica_amministratore_clinica` (`id`),
  ADD CONSTRAINT `Clinica_trattamento_paziente_id_c929b79a_fk_Clinica_paziente_id` FOREIGN KEY (`paziente_id`) REFERENCES `clinica_paziente` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
