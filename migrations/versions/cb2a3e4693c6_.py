"""empty message

Revision ID: cb2a3e4693c6
Revises: f6c395aec58e
Create Date: 2019-03-16 06:32:03.644789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb2a3e4693c6'
down_revision = 'f6c395aec58e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('photo', sa.String(length=80), nullable=True))
    op.drop_column('user_profiles', 'photo_filepath')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('photo_filepath', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('user_profiles', 'photo')
    # ### end Alembic commands ###
