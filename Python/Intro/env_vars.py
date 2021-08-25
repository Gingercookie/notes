import os

# get STAGE env var if exists, otherwise default to 'dev'
stage = os.getenv('STAGE', 'dev').upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)
