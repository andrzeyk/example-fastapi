"""add foreign-key to post table

Revision ID: 1911160d298b
Revises: 162808ea992e
Create Date: 2021-11-10 11:01:11.139351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1911160d298b'
down_revision = '162808ea992e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",
    local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
