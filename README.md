# Spend.io

Spend.io is a simple spending tracker app. There is no authetication implemented, but a default user is constructed when the SQL to 
create the database tables is run.

## Requirements
Spend.io requires a modern web browser to run in. Python 3, flask, psycopg2 and PostgreSQL are also essential.

## Setup and running
After cloning the repository, create a database called "spendio" in PostgreSQL. This can be done with the command `createdb spendio`.
Once done run the SQL file included to create the tables required. From the directory that this readme file is in, this can be 
achieved by runnning the command `psql -d spendio -f app/db/spendio.sql`. If you would like some seed data in order to demonstrate the 
app's functionality, you can run seed.py using `python3 seed.py`

Once set up, `flask run` will start the app. The app can be accessed in your browser at the port specified by your flask instance.

## Use
### Tags and merchants
Within the app, you can use the navigation buttons along the top add or edit transactions, merchants and tags. Once a merchant is created, 
transactions can be recorded with the merchant as a beneficiary. Each transaction can be tagged with a category to allow the user to 
group together related spending (e.g. transport or groceries). Merchants can be assigned a default tag which will be applied to every 
transaction involving that merchant, although individual transactions can still be tagged differently if required.

Tags can be further grouped by colour-coding as the user is able to assign a colour to each tag for easy identification. Several tags can 
bs assigned the same colour.

On the tag management and merchant management pages, tags and merchants can be deactivated and reactivated. If a tag or merchant is not active, 
it will not appear as an option to be applied to a transaction, but will be retained on any existing transactions that have them.

### Transactions and filters
On the main transaction page, all transactions are listed, sorted by date. The panel on the right shows the users' budget, the remaining 
budget after all of the transactions and the total of all the selected transactions (before filtering, this includes all transactions). 
The panel on the left allows filtering of the visible transactions. 

To edit or delete and individual transaction, click on it in the main list of transactions.  

To filter the visible transactions, choose the merchant or tag that you would like to see from the drop-downs on the panel on the left.
Multiple tags and merchants can be filtered for simultaneously. The "Total Selected" figure on the right-hand panel shows a total of all transactions
filtered for.

To remove a filter, click on the 'X' symbol next to the tag or merchant's name on the left-hand panel. 
Clicking the "Clear Filter" button will remove all filters and display all transactions.

## Deleting Transactions
A single transaction can be deleted by clicking on it int the main transaction list, then clicking the delete button on the subsequent page.
To delete all transactions, click on the "Reset Transactions" button at the top of the page. Deleting transactions is NON-REVERSIBLE.
