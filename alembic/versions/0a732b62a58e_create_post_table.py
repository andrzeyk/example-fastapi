"""create post table

Revision ID: 0a732b62a58e
Revises: 
Create Date: 2021-11-09 17:28:49.629049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a732b62a58e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('posts')
