from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_ncc(ncc_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:NCC {MANCC: $MANCC, TenNCC: $TenNCC, SDT: $SDT, EMAIL: $EMAIL, MST: $MST, DC: $DC}) RETURN n",
            **ncc_data.dict()
        )
        return result.single()[0]


def get_ncc(mancc):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NCC {MANCC: $MANCC}) RETURN n",
            MANCC=mancc
        )
        return result.single()[0]


def update_ncc(mancc, ncc_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NCC {MANCC: $MANCC}) "
            "SET n += {TenNCC: $TenNCC, SDT: $SDT, EMAIL: $EMAIL, MST: $MST, DC: $DC} "
            "RETURN n",
            MANCC=mancc, **ncc_data.dict()
        )
        return result.single()[0]


def delete_ncc(mancc):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NCC {MANCC: $MANCC}) DELETE n",
            MANCC=mancc
        )
        return result.consume().counters.nodes_deleted > 0
