"""empty message

Revision ID: e29e2cc87d38
Revises: 3e125baccac3
Create Date: 2017-04-14 17:45:21.480000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e29e2cc87d38'
down_revision = '3e125baccac3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signin_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['front_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'front_user', sa.Column('signin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'front_user', 'signin')
    op.drop_table('signin_table')
    # ### end Alembic commands ###