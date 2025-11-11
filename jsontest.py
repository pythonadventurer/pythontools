import json

backups = {
    "documents":{"src":r"C:\Users\robtf04\Documents",
                 "dest":r"F:\Thor\robuser\Documents"},
    "satisfactory":{"src":r"C:\Users\robtf04\AppData\Local\FactoryGame\Saved\SaveGames",
                 "dest":r"F:\Thor\robuser\Satisfactory"},
    "robdata":{"src":r"D:\robdata",
                 "dest":r"F:\Thor\robdata"},
    "archive":{"src":r"D:\robarchive\archive_current",
               "dest":r"F:\Thor\robarchive"}                 
}


with open("backups.json","w",encoding="utf-8") as write_file:
    json.dump(backups, write_file, indent=2)





