from app.db.run_sql import run_sql
from app.models.transaction import Transaction
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository

def save (transaction):
    sql = "INSERT INTO transactions(merchant_id, tag_id, datestamp, amount) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.tag.id, transaction.date, transaction.amount]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']

    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(merchant, row['amount'], row['datestamp'], tag, row['id'])
        transactions.append(transaction)

    return transactions 


def select(id):
    transaction = None

    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result['tag_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(merchant, result['amount'], result['datestamp'], tag, result['id'])
    
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, tag_id, datestamp, amount) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.tag.id, transaction.date, transaction.amount, transaction.id]

    run_sql(sql, values)