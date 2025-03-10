"""update user model

Revision ID: aa5f6e51a828
Revises: 4474c9e0b355
Create Date: 2025-01-25 17:21:36.441885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa5f6e51a828'
down_revision: Union[str, None] = '4474c9e0b355'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_uid_key', 'users', type_='unique')
    op.drop_column('users', 'uid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uid', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_uid_key', 'users', ['uid'])
    # ### end Alembic commands ###
