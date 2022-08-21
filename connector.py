import urllib.request, json, psycopg2

from config import config

with urllib.request.urlopen("https://random-data-api.com/api/v2/beers?size=10") as url:
    data = json.loads(url.read().decode())

try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    for item in data:
        ibu = item['ibu']
        ibu = int(ibu[:len(ibu)-4])

        alcohol = item['alcohol']
        alcohol = float(alcohol.rstrip(alcohol[-1]))

        blg = item['blg']
        blg = float(blg[:len(blg)-4])

        cur.execute('INSERT INTO beers (id, uid, brand, name, style, hop, yeast, malts, ibu, alcohol, blg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (item['id'], item['uid'], item['brand'], item['name'], item['style'], item['hop'], item['yeast'], item['malts'], ibu, alcohol, blg))

    cur.close()
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
