from pathlib import Path
import glob

test_file = "Add Final Check Before Billing"
vault_root = r"\\server/Rob/PCS_DevWiki/"

# get the full path of a note using just the file name 
md_files = glob.glob(str(vault_root) + "**/*.md",recursive=True)

for file in md_files:
    if test_file in file:
        print(Path(file))


