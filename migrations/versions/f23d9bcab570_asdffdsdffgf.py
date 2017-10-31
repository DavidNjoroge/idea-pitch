"""asdffdsdffgf

Revision ID: f23d9bcab570
Revises: 8950aa14b709
Create Date: 2017-10-31 12:41:11.679073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f23d9bcab570'
down_revision = '8950aa14b709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###