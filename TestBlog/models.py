"""
创建学生信息表模型
"""
from django.db import models

"""
 该类是用来生成数据库的 必须要继承models.Model
"""
class Article(models.Model):
    """
    创建如下几个表的字段
    """
    # id
    id = models.IntegerField('id', primary_key=True,null=False)
    # 标题
    title = models.CharField('标题',max_length=15,null=False)
    # 文章内容
    content = models.CharField('内容',max_length=1500,null=False)
    # 创建时间
    createTime = models.CharField('创建时间',max_length=15,null=False)
    # 分组
    group = models.CharField('手机',max_length=15, null=False)

    # 指定表名 不指定默认APP名字——类名(app_demo_Student)
    class Meta:
        db_table = 'article'
