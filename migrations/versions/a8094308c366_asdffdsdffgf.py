"""asdffdsdffgf

Revision ID: a8094308c366
Revises: f23d9bcab570
Create Date: 2017-10-31 14:02:21.239978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8094308c366'
down_revision = 'f23d9bcab570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('user', sa.String(length=255), nullable=True))
    op.drop_constraint('pitches_user_id_fkey', 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitches_user_id_fkey', 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'user')
    # ### end Alembic commands ###
