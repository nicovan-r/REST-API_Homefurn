"""add currency column to product_list table

Revision ID: 8e75acf66313
Revises: 27e1193b66a0
Create Date: 2024-06-08 20:26:46.498070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8e75acf66313'
down_revision = '27e1193b66a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency', sa.Integer(), nullable=False))
        batch_op.alter_column('price',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_list', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.String(length=30),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.drop_column('currency')

    # ### end Alembic commands ###
