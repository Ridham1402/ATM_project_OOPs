import pytest
from ATM import User

class TestUser:
    
    #test case for checking initialisation of User
    def test_registration(self):
        mohit = User(7520912456263237, 1211, 452)
        print('testing details : new user registration')
        assert (7520912456263237, 1211) == (mohit.card_no, mohit.PIN)

    #test case for checking balance function
    def test_balance(self):
        mohit = User(7520912456263237, 1211, 45282)
        print('\ntesting : balance')
        assert (7520912456263237, 25367) == (mohit.card_no, mohit.balance)      #Test should fail as 25367 != 45282

#for next 2 tests, amount entered in CLI changes balance

    #testing withdrawl function
    def test_withdraw(self):
        mohit = User(7520912456263237, 1211, 45282)
        print('\ntesting : withdrawl')
        mohit.withdraw()             
        assert (45282) == (mohit.balance)       #test will fail as balance is no more the same showing that balance is updated

    #testing deposit function
    def test_deposit(self):
        mohit = User(7520912456263237, 1211, 45282)
        print('\ntesting deposit')
        mohit.deposit()             
        assert (45282) == (mohit.balance)           #test will fail as balance is no more the same showing that balance is updated