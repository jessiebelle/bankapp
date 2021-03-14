# from account import Account
# from current_account import CurrentAccount

class MaxNumberOfWithdrawals(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args
        else:
            self.msg = None
# class spend_limit_error(Error):
#
#
# def __init__ (self, message="Exception occured because the account does not have sufficient funds."):
#
#     self.message = message
#     super().__init__(self.message)

# while True:
#     if:
#         balance < amount:
#         raise InsufficientFunds
#     except:
#         print("Your have withdrawn: ", str(self.balance))

