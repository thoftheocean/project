"""empty message

Revision ID: 43142f2ac846
Revises: ef17fd21a7d6
Create Date: 2017-06-20 09:48:13.996969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43142f2ac846'
down_revision = 'ef17fd21a7d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
