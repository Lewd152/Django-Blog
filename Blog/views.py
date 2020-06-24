from django.http import JsonResponse
import time
from django.shortcuts import render
# 查询文章
# def select_article(request):
#     return JsonResponse({"status":True})


from TestBlog.models import Article
# PageNotAnInteger 判断页面传入的参数异常
# EmptyPage  判断不存在的页面
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import random
"""
插入测试数据
"""
def selectAll(request):
    #获取前端传入的页码
    n = request.GET.get('num',1)
    num = int(n)
    # 查询所有数据
    result = Article.objects.filter()
    # 设置一个分页，
    page = Paginator(result,4)
    # 获取当前页的数据
    # 获取异常
    try:
        page_data = page.page(num)
    except PageNotAnInteger:
        # 返回第一页数据
        page_data = page.page(1)
        return JsonResponse({"code":1})
    except EmptyPage:
        # 返回最后一页数据
        page_data = page.page(page.num_pages)
        return JsonResponse({"code": 0})

    arr = []
    for i in page_data:
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


def installArticle(request):
    title = request.GET['title']
    centen = request.GET['centen']
    group = request.GET['group']
    article = Article()
    article.title = title
    article.content = centen
    article.group = group
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    article.createTime = datetime
    # 保存数据
    article.save()
    return JsonResponse({"code":200})

# 跳转到新增页面
def index(request):
    return render(request,'index.html')

# 通过文章id删除
def deleteArticle(request):
    id = request.GET['id']
    Article.objects.filter(id=id).delete()
    return JsonResponse({"code":200})

# 跳转到删除页面
def delete(request):
    return render(request, 'delete.html')