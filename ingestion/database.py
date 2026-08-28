"""Database starter.

The API currently keeps live demo state in memory. This module provides a clean
place for students to add SQLAlchemy/TimescaleDB persistence in the next phase.
"""
import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://mountainguard:mountainguard@localhost:5432/mountainguard",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
