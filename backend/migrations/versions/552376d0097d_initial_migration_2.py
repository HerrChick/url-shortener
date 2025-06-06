"""Initial migration 2

Revision ID: 552376d0097d
Revises: 63f89c42e516
Create Date: 2025-04-29 19:21:27.580094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '552376d0097d'
down_revision: Union[str, None] = '63f89c42e516'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URLs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unshortened_url', sa.String(), nullable=True),
    sa.Column('shortened_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_URLs_id'), 'URLs', ['id'], unique=False)
    op.create_index(op.f('ix_URLs_shortened_url'), 'URLs', ['shortened_url'], unique=True)
    op.create_index(op.f('ix_URLs_unshortened_url'), 'URLs', ['unshortened_url'], unique=True)
    op.create_table('examples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_examples_id'), 'examples', ['id'], unique=False)
    op.create_index(op.f('ix_examples_name'), 'examples', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_examples_name'), table_name='examples')
    op.drop_index(op.f('ix_examples_id'), table_name='examples')
    op.drop_table('examples')
    op.drop_index(op.f('ix_URLs_unshortened_url'), table_name='URLs')
    op.drop_index(op.f('ix_URLs_shortened_url'), table_name='URLs')
    op.drop_index(op.f('ix_URLs_id'), table_name='URLs')
    op.drop_table('URLs')
    # ### end Alembic commands ###
