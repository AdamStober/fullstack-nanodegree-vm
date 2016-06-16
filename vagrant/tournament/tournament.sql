-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database "tournament" and connect to that database before creating tables
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE Players (
						ID serial primary key
					  , name text
					 );

CREATE TABLE Matches (
						 Match_ID serial primary key
						,winner int REFERENCES Players (ID)
						,loser int REFERENCES Players (ID)
						);

-- # CREATE TABLE Standings (name text, wins int);

--  A list of tuples, each of which contains (id, name, wins, matches):
--         id: the player's unique id (assigned by the database)
--         name: the player's full name (as registered)
--         wins: the number of matches the player has won
--         matches: the number of matches the player has played


CREATE OR REPLACE VIEW Wins_Per_Player AS
SELECT 
	  p.ID
	 ,p.name
	 ,count(m.winner) as wins
FROM Players p 
LEFT JOIN Matches m 
	ON  p.ID = m.winner
GROUP BY
	  p.ID
	,p.name;

CREATE OR REPLACE VIEW Matches_Per_Player AS
SELECT 
	  p.ID
	 ,p.name
	 ,count(m.winner) + count(m2.loser) as matches
FROM Players p 
LEFT JOIN Matches m 
	ON  p.ID = m.winner
LEFT JOIN Matches m2
	ON p.ID = m2.loser
GROUP BY
	  p.ID
	,p.name;

CREATE OR REPLACE VIEW Standings AS
SELECT 
	 Wins_Per_Player.ID
	,Wins_Per_Player.name
	,Wins_Per_Player.wins
	,Matches_Per_Player.matches
FROM Wins_Per_Player
LEFT JOIN Matches_Per_Player
	ON  Wins_Per_Player.ID = Matches_Per_Player.ID
ORDER BY
	  Wins_Per_Player.wins desc;


