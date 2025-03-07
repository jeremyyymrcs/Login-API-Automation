import os
from utilities.custom_logging import get_custom_logger

logger = get_custom_logger(__name__)


class FileOperations:
    @staticmethod
    def save_totp_code(totp, file_name="saved_totp_code.txt"):
        """Create the generated TOTP code from a file."""
        file_path = os.path.join("..", "data", file_name)
        try:
            with open(file_path, "w") as file:
                file.write(totp)
            logger.info(f"TOTP code saved successfully to {file_path}.")
        except Exception as e:
            logger.error(f"Failed to save TOTP code to file at {file_path}: {e}")
            raise

    @staticmethod
    def read_totp_code():
        """Reads the generated TOTP code from a file."""
        file_path = os.path.join("..", "data", "saved_totp_code.txt")
        try:
            with open(file_path, "r") as file:
                return file.read().strip()
        except Exception as e:
            logger.error(f"Failed to read TOTP code from file at {file_path}: {e}")
            raise
