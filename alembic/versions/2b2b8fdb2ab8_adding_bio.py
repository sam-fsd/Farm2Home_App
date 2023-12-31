"""adding bio

Revision ID: 2b2b8fdb2ab8
Revises: c4836d3d71bf
Create Date: 2023-11-29 02:06:34.946211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b2b8fdb2ab8'
down_revision: Union[str, None] = 'c4836d3d71bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'category',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'category',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
