from pathlib import Path
import datetime
import glob
import re

new_member_match = r"_[0-9]{10}.pdf"

print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Starting glob...")

# results = glob.glob(r'S:\Clinician Center/**/*Reports/*.pdf',recursive=True)
# results = glob.glob(r'S:\Clinician Center/**/*Member Documents/*.pdf',recursive=True)
# results = [f for f in glob.glob(r'S:\Clinician Center/**/*Member Documents/*.pdf',recursive=True) if re.search(new_member_match,f)]
results = [f for f in glob.glob(r'\\server/Rob/**/*.pdf',recursive=True) if re.search(new_member_match,f)]
print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Glob done.")

with open("results.txt","w",encoding="utf-8") as f:
    for result in results:
        f.write(f"{result}\n")


# results = [f for f in glob.glob(r'S:\Clinician Center/**/*Member Documents/*.pdf',recursive=True) if re.search(new_member_match,f)]
# for f in results:
#     print(f)