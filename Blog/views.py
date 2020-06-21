from django.http import JsonResponse


# 查询文章
# def select_article(request):
#     return JsonResponse({"status":True})


from TestBlog.models import Article
import random
"""
插入测试数据
"""
def selectAll(request):
    # 查询所有数据
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

# 根据关键字查询
def selectKeyword(request):
    keyword = request.GET['keyword']
    # 如果搜索为空，返回全部内容
    if keyword == "":
        # 查询所有数据
        result = Article.objects.filter()
        print(result)
        """
        result为<class 'django.db.models.query.QuerySet'>的对象
        需要进行数据处理
        """
        arr = []
        for i in result:
            content = {'id': i.id, 'title': i.title, 'content': i.content, 'createdata': i.createTime, 'group': i.group}
            arr.append(content)
        print(arr)
        rejson = {
            'data': arr,
            'status': True
        }
        return JsonResponse(rejson)
    if keyword !="":
        # 模糊查询
        result = Article.objects.filter(title__contains=keyword)

        arr = []
        for i in result:
            content = {'id': i.id, 'title': i.title, 'content': i.content, 'createdata': i.createTime, 'group': i.group}
            arr.append(content)
        print(arr)
        rejson = {
            'data': arr,
            'status': True
        }
        return JsonResponse(rejson)

# 按前端传递的分组查询
def selectGroup(request):
    group = request.GET['group']
    result = Article.objects.filter(group=group)
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