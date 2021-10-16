'''Valid email address format
A valid email address consists of an email prefix and an email domain, both in acceptable formats.
The prefix appears to the left of the @ symbol.

The domain appears to the right of the @ symbol.

For example, in the address example@mail.com, "example" is the email prefix, and "mail.com" is the email domain.

Acceptable email prefix formats
Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
An underscore, period, or dash must be followed by one or more letter or number.
Invalid email prefixes:	Valid email prefixes:
abc-@mail.com	abc-d@mail.com
abc..def@mail.com	abc.def@mail.com
.abc@mail.com	abc@mail.com
abc#def@mail.com	abc_def@mail.com
Acceptable email domain formats
Allowed characters: letters, numbers, dashes.
The last portion of the domain must be at least two characters, for example: .com, .org, .cc
Invalid email domains:	Valid email domains:
abc.def@mail.c	abc.def@mail.cc
abc.def@mail#archive.com	abc.def@mail-archive.com
abc.def@mail	abc.def@mail.org
abc.def@mail..com	abc.def@mail.com, shubhamsingh@gmail.com
'''
def valid_email(mail):
    def domain_length(mail):
        domain_length = 0
        for char in reversed(mail):
            if char != '.':
                domain_length += 1
            else:
                break
    if '@' in mail or '.' in mail or '_' in mail:
        if domain_length(mail) > 2:
            return True
    return False
t1 = "siraj049@"

print(valid_email(t1))
