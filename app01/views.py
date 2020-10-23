from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.
#展示出版社
def publish_list(request):
    # 获取所有的的出版社信息
    all_publishers = models.publisher.objects.all().order_by('pk')
    # 返回一个页面，页面中包含所以出版社信息
    return render(request, 'publish_list.html', {'all_publishers': all_publishers})

#添加出版社
def publish_add(request):
    # post请求、
    if request.method == 'POST':
        # 获取用户提交的数据
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publish_add.html', {'error': '出版社不能为空'})
        if models.publisher.objects.filter(name=pub_name):
            # 数据库中有重复的名字
            return render(request, 'publish_add.html', {'error': '出版社名称已存在'})
        # 将数据新增到数据库中
        models.publisher.objects.create(name=pub_name)
        # 返回一个重定向到展示出版社的页面
        return redirect("/publish_list/")
    return render(request, 'publish_add.html')
#添加出版社 cbv
from django.views import View
class PublisherAdd(View):

    def get(self, request):
        #处理get请求的逻辑
        return render(request, 'publish_add.html')
    def post(self, request):
        # 获取用户提交的数据
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publish_add.html', {'error': '出版社不能为空'})
        if models.publisher.objects.filter(name=pub_name):
            # 数据库中有重复的名字
            return render(request, 'publish_add.html', {'error': '出版社名称已存在'})
        # 将数据新增到数据库中
        models.publisher.objects.create(name=pub_name)
        # 返回一个重定向到展示出版社的页面
        return redirect("/publish_list/")

# 删除出版社
def publish_del(request):
    # 获取要删除数据的id
    pk = request.GET.get('pk')
    # 根据id到数据库进行删除
    # models.publisher.objects.filter(pk=pk).delete() #查询到对象，删除对象
    models.publisher.objects.filter(pk=pk).delete()  # 查询一个对象列表，删除对象列表所有对象
    # 返回重定向到出版社页面
    return redirect('/publish_list/')

#编辑出版社
def publish_edit(request):
    # get 返回一个页面 页面包含form表单 input有原始的数据
    pk = request.GET.get('pk')
    pub_obj = models.publisher.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'publish_edit.html', {'pub_obj': pub_obj})
    # POST
    else:
        pub_name = request.POST.get('pub_name')  # 获取要修改后的内容
        pub_obj.name = pub_name  # 只是再内存中修改
        pub_obj.save()  # 将修改操提交到数据库
        return redirect('/publish_list/')

#展示书
def book_list(request):
    # 查询所有的数据
    all_books = models.Book.objects.all()
    # for book in all_books:
    #     print(book)    #拿到 book对象
    #     print(book.pk)  #拿到  book表的主键
    #     print(book.name) #拿到  book表 name栏位
    #     print(book.publisher_id)  #拿到外键
    #     print(book.publisher)  #拿到 publisher表 对象
    #     print(book.publisher.name)  #拿到 publ表中name 栏位
    return render(request, 'book_list.html', {'all_books': all_books})

#添加书
def book_add(request):
    error = ''
    if request.method == "POST":
        #获取用户提交数据
        book_name = request.POST.get('book_name')
        if not book_name:
            error = '书名不能为空'
        elif models.Book.objects.filter(name=book_name):
            error = '书名已存在'
        else:
            models.Book.objects.create(name=book_name, publisher_id=request.POST.get('publisher.pk'))
            return redirect('/book_list/')
    all_publisher = models.publisher.objects.all()
    return render(request, 'book_add.html', {'all_publisher': all_publisher, 'error': error})
#删除书
def book_del(request):
    #获取用户提交的要删除id
    pk = request.GET.get('pk')
    #获取要删除的对象，删除
    models.Book.objects.filter(pk=pk).delete()
    #回复一个重定向页面
    return redirect('/book_list/')
# 编辑书
def book_edit(request):
    # 查询要编辑的id
    pk = request.GET.get('pk')
    # 根据id 查询到要编辑的对象
    book_obj = models.Book.objects.get(pk=pk)
    # post
    if request.method == 'POST':
        # 获取用户提交的数据
        book_name = request.POST.get('book_name')
        publisher_pk = request.POST.get('publisher_pk')
        # # 编辑用户的更改
        # 方法1
        # book_obj.name = book_name
        # book_obj.publisher_id = publisher_pk
        # book_obj.save()  # 保存到数据库中
        # 方式2
        models.Book.objects.filter(pk=pk).update(name=book_name, publisher_id=publisher_pk)
        # 重定向到展示页面
        return redirect('/book_list/')
    # get请求
    all_publisher = models.publisher.objects.all()
    # 返回一个页面 包含原始数据
    return render(request, 'book_edit.html', {'book_obj': book_obj, 'all_publisher': all_publisher})

#展示作者
def author_list(request):
    #查找所有的作者
    all_author = models.author.objects.all()
    # for author in all_author:
    #     # print(author.books, type(author.books)) #关系管理对象
    #     # print(author.books.all()) #所关联的所有对象
    #     # print('*'*40)
    #返回一个页面，包含所有的作者
    return render(request,'author_list.html', {'all_authors': all_author})
#新增作者
def author_add(request):
    if request.method == 'POST':
        # post
        author_name = request.POST.get('author_name')
        # 获取用户提交的数据
        book_ids = request.POST.getlist('book_ids') #getlist  获取多个数据
        # 向数据库中插入数据
        #向作者表插入了作者的信息
        author_obj = models.author.objects.create(name=author_name)
        #改作者和提交的数据绑定多对多的关系
        author_obj.books.set(book_ids) #设置多对多关系
        # 返回重定向到展示作者页面
        return redirect('/author_list/')
    # get
    # 查询所有的书籍
    all_books = models.Book.objects.all()
    #返回一个页面，保护form表单，让用户输入作者姓名，选择作品
    return render(request, 'author_add.html', {'all_books': all_books})

def author_del(request):
    #获取要删除对象的ID
    pk = request.GET.get('id')
    #根据id查询到对象进行删除
    models.author.objects.filter(pk=pk).delete()  #删除了作者，也删除了和该作者相关的书籍
    #返回重定向到展示作业页面
    return redirect('/author_list/')

def author_edit(request):
    #get
    #获取要编辑对象的id
    pk = request.GET.get('id')
    # 根据id获取到对象
    author_obj = models.author.objects.get(pk=pk)
    #post
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')
    #获取用户提交的书籍
    #修改书籍
        author_obj.name = author_name
        author_obj.save()
        #修改作者和书的多对多关系
        author_obj.books.set(book_ids)  #重新设置
    #返回重定向到展示页面
        return redirect('/author_list/')

    # 获取所有的书籍
    all_books = models.Book.objects.all()
    #返回一个页面，页面中包含作者的姓名，包含代表作品
    return render(request, 'author_edit.html', {'author_obj': author_obj, 'all_books':all_books})