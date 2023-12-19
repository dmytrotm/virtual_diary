"""create diary table

Revision ID: c1f45f858fb0
Revises: d1e288de40f4
Create Date: 2023-12-14 13:08:12.856301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1f45f858fb0'
down_revision: Union[str, None] = 'd1e288de40f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'diary',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(150)),
        sa.Column('user_id', sa.Integer(), nullable=False),
        # Add other columns as needed
    )

    op.create_foreign_key(
        'fk_diary_user_id',
        'diary', 'user',
        ['user_id'], ['id']
    )

def downgrade() -> None:
    op.drop_table('diary')

