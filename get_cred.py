import os, json


with open(os.path.abspath("env.json")) as f:
    secrets = json.loads(f.read())


def get_secret_setting(setting, secrets=secrets):
    try:
        return secrets[setting]
    except ValueError:
        print("Oops!  That was no valid credential.  Try again...")

