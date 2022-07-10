import hashlib


class MNY_coin_block():
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = ":*:".join(transaction_list) + ":*:" + previous_block_hash
        self.block_hash = hashlib.sha512(self.block_data.encode()).hexdigest()


## transactions comes here
# name_from + " sent to " + name_to + " " + amount + " MNY coins"
#

t_000 = "MNY sent to @dabzse 13 MNY coins"
t_001 = "@dabzse sent to root 7 MNY coins"
t_002 = "@dabzse sent to admin 4 MNY coins"
t_003 = "MNY sent to @dabzse 16 MNY coins"
t_004 = "root sent to admin 3.16 MNY coins"

## start! -> hashing()

start_transaction = MNY_coin_block("Everything started here", [t_000])
print(start_transaction.block_data)
print(start_transaction.block_hash)

first_transaction = MNY_coin_block(start_transaction.block_hash, [t_001])
print(first_transaction.block_data)
print(first_transaction.block_hash)

second_transaction = MNY_coin_block(first_transaction.block_hash, [t_002])
print(second_transaction.block_data)
print(second_transaction.block_hash)

third_transaction = MNY_coin_block(second_transaction.block_hash, [t_003])
print(third_transaction.block_data)
print(third_transaction.block_hash)

fourht_transaction = MNY_coin_block(third_transaction.block_hash, [t_004])
print(fourht_transaction.block_data)
print(fourht_transaction.block_hash)

"""

of course: you have to check is there enough amount to send
you can do multiple transactions inside the MNY_coin_block( <name>_transaction.block_hash, [<one>, <two>, <three>, <four>])
you can change any concatenation string, that is, .join(), inside of the block_data
you can use other hashing algorythm; hashlib.<ALGORYTHM>(self.block_data.encode()).hexdigest()
and these are only the basic steps....

"""
