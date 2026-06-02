from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"

USERNAME = "neo4j"

PASSWORD = "@ditya2104"


driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# 🚀 WHAT THIS DOES

# Python now connects to:

# Neo4j graph database



def get_graph_context(entity):

    query = """
    MATCH (n {name:$name})-[r]->(m)
    RETURN type(r) as relationship, m.name as target
    """

    with driver.session() as session:

        result = session.run(query, name=entity)

        output = []

        for record in result:

            output.append({
                "relationship": record["relationship"],
                "target": record["target"]
            })

        return output
    
    # 🚀 STEP 4 — ADD GRAPH QUERY FUNCTION
    
def get_graph_context(entity):

    query = """
    MATCH (n {name:$name})-[r]->(m)
    RETURN type(r) as relationship, m.name as target
    """

    with driver.session() as session:

        result = session.run(query, name=entity)

        output = []

        for record in result:

            output.append({
                "relationship": record["relationship"],
                "target": record["target"]
            })

        return output