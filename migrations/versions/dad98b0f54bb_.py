"""empty message

Revision ID: dad98b0f54bb
Revises: None
Create Date: 2016-01-09 15:50:28.719844

"""

# revision identifiers, used by Alembic.
revision = 'dad98b0f54bb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social_media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=15), nullable=True),
    sa.Column('atr', sa.VARCHAR(length=2), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('updatedtime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=45), nullable=True),
    sa.Column('username', sa.VARCHAR(length=15), nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), nullable=True),
    sa.Column('email', sa.VARCHAR(length=30), nullable=True),
    sa.Column('bio', sa.VARCHAR(length=20), nullable=True),
    sa.Column('picture', sa.VARCHAR(length=50), nullable=True),
    sa.Column('updatedtime', sa.DateTime(), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('id_type_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_type_user'], ['user_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=True),
    sa.Column('slug', sa.VARCHAR(length=50), nullable=True),
    sa.Column('content', sa.VARCHAR(length=100), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('updatetime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('social_media_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_socmed', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('value', sa.VARCHAR(length=45), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('updatedtime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_socmed'], ['social_media.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_post', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('desc', sa.VARCHAR(length=50), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('updatetime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_post', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('createdtime', sa.DateTime(), nullable=True),
    sa.Column('updatetime', sa.DateTime(), nullable=True),
    sa.Column('deletedtime', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    op.drop_table('comment')
    op.drop_table('social_media_user')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('user_type')
    op.drop_table('social_media')
    ### end Alembic commands ###
