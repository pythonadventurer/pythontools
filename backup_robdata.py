import json
import argparse
from backups import ffs_backup
from  pathlib import Path

# parser = argparse.ArgumentParser()
# parser.add_argument("bkp_name")
# args = parser.parse_args()
# bkp_name = args.bkp_name


with open("backups.json","r",encoding="utf-8") as read_file:
    backups = json.load(read_file)

ffs_file = Path(r"C:\\Users\\robtf04\\Documents\documents.ffs_batch")

ffs_backup(ffs_file,backups["documents"]["src"],backups["documents"]["dest"])


