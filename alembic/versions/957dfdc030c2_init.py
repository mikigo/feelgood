"""init

Revision ID: 957dfdc030c2
Revises: 
Create Date: 2023-05-04 02:07:17.325765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '957dfdc030c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appname',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('package', sa.String(length=100), nullable=True, comment='包名'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_appname_app_name'), 'appname', ['app_name'], unique=False)
    op.create_index(op.f('ix_appname_id'), 'appname', ['id'], unique=False)
    op.create_table('framework',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('description', sa.String(length=1000), nullable=True, comment='描述'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_framework_id'), 'framework', ['id'], unique=False)
    op.create_index(op.f('ix_framework_platform'), 'framework', ['platform'], unique=False)
    op.create_table('scene',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('frame_work', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('scene', sa.String(length=100), nullable=True, comment='场景'),
    sa.Column('description', sa.String(length=1000), nullable=True, comment='描述'),
    sa.Column('is_online', sa.Boolean(), nullable=True, comment='是否上线'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['app_name'], ['appname.app_name'], ),
    sa.ForeignKeyConstraint(['frame_work'], ['framework.platform'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scene_app_name'), 'scene', ['app_name'], unique=False)
    op.create_index(op.f('ix_scene_frame_work'), 'scene', ['frame_work'], unique=False)
    op.create_index(op.f('ix_scene_id'), 'scene', ['id'], unique=False)
    op.create_table('testapplicationversion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('frame_work', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('version', sa.String(length=20), nullable=True, comment='版本'),
    sa.Column('test_time', sa.DateTime(), nullable=True, comment='测试时间'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['app_name'], ['appname.app_name'], ),
    sa.ForeignKeyConstraint(['frame_work'], ['framework.platform'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_testapplicationversion_app_name'), 'testapplicationversion', ['app_name'], unique=False)
    op.create_index(op.f('ix_testapplicationversion_frame_work'), 'testapplicationversion', ['frame_work'], unique=False)
    op.create_index(op.f('ix_testapplicationversion_id'), 'testapplicationversion', ['id'], unique=False)
    op.create_table('perfdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('frame_work', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('scene', sa.String(length=100), nullable=True, comment='场景'),
    sa.Column('number', sa.Integer(), nullable=True, comment='次数'),
    sa.Column('test_time', sa.DateTime(), nullable=True, comment='测试时间'),
    sa.Column('report_url', sa.String(), nullable=True, comment='测试报告url'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['app_name'], ['appname.app_name'], ),
    sa.ForeignKeyConstraint(['frame_work'], ['framework.platform'], ),
    sa.ForeignKeyConstraint(['scene'], ['scene.scene'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_perfdata_app_name'), 'perfdata', ['app_name'], unique=False)
    op.create_index(op.f('ix_perfdata_frame_work'), 'perfdata', ['frame_work'], unique=False)
    op.create_index(op.f('ix_perfdata_id'), 'perfdata', ['id'], unique=False)
    op.create_table('perfdataday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('frame_work', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('scene', sa.String(length=100), nullable=True, comment='场景'),
    sa.Column('time_consume', sa.Float(), nullable=True, comment='耗时'),
    sa.Column('test_time', sa.DateTime(), nullable=True, comment='测试时间'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['app_name'], ['appname.app_name'], ),
    sa.ForeignKeyConstraint(['frame_work'], ['framework.platform'], ),
    sa.ForeignKeyConstraint(['scene'], ['scene.scene'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_perfdataday_app_name'), 'perfdataday', ['app_name'], unique=False)
    op.create_index(op.f('ix_perfdataday_frame_work'), 'perfdataday', ['frame_work'], unique=False)
    op.create_index(op.f('ix_perfdataday_id'), 'perfdataday', ['id'], unique=False)
    op.create_table('temporarytable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=20), nullable=True, comment='应用名称'),
    sa.Column('frame_work', sa.String(length=20), nullable=True, comment='架构'),
    sa.Column('scene', sa.String(length=100), nullable=True, comment='场景'),
    sa.Column('number', sa.Integer(), nullable=True, comment='次数'),
    sa.Column('test_time', sa.DateTime(), nullable=True, comment='测试时间'),
    sa.Column('report_url', sa.String(), nullable=True, comment='测试报告url'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['app_name'], ['appname.app_name'], ),
    sa.ForeignKeyConstraint(['frame_work'], ['framework.platform'], ),
    sa.ForeignKeyConstraint(['scene'], ['scene.scene'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_temporarytable_app_name'), 'temporarytable', ['app_name'], unique=False)
    op.create_index(op.f('ix_temporarytable_frame_work'), 'temporarytable', ['frame_work'], unique=False)
    op.create_index(op.f('ix_temporarytable_id'), 'temporarytable', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_temporarytable_id'), table_name='temporarytable')
    op.drop_index(op.f('ix_temporarytable_frame_work'), table_name='temporarytable')
    op.drop_index(op.f('ix_temporarytable_app_name'), table_name='temporarytable')
    op.drop_table('temporarytable')
    op.drop_index(op.f('ix_perfdataday_id'), table_name='perfdataday')
    op.drop_index(op.f('ix_perfdataday_frame_work'), table_name='perfdataday')
    op.drop_index(op.f('ix_perfdataday_app_name'), table_name='perfdataday')
    op.drop_table('perfdataday')
    op.drop_index(op.f('ix_perfdata_id'), table_name='perfdata')
    op.drop_index(op.f('ix_perfdata_frame_work'), table_name='perfdata')
    op.drop_index(op.f('ix_perfdata_app_name'), table_name='perfdata')
    op.drop_table('perfdata')
    op.drop_index(op.f('ix_testapplicationversion_id'), table_name='testapplicationversion')
    op.drop_index(op.f('ix_testapplicationversion_frame_work'), table_name='testapplicationversion')
    op.drop_index(op.f('ix_testapplicationversion_app_name'), table_name='testapplicationversion')
    op.drop_table('testapplicationversion')
    op.drop_index(op.f('ix_scene_id'), table_name='scene')
    op.drop_index(op.f('ix_scene_frame_work'), table_name='scene')
    op.drop_index(op.f('ix_scene_app_name'), table_name='scene')
    op.drop_table('scene')
    op.drop_index(op.f('ix_framework_platform'), table_name='framework')
    op.drop_index(op.f('ix_framework_id'), table_name='framework')
    op.drop_table('framework')
    op.drop_index(op.f('ix_appname_id'), table_name='appname')
    op.drop_index(op.f('ix_appname_app_name'), table_name='appname')
    op.drop_table('appname')
    # ### end Alembic commands ###
