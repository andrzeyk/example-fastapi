"""add content column to post table

Revision ID: 5d6614157f93
Revises: 0a732b62a58e
Create Date: 2021-11-09 17:43:32.619555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d6614157f93'
down_revision = '0a732b62a58e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
        sa.Column('content', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_column('posts', 'content')
    
