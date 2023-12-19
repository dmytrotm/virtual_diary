"""Create Note table

Revision ID: df026cb5e5f8
Revises: c1f45f858fb0
Create Date: 2023-12-14 13:29:07.248250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df026cb5e5f8'
down_revision: Union[str, None] = 'c1f45f858fb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'note',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('data', sa.String(10000)),
        sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('diary_id', sa.Integer(), sa.ForeignKey('diary.id'), nullable=False),
        # Add other columns as needed
    )


def downgrade() -> None:
    op.drop_table('note')
