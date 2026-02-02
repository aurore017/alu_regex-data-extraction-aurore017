import re
import json

RAW_TEXT = """
Contact: support@company.co.uk, admin@test.com
Website: https://www.example.com
Phone: (123) 456-7890, 123-456-7890
Card used: 1234 5678 9012 3456
Meeting times: 14:30, 2:30 PM
Trending: #Python #Regex101

<script>alert('hack')</script>
javascript:alert(1)
"""

PATTERNS = {
    "emails": re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"),
    "urls": re.compile(r"\bhttps?:\/\/[^\s<>\"']+\b"),
    "phones": re.compile(r"\b(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b"),
    "credit_cards": re.compile(r"\b(?:\d{4}[- ]?){3}\d{4}\b"),
    "times": re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AP]M)?\b", re.IGNORECASE),
    "hashtags": re.compile(r"#[a-zA-Z0-9_]+\b")
}

def mask_email(email):
    user, domain = email.split("@")
    return user[0] + "***@" + domain

def mask_card(card):
    return "**** **** **** " + card[-4:]

def extract(text):
    result = {}
    for key, pattern in PATTERNS.items():
        matches = pattern.findall(text)
        if key == "emails":
            result[key] = [mask_email(e) for e in matches]
        elif key == "credit_cards":
            result[key] = [mask_card(c) for c in matches]
        else:
            result[key] = matches
    return result

if __name__ == "__main__":
    print(json.dumps(extract(RAW_TEXT), indent=4))

