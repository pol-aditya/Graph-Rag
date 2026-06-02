KEYWORDS = [
    "camera",
    "location",
    "tracking",
    "analytics",
    "privacy",
    "permission",
    "gdpr",
    "ccpa",
    "personal data",
    "microphone",
    "contacts",
]

CRITICAL_FILES = [
    "AndroidManifest.xml",
    "Info.plist",
    "privacy",
]


def keyword_score(text):

    text = text.lower()

    score = 0

    for keyword in KEYWORDS:
        score += text.count(keyword)

    return score


def critical_file_score(file_name):

    file_name = file_name.lower()

    for critical in CRITICAL_FILES:
        if critical.lower() in file_name:
            return 20

    return 0


def calculate_chunk_score(chunk, file_name):

    score = 0

    score += keyword_score(chunk) * 5

    score += critical_file_score(file_name)

    return score
#🚀 RESULT

# Privacy-sensitive chunks automatically rank higher.