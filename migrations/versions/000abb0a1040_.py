"""empty message

Revision ID: 000abb0a1040
Revises: be485eff3258
Create Date: 2022-02-01 16:22:51.771611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '000abb0a1040'
down_revision = 'be485eff3258'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('game_player_id_fk_fkey', 'game', type_='foreignkey')
    op.drop_column('game', 'player_id_fk')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('player_id_fk', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('game_player_id_fk_fkey', 'game', 'player', ['player_id_fk'], ['player_id'])
    # ### end Alembic commands ###
