import psycopg2
from django.db import DatabaseError,transaction

def connect_psql(req_first_name,req_last_name,req_email):
	print("CONNECT PSQL")
	try:
		conn = psycopg2.connect(database='django_db',user='django_user',password='django_user_passwrd',host='localhost')
		cur = conn.cursor()

	except:
		print("I am unable to connect to the database.")

	try:
		cur.execute('INSERT INTO django_table (firstname,lastname,email) VALUES (%s, %s, %s) RETURNING id', (req_first_name,req_last_name,req_email))
		conn.commit()
		records = cur.fetchall()
		cur.close()
		conn.close()
		return(records[0][0])

	except DatabaseError:
		print("Write in database: ERROR")
		transaction.rollback()

def request_record_id(record_id):

	print("CONNECT PSQL")
	try:
		conn = psycopg2.connect(database='django_db',user='django_user',password='django_user_passwrd',host='localhost')
		cur = conn.cursor()

	except:
		print("I am unable to connect to the database.")


	try:
		cur.execute('SELECT * FROM django_table WHERE id=(%s)' % (record_id))

		records = cur.fetchall()
		if not records:
			keys_records_id = None
			return(keys_records_id)
		
		keys_record_id = records[0]
		cur.close()
		conn.close()
		return(keys_record_id)

	except DatabaseError:
		print("Reading from table:ERROR")
		transaction.rollback()


