# setup a global logger for the project
import os
from logging import StreamHandler, FileHandler, Formatter, Logger
from logging.handlers import RotatingFileHandler
from datetime import date


# Create the logger class
class _Logger(Logger):
    def __init__(self, name=None):
        super().__init__(name)
    
    def start(
        self, 
        log_level: str, 
        date_format: str, 
        msg_format: str, 
        enable_console_log: bool,
        enable_file_log: bool,
        log_file_path: str
    ) -> None:
        self.setLevel(log_level.upper())
        formatter = Formatter(msg_format, datefmt=date_format)

        if enable_file_log:
            # Create a file handler with rotation
            log_file = os.path.join(os.getcwd(), f"app_{date.today()}.log")
            file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
            file_handler.setLevel(log_level.upper())
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)
        
        if enable_console_log:
            # Create a console handler
            console_handler = StreamHandler()
            console_handler.setLevel(log_level.upper())
            console_handler.setFormatter(formatter)
            self.addHandler(console_handler)

    def stop (self) -> None:
        """Stop the logger."""
        for handler in self.handlers[:]:
            handler.close()
            self.removeHandler(handler)
        self.info("Logger stopped.")

logger = _Logger("logger")