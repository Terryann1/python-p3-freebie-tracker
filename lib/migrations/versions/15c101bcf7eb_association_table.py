"""association table

Revision ID: 15c101bcf7eb
Revises: a712f3f5edaf
Create Date: 2025-03-05 19:15:19.408998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15c101bcf7eb'
down_revision = 'a712f3f5edaf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'companies_devs',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
)


def downgrade() -> None:
    op.drop_table='companies_devs'
