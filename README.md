# Regex Data Extraction

This project demonstrates regex-based extraction and validation of structured data from unstructured text, simulating raw data returned from an external API.

The program focuses on accuracy, robustness, and basic security awareness when handling potentially unsafe input.

# Features

The program extracts the following data types from raw text:

- Email addresses
- URLs (HTTP/HTTPS only)
- Phone numbers
- Credit card numbers
- Time values (12-hour and 24-hour formats)
- Hashtags

Sensitive data such as emails and credit card numbers are masked before being displayed.

# Security Considerations

- Only well-formed patterns are extracted.
- Unsafe input such as `<script>` tags or `javascript:` URLs is ignored.
- Sensitive information is never printed in full.
- The program assumes all input may be untrusted.

# Project Structure


