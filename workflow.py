import os

# GitHub boolean inputs come across as "true" or "false" strings
run_update = os.getenv("RUN_UPDATE") == "true"

if run_update:
    print("Running the update program...")
    # Your update logic here
else:
    print("Standard run triggered.")
