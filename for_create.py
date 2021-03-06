import psycopg2


def create_connection(db_name, db_user, db_password,
                      db_host, db_port=5432):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


conn = create_connection(
    'postgres', 'admin', 'admin', 'localhost'
)

create_users = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  login VARCHAR(30) NOT NULL UNIQUE, 
  password VARCHAR(32) NOT NULL
)
"""

create_links = """
CREATE TABLE IF NOT EXISTS links (
  id SERIAL PRIMARY KEY,
  url VARCHAR(300) NOT NULL,
  name_url VARCHAR(150) NOT NULL,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
)"""

conn.autocommit = True
cursor = conn.cursor()
cursor.execute(create_users)
cursor.execute(create_links)
print('ok')