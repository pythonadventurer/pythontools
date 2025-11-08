import subprocess
import datetime
from pathlib import Path

backup_time = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
backup_src = Path(r"C:\Users\robtf04\Documents\Anno 1800")
backup_dest = Path(Path(r"F:\Thor\robuser\Anno 1800"),backup_time)
ffs_file = Path(r"C:\Users\robtf04\Documents\anno.ffs_batch")
Path.mkdir(backup_dest)

# C:\Users\robtf04\Documents\anno.ffs_batch -DirPair "C:\Users\robtf04\Documents\Anno 1800" $dest



command = f"FreeFileSync.exe {ffs_file} -DirPair '{backup_src}' '{backup_dest}'"

result = subprocess.run(["powershell","-Command",command],capture_output=True,text=True)
print(result.stdout)

