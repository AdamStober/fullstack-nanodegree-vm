#
# Database access functions for the web forum.
# 

import time
import psycopg2

#adding bleach
import bleach

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
	'''Get all the posts from the database, sorted with the newest first.

	Returns:
		A list of dictionaries, where each dictionary has a 'content' key
		pointing to the post content, and 'time' key pointing to the time
		it was posted.
	'''
### Adam's code below
	DB = psycopg2.connect("dbname=forum")
	c = DB.cursor()
	c.execute("SELECT time, content from posts ORDER BY time DESC")
## code to be commented out
#    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
#    posts.sort(key=lambda row: row['time'], reverse=True)
### code to replace code above
	posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
	DB.close()
	return posts

## Add a post to the database.
def AddPost(content):
	'''Add a new post to the database.

	Args:
		content: The text content of the new post.
	'''
	## code to be commented out
	#   t = time.strftime('%c', time.localtime())
	#   DB.append((t, content))
	DB = psycopg2.connect("dbname=forum")
	c = DB.cursor()
	# fails to protect from SQL injection attack
	#c.execute("INSERT INTO posts (content) VALUES ('%s')" % content)
	# attempts to protect from SQL injection attack, protect from bleach
	cleaned_content = bleach.clean(content, strip=True)
	c.execute("INSERT INTO posts (content) VALUES (%s)", (cleaned_content,))
	DB.commit()
	DB.close()