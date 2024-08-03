"""initial migration

Revision ID: f82bce455ac9
Revises: 
Create Date: 2024-07-28 21:26:40.818812

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f82bce455ac9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todolist",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("item", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("price", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("is_done", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="todolist_pkey"),
    )


def downgrade() -> None:
    op.drop_table("todolist")
