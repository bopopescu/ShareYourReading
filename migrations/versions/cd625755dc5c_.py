"""empty message

Revision ID: cd625755dc5c
Revises: 71af79794684
Create Date: 2020-05-03 20:20:05.533393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd625755dc5c'
down_revision = '71af79794684'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('user_type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_title', sa.String(length=200), nullable=False),
    sa.Column('post_content', sa.Text(), nullable=False),
    sa.Column('post_time', sa.DateTime(), nullable=True),
    sa.Column('comment_num', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('comment',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('comment_content', sa.String(length=2000), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
