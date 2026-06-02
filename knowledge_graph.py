graph = {
    "camera": {
        "requires": ["permission disclosure", "user consent"],
        "governed_by": ["gdpr", "app store policy"]
    },

    "location": {
        "requires": ["privacy explanation", "user consent"],
        "governed_by": ["gdpr"]
    },

    "analytics": {
        "requires": ["tracking disclosure"],
        "governed_by": ["privacy policy"]
    }
}


def query_graph(entity):

    entity = entity.lower()

    if entity in graph:
        return graph[entity]

    return {}

# 🚀 WHAT THIS DOES

# Example:

# query_graph("camera")

# returns:

# {
#    "requires": ["permission disclosure"],
#    "governed_by": ["gdpr"]
# }