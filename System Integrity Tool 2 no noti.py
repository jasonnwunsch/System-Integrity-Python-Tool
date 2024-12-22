#Jason M. Wunsch
#System Integrity Python Tool
#December 18, 2024





import hashlib
import os
import shutil
import time
import logging
from threading import Thread

# Log files
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

monitoring_log_file = os.path.join(downloads_folder, "MONITORING_LOG.txt")
cleared_temp_files_log_file = os.path.join(downloads_folder, "CLEARED_TEMP_FILES_LOG.txt")

os.makedirs(os.path.dirname(monitoring_log_file), exist_ok=True)
os.makedirs(os.path.dirname(cleared_temp_files_log_file), exist_ok=True)

# Files and folders to monitor
file_paths_to_monitor = [
    "G:/My Drive/Jason Files/School/CYB 333 Security Automation/TEST_SCRIPT.txt",
]

# Hash store
hash_file = "hashes.txt"

# Temporary file cleanup settings
temp_dirs_to_clean = [
    os.getenv("TEMP"), 
    "C:/Windows/Temp"
]

# Temp file logger
monitoring_logger = logging.getLogger('monitoring')
monitoring_logger.setLevel(logging.INFO)
monitoring_handler = logging.FileHandler(monitoring_log_file)
monitoring_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
monitoring_logger.addHandler(monitoring_handler)

cleared_temp_files_logger = logging.getLogger('cleared_temp_files')
cleared_temp_files_logger.setLevel(logging.INFO)
cleared_temp_files_handler = logging.FileHandler(cleared_temp_files_log_file)
cleared_temp_files_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
cleared_temp_files_logger.addHandler(cleared_temp_files_handler)

# File hash calculation
def calculate_file_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

# Monitor file continuously
def monitor_files():
    try:
        with open(hash_file, "r") as file:
            saved_hashes = {line.split()[0]: line.split()[1] for line in file.readlines()}
    except FileNotFoundError:
        saved_hashes = {}

    while True:
        for file_path in file_paths_to_monitor:
            if os.path.exists(file_path):
                current_hash = calculate_file_hash(file_path)
                if file_path in saved_hashes:
                    if saved_hashes[file_path] != current_hash:
                        log_change(f"File {file_path} CHANGE DETECTED!")
                        saved_hashes[file_path] = current_hash  
                else:
                    saved_hashes[file_path] = current_hash

        # Update hash file
        with open(hash_file, "w") as file:
            for file_path, file_hash in saved_hashes.items():
                file.write(f"{file_path} {file_hash}\n")

        time.sleep(1)

# Clean up temporary files at specified intervals
def cleanup_temp_files(interval_seconds):
    while True:
        deleted_files = []
        for temp_dir in temp_dirs_to_clean:
            if os.path.exists(temp_dir):
                for file_name in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, file_name)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            deleted_files.append(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                            deleted_files.append(file_path)
                    except Exception as e:
                        cleared_temp_files_logger.error(f"Error deleting {file_path}: {e}")

        if deleted_files:
            log_deleted_files(deleted_files)
        else:
            cleared_temp_files_logger.info("No temporary files to clear.")

        time.sleep(interval_seconds)

# Log file changes
def log_change(message):
    monitoring_logger.info(message)

# Log deleted files
def log_deleted_files(deleted_files):
    for file_path in deleted_files:
        cleared_temp_files_logger.info(f"Deleted {file_path}")

# Execution
def main():
    print("System Integrity Tool")

    # Prompt for intervals
    try:
        temp_cleanup_interval = int(input("Enter interval in minutes to clear temporary files: ")) * 60
    except ValueError:
        print("Invalid input, please enter a valid number.")
        return

    print("\nMonitoring started")
    print(f"Monitoring log location: {monitoring_log_file}")
    print(f"Temporary file cleanup log location: {cleared_temp_files_log_file}")

    # Start threads for file monitoring and temp file cleanup
    Thread(target=monitor_files, daemon=True).start()
    Thread(target=cleanup_temp_files, args=(temp_cleanup_interval,), daemon=True).start()

    # Loop to keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == "__main__":
    main()
