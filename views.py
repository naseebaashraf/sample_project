from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request, './myapp/about.html')

from.models  import user_login

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        # Select Query
        user_list = user_login.objects.filter(uname=uname, passwd=passwd, utype='admin')
        if len(user_list) == 1:
            # Setting Session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request, './myapp/admin_home.html', context)
        else:
            context = {'msg': 'Invalid Credentials!!!'}
            return render(request, './myapp/admin_login.html', context)
    else:
        return render(request, './myapp/admin_login.html')


def admin_home(request):
    context = {'uname': 'admin'}
    return render(request, './myapp/admin_home.html', context)


def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        try:
            uname = request.session['user_name']
        except:
            return render(request, './myapp/admin_login.html')
        try:
            user1 = user_login.objects.get(uname=uname, passwd=opasswd, utype='admin')
            # Update Query
            user1.passwd = npasswd
            user1.save()
            context = {'msg': 'Password Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Invalid Old Password'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        return render(request, './myapp/admin_changepassword.html')

def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return admin_login(request)
    except:
        return admin_login(request)

def admin_users_view(request):
    user_list = user_login.objects.all()
    context = {'user_list': user_list}
    return render(request, './myapp/admin_users_view.html', context)

from .models import student

def admin_add_student(request):
    if request.method == 'POST':
            sregno = request.POST.get('regno')
            sname = request.POST.get('name')
            scourse = request.POST.get('course')
            # utype = 'student'
            # insert query
            stud1 = student(sregno=sregno,sname=sname,scourse=scourse)
            stud1.save()
            context = {'msg': 'student details added successfully'}
            return render(request, './myapp/admin_add_student.html', context)
    else:
        context = {'msg':''}
        return render(request,'./myapp/admin_add_student.html',context)


def admin_view_student(request):
        s_list = student.objects.all()
        msg = ''
        context = {'msg': msg, 'stud_list': s_list}
        return render(request, './myapp/admin_view_student.html', context)


def admin_delete_student(request):
    sid = request.GET.get('id')
    sd = student.objects.get(id=int(sid))
    sd.delete()

    msg = 'deleted'
    s_list = student.objects.all()
    context = {'msg': msg, 'stud_list': s_list}
    return render(request, './myapp/admin_view_student.html', context)


########################   USER  ###################

def user_registration(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        utype = 'user'
        # Insert Query
        user1 = user_login(uname=uname, passwd=passwd, utype=utype)
        user1.save()
        context = {'msg':'User Registered'}
        return render(request,'./myapp/user_login.html',context)
    else:
        return render(request,'./myapp/user_registration.html')

def user_validation(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        # Select Query
        user_list = user_login.objects.filter(uname=uname, passwd=passwd, utype='user')
        if len(user_list) == 1:
            # Setting Session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request, './myapp/user_home.html', context)
        else:
            context = {'msg': 'Invalid Credentials!!!'}
            return render(request, './myapp/user_login.html', context)
    else:
        return render(request, './myapp/user_login.html')


def user_home(request):
    try:
        uname = request.session['user_name']
        context = {'uname':uname}
        return render(request, './myapp/user_home.html', context)
    except:
        return render(request, './myapp/user_login.html')

def user_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        try:
            uname = request.session['user_name']
        except:
            return render(request, './myapp/user_login.html')
        try:
            user1 = user_login.objects.get(uname=uname, passwd=opasswd, utype='user')
            # Update Query
            user1.passwd = npasswd
            user1.save()
            context = {'msg':'Password Changed'}
            return render(request, './myapp/user_changepassword.html',context)
        except user_login.DoesNotExist:
            context = {'msg':'Invalid Old Password'}
            return render(request, './myapp/user_changepassword.html',context)
    else:
        return render(request,'./myapp/user_changepassword.html')


def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return user_validation(request)
    except:
        return user_validation(request)

from .models import pic_pool
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def user_pic_pool_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(u_file.name,u_file)

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        pp = pic_pool(pic_path=pic_path, dt=dt, tm=tm)
        pp.save()
        context = {'msg': 'Picture Uploaded'}
        return render(request, './myapp/user_pic_pool_add.html', context)
    else:
        context = {'msg':''}
        return render(request,'./myapp/user_pic_pool_add.html',context)

def user_pic_pool_delete(request):
    id = request.GET.get('id')
    pp = pic_pool.objects.get(id=int(id))
    pp.delete()
    msg = 'Deleted'

    pic_list = pic_pool.objects.all()
    context = {'msg':msg,'pic_list':pic_list}
    return render(request,'./myapp/user_pic_pool_view.html',context)


def user_pic_pool_view(request):
    msg = ''
    pic_list = pic_pool.objects.all()
    context = {'msg': msg, 'pic_list': pic_list}
    return render(request, './myapp/user_pic_pool_view.html', context)

def user_view_only_student(request):
    s_list=student.objects.all()
    msg=''
    context={'msg':msg , 'stud_list':s_list}
    return render(request,'./myapp/user_view_only_student.html',context)


