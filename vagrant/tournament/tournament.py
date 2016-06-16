#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    conn = psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    query = "DELETE FROM Matches;"
    c.execute(query)
    conn.commit() 
    conn.close() 

def deletePlayers():
    """Remove all the player records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    query = "DELETE FROM Players;"
    c.execute(query)
    conn.commit() 
    conn.close() 

def countPlayers():
    """Returns the number of players currently registered."""
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    query = "SELECT COUNT (*) from Players;"
    c.execute(query)
    result = c.fetchall()
    #print 'res is %s\n\n' % result
    conn.close()
    #print 'CountPlayers result is %s\n\n' % result[0][0]
    return result[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    #Note: structure below lets execute() do both string substition and prevention of SQL injection
    query = "INSERT INTO Players (name) Values (%s);"
    c.execute(query, (name,))
    conn.commit() 
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    query = "SELECT * FROM Standings;"
    c.execute(query)
    result = c.fetchall()
    conn.commit() 
    #print 'playerStandings res is %s\n\n' % result
    conn.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    query = "INSERT INTO Matches (winner,loser) Values ('%s','%s');" % (winner, loser)
    c.execute(query)
    conn.commit() 
    conn.close()
    return
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    #query to get tuple:
    query = "SELECT ID, NAME FROM Standings ORDER BY wins;"
    c.execute(query)
    tourneyPlayers = c.fetchall()
    # print 'swissPairings query is %s' % tourneyPlayers
    # print len(tourneyPlayers)
    # print (tourneyPlayers[1] + tourneyPlayers[2])
    # print type(tourneyPlayers)
    # print type(Pairings(tourneyPlayers))
    return Pairings(tourneyPlayers)

def Pairings(playersAndScores):
#players and scores go in, players in pairs come out
    pairs = []
    for i in range(0, len(playersAndScores),2):
        pairs.append((playersAndScores[i] + playersAndScores[i+1]))
   #alternative method
    # p1 = playersAndScores[i]
    # p2 = playersAndScores[i+1]
    # p1_id = p1[0]
    # p1_name = p1[1]
    # p2_id = p2[0]
    # p2_name = p2[1]
    # pairs.append((p1_id, p1_name, p2_id, p2_name))
    #print pairs
    return pairs


# advanced fancy-pants Christian's way
# def PairWise(seq):
#     seq = iter(seq)
#     while seq:
#         pair = next(seq)+next(seq)
#         print pair
#         yield pair

