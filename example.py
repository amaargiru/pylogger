import pathlib

from pylogger import PyLogger

# Path to logs
log_file_path = "logs//example.log"
# Max file size
log_max_file_size = 1024 ** 2
# Max number of files
log_max_file_count = 10

if __name__ == '__main__':
    # Create a path to the log file if it doesn't exist
    path = pathlib.Path(log_file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = PyLogger.get_logger(log_file_path, log_max_file_size, log_max_file_count)

    logger.debug("Sample of DEBUG message")
    logger.info("Sample of INFO message")
    logger.warning("Sample of WARNING message")
    logger.error("Sample of ERROR message")
    logger.critical("Sample of CRITICAL message")
