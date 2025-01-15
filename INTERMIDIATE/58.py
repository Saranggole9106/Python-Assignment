import logging

# Configure the logging system
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log some messages
logging.info("This is an informational message.")
logging.error("This is an error message.")
logging.warning("This is a warning message.")

print("Logs have been written to app.log.")
