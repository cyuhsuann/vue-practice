"""Add a column

Revision ID: 7c25cb934dfb
Revises: f82bce455ac9
Create Date: 2024-08-04 12:42:59.442245

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c25cb934dfb"
down_revision: Union[str, None] = "f82bce455ac9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("todolist", sa.Column("last_transaction_date", sa.DateTime))


def downgrade() -> None:
    op.drop_column("todolist", "last_transaction_date")
