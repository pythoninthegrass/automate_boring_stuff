#!/usr/bin/env python3

import logging, os

"""
## 5 Log levels:
1) debug (lowest)
2) info
3) warning
4) error
5) critical (highest)
"""

# pwd
print(os.getcwd())

# logging config function
logging.basicConfig(
    filename='./debugging/error.log',                           # relative path of error log
    filemode='a',                                               # append mode vs. write
    level=logging.DEBUG,                                        # debug redirect to log vs. stdout
    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(
#     level=logging.DEBUG,                                      # debug to stdout
#     format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)                             # disables logging at highest level, critical

logging.debug('Start of program')

# factorial function
def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    # for i in range(n + 1):                                    # starts at 0 (0*1*2*3*4*5 == 0)
    for i in range(1, n + 1):                                   # starts at 1
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))                                             # 1*2*3*4*5 == 120

logging.debug('End of program')