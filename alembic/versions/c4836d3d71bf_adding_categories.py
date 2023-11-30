"""adding categories

Revision ID: c4836d3d71bf
Revises: 9a82dbf52065
Create Date: 2023-11-29 01:38:08.867146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4836d3d71bf'
down_revision: Union[str, None] = '9a82dbf52065'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'category')
    # ### end Alembic commands ###
