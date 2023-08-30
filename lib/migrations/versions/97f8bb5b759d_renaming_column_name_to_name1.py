"""Renaming column name to name1

Revision ID: 97f8bb5b759d
Revises: 16b466a34fa7
Create Date: 2023-08-30 13:18:21.552452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f8bb5b759d'
down_revision = '16b466a34fa7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students','name' ,new_column_name='name1')


def downgrade() -> None:
    op.alter_column('students','name1',new_column_name='name')
