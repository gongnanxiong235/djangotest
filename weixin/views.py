from django.shortcuts import render,HttpResponse,render_to_response,redirect
from weixin.models import models_mytest
from weixin.form import BookForm
import datetime
from django import views
# Create your views here.
def test(request):

    return HttpResponse("hello")

def current_time(request):
    current_time=datetime.datetime.now()
    return render(request,'time.html',{"current_time":current_time})

def userInfo(request):
    name=request.POST.get("name",None)
    sex=request.POST.get("sex",None)
    email=request.POST.get("email",None)
    user={"name":name,"sex":sex,"email":email}
    models_mytest.userInfo.objects.create(name=name, sex=sex, email=email)
    userList= models_mytest.userInfo.objects.all()
    #return render(request,"index.html",{"user_list":userList})
    return render(request, "index.html", locals())

#re_path(r'^active/[0-9]{4}/$',views.activite), #不带$表示最后是任意字符都可以匹配到
def activite(request):
    return HttpResponse("activity")

#re_path(r'^activity/([0-9]{4})/([0-9]{2})',views.activity), #  加小括号表示作为一个参数 映射到的view上的方法中药带此参数
def activity(request,year,month):
    return  HttpResponse(year+month)

#re_path(r'^group/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})',views.group),
def group(request,year,month):
    return HttpResponse(year + month)

#path('alex',views.alex,{"name":"alex"}),
#urls中的参数这里必须要放在方法的形参中，不然会报错
def alex(request,name):
    return HttpResponse(name)

def login(request):

    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        if username=='gnx' and password=='111111':
            return redirect("http://www.baidu.com")
        else:
            return redirect("/weixin/login/")
    #return render(request,"login.html")
    return render_to_response("login.html")


def template_method(request):
    name="gongnanxiong"
    number=200;
    mylist=[11,22,33,44]
    mydict={"name":"zhangsan","age":30,"job":"it"}
    person_list=[]
    date=datetime.datetime.now()
    safe="<a href=#>safe</a>"
    class Person(object):
        def __init__(self,username,age,job):
            self.name=username
            self.age=age
            self.job=job
        def __str__(self):
            return '%s:%s:%s' % (self.name,self.age,self.job)
        def fun(self):
            return "welcome"
    lisi=Person("lisi",28,"it")
    wangwu=Person("wangwu",29,"it")
    zhaoliu=Person("zhaoliu",30,"it")
    wangba=Person("wangba",31,"it")
    personList=[wangwu,zhaoliu,wangba]
    return render(request,"template_demo.html",locals())

def template_method_2(request):

    a=3
    return render(request,"template_demo_2.html",locals())

def order(request):
    return render(request,"odered.html")

def shop(request):
    return render(request,"shopping_car.html")

def li(request):
    objects=[11,22,33]
    return render(request,"li.html",locals())

def testsqlite(request):
    dict={"name":"zhangsan"}
    dict["sex"]=1
    dict["birthday"]=datetime.date(1986,3,30)
    dict["salary"]=1.0
    dict["emali"]='18151143059@163.com'
    dict["login_ip"]="127.0.0.121"
    dict["create_time"]=datetime.datetime.now()
    dict["update_time"]=datetime.datetime.now()
    models_mytest.user.objects.create(**dict)
    dt= models_mytest.user.objects.filter(name="zhangsan")
    return HttpResponse(dt.values())


def book(request):
    #models.Author.objects.create(name="gongnanxiong",emali="18151143059163com")
    a= models_mytest.Author.objects.all()
    print(a.filter(name="gongnanxiong").name)
    return HttpResponse("ddd")

def add(request):
    a=request.GET.get('a',0)
    b=request.GET.get('b',0)
    result=int(a)+int(b)
    print(request.META)
    return HttpResponse(str(result))


def add2(request,a,b):
    return HttpResponse(str(int(a)+int(b)))

def home(request):
    hello=map(str,range(100))
    hello_dict=dict([('hello','world'),('my','name'),('haha','xixi')])
    return render(request,'home.html',{'hello':hello,'hello_dict':hello_dict})


class IndexView(views.View):
    # 如果是GET请求，那么返回一个空的表单
    def get(self, request):
        form = BookForm()
        return render(request, 'book.html', {'form': form})

    # 如果是POST请求，那么将提交上来的数据进行校验
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            page = form.cleaned_data.get('page')
            price = form.cleaned_data.get('price')
            print('=' * 30)
            print(title)
            print(page)
            print(price)
            print('=' * 30)
            # 在验证完成后直接调用save方法，就可以将这个数据保存到数据库中了
            form.save()

            return HttpResponse('表单验证成功')
        else:
            # 点上get_json_data()它，打印的错误信息会以json方式显示
            print(form.errors.get_json_data())
            return HttpResponse('表单验证失败')


