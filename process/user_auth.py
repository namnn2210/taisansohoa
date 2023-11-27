# auth.py
from connect import get_neo4j_driver


def register(username, password, default_role='admin'):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run("CREATE (:TK {TenDN: $username, PW: $password})",
                    username=username, password=password)
        session.run(
            "MATCH (user:TK {TenDN: $username}), (role:QUYEN {TenQ: $default_role}) "
            "CREATE (user)-[:HAS_ROLE]->(role)",
            username=username, default_role=default_role
        )
        print(
            f"User {username} with default role '{default_role}' created successfully.")
    driver.close()


def login(username, password):
    driver = get_neo4j_driver()
    with driver.session() as session:
        result = session.run("MATCH (user:TK {TenDN: $username, PW: $password}) RETURN user",
                             username=username, password=password)
        user = result.single()
        is_authenticated = user is not None
    driver.close()
    return is_authenticated

# # Example usage
# # Register a new user
# register("new_user", "new_password123")

# # Attempt to login
# if login("new_user", "new_password123"):
#     print("Login successful")
# else:
#     print("Login failed")
