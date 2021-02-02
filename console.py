import pdb
from datetime import date
from app.models.colour import Colour
from app.models.tag import Tag
from app.models.merchant import Merchant
from app.models.transaction import Transaction
from app.models.view_filter import ViewFilter
from app.models.user import User


import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository

user_repository.delete_all()
transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()
colour_repository.delete_all()


user1 = User("Scott", 1000.00)
user_repository.save(user1)

colour1 = Colour("black")
colour3 = Colour("red")
colour4 = Colour("green")
colour5 = Colour("blue")
colour6 = Colour("yellow")
colour7 = Colour("purple")
colour8 = Colour("pink")
colour9 = Colour("deepblue")

colour_repository.save(colour1)
colour_repository.save(colour3)
colour_repository.save(colour4)
colour_repository.save(colour5)
colour_repository.save(colour6)
colour_repository.save(colour7)
colour_repository.save(colour8)
colour_repository.save(colour9)

tag1 = Tag("Untagged", colour_repository.select_by_name("white"), True, True)
tag2 = Tag("Groceries", colour_repository.select_by_name("yellow"), True, False)

tag_repository.save(tag1)
tag_repository.save(tag2)

tag2.change_colour(colour_repository.select_by_name("green"))
tag_repository.update(tag2)

merchant1 = Merchant("Tesco", tag_repository.select_by_name("Untagged"))
merchant_repository.save(merchant1)

merchant1.change_default(tag2)
merchant_repository.update(merchant1)

transaction1 = Transaction(merchant1, 30.00, "2121-01-15")
transaction2 = Transaction(merchant1, 3.00, "2121-01-01")
transaction3 = Transaction(merchant1, 3.00, "2121-01-29")
transaction4 = Transaction(merchant1, 3.00, "2121-01-15")
transaction5 = Transaction(merchant1, 3.00, "2121-01-15")
transaction6 = Transaction(merchant1, 3.00, "2121-01-15")
transaction7 = Transaction(merchant1, 10.00, "2121-01-15")
transaction8 = Transaction(merchant1, 3.00, "2121-01-15")
transaction9 = Transaction(merchant1, 3.00, "2121-01-15")
transaction10 = Transaction(merchant1, 3.00, "2121-01-15")
transaction11 = Transaction(merchant1, 3.00, "2121-01-15")
transaction12 = Transaction(merchant1, 3.00, "2121-01-15")
transaction13 = Transaction(merchant1, 3.00, "2121-01-15")
transaction14 = Transaction(merchant1, 3.00, "2121-01-15")
transaction15 = Transaction(merchant1, 3.00, "2121-01-15")
transaction16 = Transaction(merchant1, 3.00, "2121-01-15")
transaction17 = Transaction(merchant1, 3.00, "2121-01-15")
transaction18 = Transaction(merchant1, 3.00, "2121-01-15")
transaction19 = Transaction(merchant1, 3.00, "2121-01-15")
transaction20 = Transaction(merchant1, 3.00, "2121-01-15")
transaction_repository.save(transaction1)
transaction_repository.save(transaction2)
transaction_repository.save(transaction3)
transaction_repository.save(transaction4)
transaction_repository.save(transaction5)
transaction_repository.save(transaction6)
transaction_repository.save(transaction7)
transaction_repository.save(transaction8)
transaction_repository.save(transaction9)
transaction_repository.save(transaction11)
transaction_repository.save(transaction12)
transaction_repository.save(transaction13)
transaction_repository.save(transaction14)
transaction_repository.save(transaction15)
transaction_repository.save(transaction16)
transaction_repository.save(transaction17)
transaction_repository.save(transaction18)
transaction_repository.save(transaction19)
transaction_repository.save(transaction20)
transaction_repository.save(transaction10)

user1.register_spending(transaction1)


pdb.set_trace()