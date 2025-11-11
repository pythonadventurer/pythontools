import subprocess
import datetime
from pathlib import Path

def ffs_backup(ffs_file, src, dest):
    """
    Run a backup using a FreeFileSync batch file.
    Backups are created in a timestamp folder within
    the backup destination.

    Parameters
    ----------
    ffs_file: string
              Path to the batch file.
         src: string
              Path of directory to be backed up.
        dest: string
              Path of directory to backup to.

    """
    # create a timestamp folder in the backup destination directory
    backup_time = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    backup_dest = Path(Path(dest),backup_time)
    Path.mkdir(backup_dest)

    command = f"FreeFileSync.exe {ffs_file} -DirPair '{src}' '{backup_dest}'"

    result = subprocess.run(["powershell","-Command",command],capture_output=True,text=True)
    print(result.stdout)


