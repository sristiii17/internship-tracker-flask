import re

PORTALS = {
    "linkedin",
    "internshala",
    "naukri",
    "indeed",
    "wellfound",
    "glassdoor",
    "unstop"
}


def extract_company(sender, subject, body=""):
    """
    Try to identify the actual company.
    """

    match = re.search(r'@([A-Za-z0-9-]+)\.', sender)

    if match:
        company = match.group(1).lower()

        if company not in PORTALS:
            return company.title()

    # Try subject
    words = re.findall(r"[A-Z][A-Za-z0-9&-]+", subject)

    for word in words:

        if word.lower() not in PORTALS:

            if len(word) > 2:

                return word

    return "Unknown"