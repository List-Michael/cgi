#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print("")

form = cgi.FieldStorage()
operands_val = form.getlist('operand')

try:
    user_sum = (sum([int(operand) for operand in operands_val]))
    print(user_sum)
except ValueError:
    print('Invalid operands')

