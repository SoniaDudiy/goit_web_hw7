"""Init

Revision ID: 2ce0f041b558
Revises: 
Create Date: 2023-11-10 19:11:10.147090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ce0f041b558'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('name', sa.String(length=150), nullable=False))
    op.drop_column('groups', 'group_name')
    op.add_column('lessons', sa.Column('name', sa.String(), nullable=True))
    op.drop_constraint('lessons_teacher_id_fkey', 'lessons', type_='foreignkey')
    op.create_foreign_key(None, 'lessons', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.drop_column('lessons', 'lessons_name')
    op.add_column('scores', sa.Column('value', sa.Integer(), nullable=True))
    op.add_column('scores', sa.Column('date', sa.Date(), nullable=True))
    op.drop_constraint('scores_lesson_id_fkey', 'scores', type_='foreignkey')
    op.drop_constraint('scores_student_id_fkey', 'scores', type_='foreignkey')
    op.create_foreign_key(None, 'scores', 'lessons', ['lesson_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'scores', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.drop_column('scores', 'score')
    op.drop_column('scores', 'created_at')
    op.add_column('students', sa.Column('name', sa.String(length=150), nullable=False))
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'groups', ['group_id'], ['id'], ondelete='CASCADE')
    op.drop_column('students', 'student_name')
    op.add_column('teachers', sa.Column('name', sa.String(length=150), nullable=False))
    op.drop_column('teachers', 'teacher_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teachers', sa.Column('teacher_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('teachers', 'name')
    op.add_column('students', sa.Column('student_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_group_id_fkey', 'students', 'groups', ['group_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('students', 'name')
    op.add_column('scores', sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('scores', sa.Column('score', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.create_foreign_key('scores_student_id_fkey', 'scores', 'students', ['student_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('scores_lesson_id_fkey', 'scores', 'lessons', ['lesson_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('scores', 'date')
    op.drop_column('scores', 'value')
    op.add_column('lessons', sa.Column('lessons_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'lessons', type_='foreignkey')
    op.create_foreign_key('lessons_teacher_id_fkey', 'lessons', 'teachers', ['teacher_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('lessons', 'name')
    op.add_column('groups', sa.Column('group_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('groups', 'name')
    # ### end Alembic commands ###
