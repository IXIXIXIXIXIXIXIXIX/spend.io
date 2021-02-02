from app.db.run_sql import run_sql
from app.models.merchant import Merchant
import app.repositories.tag_repository as tag_repository

def save (merchant):
    sql = "INSERT INTO merchants(name, default_tag_id, active) VALUES (%s, %s, %s) RETURNING id"
    values = [merchant.name, merchant.default_tag.id, merchant.active]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']

    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row['default_tag_id'])
        merchant = Merchant(row['name'], tag, row['active'], row['id'])
        merchants.append(merchant)

    return merchants 


def select_active():
    merchants = []

    sql = "SELECT * FROM merchants WHERE active = true"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row['default_tag_id'])
        merchant = Merchant(row['name'], tag, row['active'], row['id'])
        merchants.append(merchant)

    return merchants 
def select(id):
    merchant = None

    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result['default_tag_id'])
        merchant = Merchant(result['name'], tag, result['active'], result['id'])
    
    return merchant

def select_by_name(name):
    merchant = None

    sql = "SELECT * FROM merchants WHERE name = %s"
    values = [name.upper()]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result['default_tag_id'])
        merchant = Merchant(result['name'], tag, result['active'], result['id'])
    
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def update(merchant):
    sql = "UPDATE merchants SET (name, default_tag_id, active) = (%s, %s, %s) WHERE id = %s"
    values = [merchant.name, merchant.default_tag.id, merchant.active, merchant.id]

    run_sql(sql, values)