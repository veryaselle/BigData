-- SQLINES DEMO ***  Distrib 5.7.33, for Linux (x86_64)
--
-- SQLINES DEMO ***   Database: spotifydb
-- SQLINES DEMO *** -------------------------------------
-- SQLINES DEMO *** 7.33-0ubuntu0.18.04.1

/* SQLINES DEMO *** ARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/* SQLINES DEMO *** ARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/* SQLINES DEMO *** LLATION_CONNECTION=@@COLLATION_CONNECTION */;
/* SQLINES DEMO *** tf8 */;
/* SQLINES DEMO *** ME_ZONE=@@TIME_ZONE */;
/* SQLINES DEMO *** NE='+00:00' */;
/* SQLINES DEMO *** IQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/* SQLINES DEMO *** REIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/* SQLINES DEMO *** L_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/* SQLINES DEMO *** L_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- SQLINES DEMO *** or table `album`
--

DROP TABLE IF EXISTS album;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE album (
  id varchar(100) NOT NULL,
  name varchar(500) DEFAULT NULL,
  uri varchar(1000) DEFAULT NULL,
  PRIMARY KEY (id)
) ;
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** or table `artist`
--

DROP TABLE IF EXISTS artist;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE artist (
  id varchar(100) NOT NULL,
  name varchar(500) DEFAULT NULL,
  uri varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
) ;
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** or table `playlist`
--

DROP TABLE IF EXISTS playlist;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE playlist (
  id varchar(100) NOT NULL,
  name varchar(500) NOT NULL,
  followers int DEFAULT NULL,
  uri varchar(1000) DEFAULT NULL,
  total_tracks int NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX p_name_idx ON playlist (name);
CREATE INDEX p_total_tracks_idx ON playlist (total_tracks);
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** or table `track`
--

DROP TABLE IF EXISTS track;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE track (
  id varchar(100) NOT NULL,
  name varchar(500) DEFAULT NULL,
  duration int DEFAULT NULL,
  popularity double precision DEFAULT NULL,
  explicit varchar(10) DEFAULT NULL,
  preview_url varchar(10000) DEFAULT NULL,
  uri varchar(1000) DEFAULT NULL,
  album_id varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
,
  CONSTRAINT album_id FOREIGN KEY (album_id) REFERENCES album (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;

CREATE INDEX album_id_idx ON track (album_id);
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** or table `track_artist1`
--

DROP TABLE IF EXISTS track_artist1;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE track_artist1 (
  track_id varchar(100) DEFAULT NULL,
  artist_id varchar(100) DEFAULT NULL,
  CONSTRAINT unique_index UNIQUE  (track_id,artist_id)
,
  CONSTRAINT ta_artist_id1 FOREIGN KEY (artist_id) REFERENCES artist (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT ta_track_id1 FOREIGN KEY (track_id) REFERENCES track (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;

CREATE INDEX track_id_idx ON track_artist1 (track_id);
CREATE INDEX artist_id_idx ON track_artist1 (artist_id);
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** or table `track_playlist1`
--

DROP TABLE IF EXISTS track_playlist1;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE track_playlist1 (
  track_id varchar(100) DEFAULT NULL,
  playlist_id varchar(100) DEFAULT NULL,
  CONSTRAINT unique_index1 UNIQUE  (track_id,playlist_id)
,
  CONSTRAINT tp_playlist_id1 FOREIGN KEY (playlist_id) REFERENCES playlist (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT tp_track_id1 FOREIGN KEY (track_id) REFERENCES track (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ;

CREATE INDEX track_id_idx1 ON track_playlist1 (track_id);
CREATE INDEX playlist_id_idx1 ON track_playlist1 (playlist_id);
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;
/* SQLINES DEMO *** NE=@OLD_TIME_ZONE */;

/* SQLINES DEMO *** E=@OLD_SQL_MODE */;
/* SQLINES DEMO *** _KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/* SQLINES DEMO *** CHECKS=@OLD_UNIQUE_CHECKS */;
/* SQLINES DEMO *** ER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/* SQLINES DEMO *** ER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/* SQLINES DEMO *** ON_CONNECTION=@OLD_COLLATION_CONNECTION */;
/* SQLINES DEMO *** ES=@OLD_SQL_NOTES */;

-- SQLINES DEMO ***  2021-02-11 15:42:39