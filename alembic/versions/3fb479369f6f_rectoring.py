"""rectoring

Revision ID: 3fb479369f6f
Revises: b4f4dff382b4
Create Date: 2023-12-02 10:51:42.872294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fb479369f6f'
down_revision: Union[str, None] = 'b4f4dff382b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('farmers', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('farmers', sa.Column('name', sa.String(length=60), nullable=False))
    op.add_column('farmers', sa.Column('email', sa.String(length=60), nullable=False))
    op.add_column('farmers', sa.Column('password', sa.String(length=60), nullable=False))
    op.add_column('farmers', sa.Column('location', sa.String(length=60), nullable=False))
    op.add_column('farmers', sa.Column('phone', sa.String(length=60), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('farmers', 'phone')
    op.drop_column('farmers', 'location')
    op.drop_column('farmers', 'password')
    op.drop_column('farmers', 'email')
    op.drop_column('farmers', 'name')
    op.drop_column('farmers', 'created_at')
    # ### end Alembic commands ###