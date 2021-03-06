"""Add thumbnails column

Revision ID: 80ecdb88cee2
Revises: b9308d306405
Create Date: 2021-02-05 16:32:50.041223

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '80ecdb88cee2'
down_revision = 'b9308d306405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('graphics', sa.Column('thumbnails', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('graphics', 'thumbnails')
    # ### end Alembic commands ###
