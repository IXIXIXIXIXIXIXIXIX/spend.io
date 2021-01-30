
from app.db.run_sql import run_sql
from app.models.view_filter import ViewFilter
from app.models.user import User

def save(user):
    sql = "INSERT INTO users(name, budget) VALUES (%s, %s) RETURNING id"
    values = [user.name, user.budget]
    results  = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['budget'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['budget'], result['id'])

    return user


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)