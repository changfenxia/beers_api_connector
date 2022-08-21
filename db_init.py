import psycopg2

from config import config

def create_table():
    commands = (
        """
        CREATE TABLE beers (
            id INTEGER PRIMARY KEY,
            uid     VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            style VARCHAR(255) NOT NULL,
            hop VARCHAR(255) NOT NULL,
            yeast VARCHAR(255) NOT NULL,
            malts VARCHAR(255) NOT NULL,
            ibu INTEGER NOT NULL,
            alcohol REAL NOT NULL,
            blg REAL NOT NULL
         )
        """,
        )

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    finally:
            if conn is not None:
                conn.close()

create_table()