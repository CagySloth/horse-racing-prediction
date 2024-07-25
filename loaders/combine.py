import csv
import os
import fcntl

# Function to append a row to a CSV file safely
def append_row_to_csv(file_path, row):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, mode='a', newline='') as file:
        # Acquire an exclusive lock on the file
        fcntl.flock(file, fcntl.LOCK_EX)
        
        writer = csv.writer(file)
        writer.writerow(row)
        
        # Flush the internal buffer
        file.flush()
        # Release the lock
        fcntl.flock(file, fcntl.LOCK_UN)
