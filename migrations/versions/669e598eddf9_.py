"""empty message

Revision ID: 669e598eddf9
Revises: d2f287698332
Create Date: 2022-01-03 17:27:54.746611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '669e598eddf9'
down_revision = 'd2f287698332'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id_fk', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id_fk'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id_fk')
    # ### end Alembic commands ###