"""empty message

Revision ID: 2a8c83dde69a
Revises: 28a3c53d2851
Create Date: 2024-02-03 04:36:22.349536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a8c83dde69a'
down_revision: Union[str, None] = '28a3c53d2851'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###