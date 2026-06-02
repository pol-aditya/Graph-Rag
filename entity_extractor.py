KNOWN_ENTITIES = [
    "camera",
    "location",
    "analytics",
    "tracking",
    "privacy",
]


def extract_entities(text):

    text = text.lower()

    found = []

    for entity in KNOWN_ENTITIES:

        if entity in text:
            found.append(entity)

    return found

# 🚀 WHAT THIS DOES

# If retrieved text contains:

# camera
# location
# tracking

# it returns:

# ["camera", "location", "tracking"]