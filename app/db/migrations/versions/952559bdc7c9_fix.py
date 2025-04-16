"""fix

Revision ID: 952559bdc7c9
Revises: 3515b3914f75
Create Date: 2025-04-16 14:49:04.297673

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "952559bdc7c9"
down_revision: Union[str, None] = "3515b3914f75"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("table", sa.Column("seats", sa.Integer(), nullable=False))
    op.drop_column("table", "seets")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "table", sa.Column("seets", sa.INTEGER(), autoincrement=False, nullable=False)
    )
    op.drop_column("table", "seats")
    # ### end Alembic commands ###
