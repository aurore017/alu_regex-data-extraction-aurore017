#!/usr/bin/env python3
"""
Regex-Based Data Extraction
Junior Frontend Developer Assignment

Security Notes:
- Only http/https URLs are allowed
- Script tags and javascript: URLs are ignored
- Sensitive data (emails, credit cards) is masked
"""

import re
import json

# -------------------------------
# Sample raw input (API response)
# -------------------------------
RAW_TEXT = """
Hello Team,

Contact: support@company.co.uk, admin123@test.com
Website: https://www.example.com/page
Backup site: https://sub.example.org

Phone numbers:
(123) 456-7890
123-456-7890
123.456.7890

Payment processed using card 1234 5678 9012 3456
Alternative card: 1234-5678-9012-9999

Meeting times:
14:30
2:30 PM

Trending topics:
#Python #Regex101 #FrontendDev

Suspicious attempts:
<script>alert('hack')</script>
javascript:alert(1)
"""

# -------------------------------
# Regex patterns
# -------------------------------
PATTERNS = {
    "emails": re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"),
    "urls": re.compile(r"\bhttps?:\/\/[^\s<>\"']+\b"),
    "phones": re.compile(r"\b(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b"),
    "credit_cards": re.compile(r"\b(?:\d{4}[- ]?){3}\d{4}\b"),
    "times": re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AP]M)?\b", re.IGNORECASE),
    "hashtags": re.compile(r"#[a-zA-Z0-9_]+\b")
}

# -------------------------------
# Masking functions (security)
# -------------------------------
def mask_email(email):
    username, domain = email.split("@")
    return username[0] + "***@" + domain

def mask_credit_card(card):
    return "**** **** **** " + card[-4:]

# -------------------------------
# Extraction logic
# -------------------------------
def extract_data(text):
    extracted = {}

    for key, pattern in PATTERNS.items():
        matches = pattern.findall(text)

        if key == "emails":
            extracted[key] = [mask_email(e) for e in matches]
        elif key == "credit_cards":
            extracted[key] = [mask_credit_card(c) for c in matches]
        else:
            extracted[key] = matches

    return extracted

# -------------------------------
# Main execution
# -------------------------------
if __name__ == "__main__":
    result = extract_data(RAW_TEXT)

    print("Extracted Data:")
    print(json.dumps(result, indent=4))

