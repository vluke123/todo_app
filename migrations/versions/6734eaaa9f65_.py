"""empty message

Revision ID: 6734eaaa9f65
Revises: 
Create Date: 2022-11-30 18:36:45.603529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6734eaaa9f65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('list_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'todolists', ['list_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('list_id')

    # ### end Alembic commands ###
