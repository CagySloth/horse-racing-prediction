import os
import platform

import pandas as pd

# Platform-specific imports
if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl


def append_row_to_csv(file_path, row):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    new_row_df = pd.DataFrame([row])
    df = pd.concat([df, new_row_df], ignore_index=True)

    with open(file_path, mode="w", newline="") as file:
        if platform.system() == "Windows":
            msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, os.path.getsize(file_path))
            df.to_csv(file, index=False)
            file.flush()
            msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, os.path.getsize(file_path))
        else:
            # for unix systems
            fcntl.flock(file, fcntl.LOCK_EX)
            df.to_csv(file, index=False)
            file.flush()
            fcntl.flock(file, fcntl.LOCK_UN)


def flatten_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.unstack().reset_index(drop=True).to_frame().T
