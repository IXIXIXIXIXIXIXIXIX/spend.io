from app.db.run_sql import run_sql
from app.models.tag import Tag
import app.repositories.colour_repository as colour_repository

def save (tag):
    sql = "INSERT INTO tags(name, colour_id, active, reserved) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [tag.name, tag.colour.id, tag.active, tag.reserved]
    results = run_sql(sql, values)
    tag.id = results[0]['id']

    return tag

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        colour = colour_repository.select(row['colour_id'])
        tag = Tag(row['name'], colour, row['active'], row['reserved'], row['id'])
        tags.append(tag)

    return tags


def select(id):
    tag = None

    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        colour = colour_repository.select(result['colour_id'])
        tag = Tag(result['name'], colour, result['active'], result['reserved'], result['id'])
    
    return tag

def select_by_name(name):
    tag = None

    sql = "SELECT * FROM tags WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        colour = colour_repository.select(result['colour_id'])
        tag = Tag(result['name'], colour, result['active'], result['reserved'], result['id'])
    
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def update(tag):
    sql = "UPDATE tags SET (name, colour_id, active, reserved) = (%s, %s, %s, %s) WHERE id = %s"
    values = [tag.name, tag.colour.id, tag.active, tag.reserved, tag.id]

    run_sql(sql, values)