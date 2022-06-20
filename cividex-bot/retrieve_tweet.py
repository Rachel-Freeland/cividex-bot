from os import environ as env
import psycopg2




def fetch_tweet(query):
    '''
    Fetches information from postgres database to create a tweet
    '''
    connect = psycopg2.connect(f"dbname={env['DATABASE_NAME']} user={env['POSTGRES_USER']} password={env['PASSWORD']} host={env['HOST']} port = '5432")

    cursor = connect.cursor()
        # TODO: Postgres query to find the information we're looking for.
    cursor.execute (f'SELECT * FROM {query}')
        # Retrieve results
    records = cursor.fetchall()

    print(records)
    return records