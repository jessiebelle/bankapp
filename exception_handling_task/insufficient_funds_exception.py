# from account import Account
# from current_account import CurrentAccount

class InsufficientFunds(Exception):
    def __init__(self, msg="You have insufficient funds."):
        self.msg = msg
        super().__init__(msg)

# class spend_limit_error(Error):
#
#
# def __init__ (self, message="Exception occured because the account does not have sufficient funds."):
#
#     self.message = message
#     super().__init__(self.message)

# while True:
#     try:
#         balance < amount:
#         raise InsufficientFunds
#     except:
#         print("Your have withdrawn: ", balance)

