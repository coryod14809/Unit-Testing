import unittest


class User:
    def __init__(self, username, email, ss, hash):
        self.username = username
        self.email = Email(email)
        self.ss = Social(ss)
        self.hash = Hash(hash)

    def check_password(passwrd):
        return self.hash == Hash(passwrd)

    def __str__(self):
        return 'Username: ' + self.username + '\n', 'Email address: ' + str(self.email) \
                + '\n', 'Social Security Number: ' + str(self.ss) + '\n'
