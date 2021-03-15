class MaxNumberOfWithdrawals(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args
        else:
            self.msg = None
