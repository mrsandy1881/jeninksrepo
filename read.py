
import os

print("Jenkins Credentials")

username = os.getenv("JENKINS_USERNAME")
password = os.getenv("JENKINS_PASSWORD")

print("Username:", username if username else "Not Set")
print("Password:", "*" * len(password) if password else "Not Set")
