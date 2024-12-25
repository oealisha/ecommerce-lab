"""Add initial data

Revision ID: 6af013b70a0c
Revises: 3ca44afb781a
Create Date: 2024-12-25 23:44:58.627411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6af013b70a0c'
down_revision: Union[str, None] = '3ca44afb781a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Insert initial data into the 'user' table
    op.execute("""
        INSERT INTO user (username, email_address, password_hash, budget)
        VALUES
        ('john_doe', 'john@example.com', 'hashed_pw', 1000),
        ('jane_doe', 'jane@example.com', 'hashed_pw', 1500);
    """)

    # Insert initial data into the 'item' table
    op.execute("""
        INSERT INTO item (name, price, barcode, description, owner)
        VALUES
        ('Samsung S25', 100000, '123456789012', 'Samsung Mobile Phone', 1),
        ('iPhone 14', 120000, '123456789013', 'Apple Mobile Phone', 2);
    """)


def downgrade():
    # Remove the initial data
    op.execute("DELETE FROM item WHERE name IN ('Samsung S25', 'iPhone 14');")
    op.execute("DELETE FROM user WHERE username IN ('john_doe', 'jane_doe');")
