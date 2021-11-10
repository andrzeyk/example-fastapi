"""add last few columns to posts table

Revision ID: 4577a12874a1
Revises: 1911160d298b
Create Date: 2021-11-10 11:15:01.345029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4577a12874a1'
down_revision = '1911160d298b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False,
        server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
        nullable=False, server_default=sa.text("now()")))


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
