
from app.db.run_sql import run_sql
from app.models.colour import Colour

def save(colour):
    sql = "INSERT INTO colours(name) VALUES (%s, %s) RETURNING id"
    values = [colour.name]
    results = run_sql(sql, values)
    colour.id = results[0]['id']
    return colour

def select_all():
    colours = []
    
    sql = "SELECT * FROM colours"
    results = run_sql(sql)

    for row in results:
        colour = Colour(row['name'], row['id'])
        colours.append(colour)
    
    return colours

def select(id):
    colour = None

    sql = "SELECT * FROM colours WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        colour = Colour(result['name'], result['id'])
    return colour

def delete_all():
    sql = "DELETE FROM colours"
    run_sql(sql)