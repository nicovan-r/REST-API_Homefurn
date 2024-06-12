"""New Table: product_list

Revision ID: ab0e4c836a4a
Revises: a8e3dbc65b9b
Create Date: 2024-06-08 10:51:50.599917

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ab0e4c836a4a'
down_revision = 'a8e3dbc65b9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('barcode', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('qty', sa.Float(), nullable=True),
    sa.Column('qty_uom', sa.String(length=200), nullable=False),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('weight_uom', sa.String(length=200), nullable=False),
    sa.Column('storage_loc', sa.String(length=200), nullable=False),
    sa.Column('image', sa.String(length=300), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('barcode')
    )
    op.create_table('storage_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('storage_loc_code', sa.String(length=30), nullable=False),
    sa.Column('storage_loc_name', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('storage_loc_code')
    )
    with op.batch_alter_table('product_material_list', schema=None) as batch_op:
        batch_op.alter_column('uom',
               existing_type=mysql.VARCHAR(length=5),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_material_list', schema=None) as batch_op:
        batch_op.alter_column('uom',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=5),
               existing_nullable=False)

    op.drop_table('storage_location')
    op.drop_table('product_list')
    # ### end Alembic commands ###
