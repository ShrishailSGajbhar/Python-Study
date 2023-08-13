# Demonstrate how to customize logging output

import logging

extData = {'user': 'shrishailgajbhar@example.com'}

# TODO: add another function to log from
def another_function():
    logging.debug("This is a log message from another fun", extra=extData)


# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtStr = f"%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(filename="output.log", level=logging.DEBUG,
                    format=fmtStr, datefmt=dateStr)

logging.info("This is an info-level log message", extra=extData)
logging.warning("This is a warning-level message", extra=extData)
another_function()
