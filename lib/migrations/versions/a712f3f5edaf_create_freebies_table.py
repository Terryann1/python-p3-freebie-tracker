"""create freebies table

Revision ID: a712f3f5edaf
Revises: 5f72c58bf48c
Create Date: 2025-03-05 11:44:22.720704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a712f3f5edaf'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('freebies',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('item_name',sa.String(),nullable=False),
    sa.Column('value',sa.Integer(),nullable=False),
    sa.Column('dev_id',sa.Integer(),nullable=False),
    sa.Column('company_id',sa.Integer(),nullable=False)
    )


    


def downgrade() -> None:
    op.drop_table('freebies')

    
