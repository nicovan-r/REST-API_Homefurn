"""add consumable column

Revision ID: 2ac69bfbab8a
Revises: 7b7103ce161b
Create Date: 2024-06-08 07:20:20.206762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac69bfbab8a'
down_revision = '7b7103ce161b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_material_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('consumable', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_material_list', schema=None) as batch_op:
        batch_op.drop_column('consumable')

    # ### end Alembic commands ###
