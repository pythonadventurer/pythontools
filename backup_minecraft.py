import json
from backups import ffs_backup
from  pathlib import Path

with open("backups.json","r",encoding="utf-8") as read_file:
    backups = json.load(read_file)

ffs_file = "documents.ffs_batch"

ffs_backup(ffs_file,backups["minecraft"]["src"],backups["minecraft"]["dest"])


