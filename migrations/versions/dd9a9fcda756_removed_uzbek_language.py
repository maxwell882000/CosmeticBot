"""Removed Uzbek Language

Revision ID: dd9a9fcda756
Revises: fafdaee608dc
Create Date: 2020-09-21 19:22:13.165551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd9a9fcda756'
down_revision = 'fafdaee608dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dish_categories', 'name_uz')
    op.drop_column('dishes', 'description_uz')
    op.drop_column('dishes', 'name_uz')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dishes', sa.Column('name_uz', sa.VARCHAR(length=100), nullable=True))
    op.add_column('dishes', sa.Column('description_uz', sa.VARCHAR(length=500), nullable=True))
    op.add_column('dish_categories', sa.Column('name_uz', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
