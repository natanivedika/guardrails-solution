import psycopg2
from psycopg2.extras import RealDictCursor
# from functools import lru_cache
from config.settings import Settings

class Postgres:
    """
    Establishes a connection on initialization using the DSN defined in
    Settings, and provides helper methods for executing queries and
    returning results as dictionaries.
    """

    def __init__(self):
        self.conn = psycopg2.connect(Settings.DB_DSN)

    def fetch_all(self, query: str, params: dict):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()

def get_policies(subdomain_id, country):
    """
    Fetches all policies for a given subdomain and country.
    """

    db = Postgres()
    return db.fetch_all("""
        SELECT * FROM aigenie_policies.policies
        WHERE subdomain_id = %(subdomain)s AND country = %(country)s
    """, {"subdomain": subdomain_id, "country": country})

def get_constraints(subdomain_id, country):
    """
    Fetches all constraints for a given subdomain and country.
    """
    
    db = Postgres()
    return db.fetch_all("""
        SELECT * FROM aigenie_policies.constraints
        WHERE subdomain_id = %(subdomain)s AND country = %(country)s
    """, {"subdomain": subdomain_id, "country": country})
