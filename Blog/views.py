from django.http import JsonResponse


# 查询文章
# def select_article(request):
#     return JsonResponse({"status":True})


from TestBlog.models import Article
import random
"""
插入测试数据
"""
def select(request):
    # 查询name = tom1的数据
    result = Article.objects.filter()
    print(result)
    """
    result为<class 'django.db.models.query.QuerySet'>的对象
    需要进行数据处理
    """
    arr = []
    for i in result:
        content = {'id': i.id, 'title': i.title, 'content': i.content,'createdata': i.createTime,'group': i.group}
        arr.append(content)
    print(arr)
    rejson = {
        'data':arr,
        'status':True
    }
    return JsonResponse(rejson)