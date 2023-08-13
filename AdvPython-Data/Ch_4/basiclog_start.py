# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(
    level=logging.DEBUG, filename="output.log"
)  # All levels will be printed
# TODO: Try out each of the log levels
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# TODO: Output formatted strings to the log
logging.debug("This is a formated string with x={} and y={}".format("ssg", 10))
