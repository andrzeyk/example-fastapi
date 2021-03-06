"""autogenerate phone column in users table

Revision ID: 7fe2eb0f5afb
Revises: 395579b2ee37
Create Date: 2021-11-10 11:32:43.427312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fe2eb0f5afb'
down_revision = '395579b2ee37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
