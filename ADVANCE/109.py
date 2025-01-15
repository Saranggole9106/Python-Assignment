import re

text = "Please contact us at support@example.com or sales@example.org."

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Found email addresses:", emails)
