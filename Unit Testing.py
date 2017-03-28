import unittest
import random


class User:
    def __init__(self, username, email, ss, hash):
        self.username = username
        self.email = Email(email)
        self.ss = SS(ss)
        self.hash = Hash(hash)

    def check_password(self, passwrd):
        return self.hash == Hash(passwrd)

    def __str__(self):
        return 'Username: ' + self.username + '\n', 'Email address: ' + str(self.email) \
                + '\n', 'Social Security Number: ' + str(self.ss) + '\n'


class InvalidEmail(Exception):
    pass


class InvalidSocial(Exception):
    pass


class InvalidPassword(Exception):
    pass


class Email:

    def __init__(self, email):
        if "@" in email:
            self.email = email
        else:
            raise InvalidEmail

    def __str__(self):
        return self.email


class SS:

    def __init__(self, social):
        if "-" in social:
            self.social = social
        else:
            raise InvalidSocial


class Hash:
    x = 0

    def __init__(self, passwd):
        if len(passwd) > 1:
            self.hash = self.generate_hash(passwd)
        else:
            raise InvalidPassword

    def __eq__(self, passwd):
        return self.hash == self.generate_hash(passwd)

    @staticmethod
    def generate_hash(passwd):
        Hash.x += 1
        return Hash.x

class FixturesTest(unittest.TestCase):

    def test(self):
        print('In test()')
        self.obj1 = Email('fred@gmail.com')
        #self.obj2 = Email('fredgmail.com')
        self.obj3 = SS('234-23-1234')
        #self.obj4 = SS('234231234')
        self.obj4 = Hash('asdf')
        #self.obj5 = Hash('')

if __name__ == '__main__':
    unittest.main()




