from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def login(request):
    if request.method == 'POST':
        #รับค่าจากฟอร์ม
        username = request.POST['username']
        password = request.POST['password']
          #ตรวจสอบค่าว่าง
        if username =='' or password =='':
            messages.warning(request,'กรุณาป้อนข้อมูลให้ครบ')
            return redirect('/login')
        else:
            #เข้าสู่ระบบ
            user = auth.authenticate(username=username,password=password)
            #มีข้อมูลอยู่ในระบบ
            if user is not None :
                auth.login(request,user)
                return redirect('/')
            else:
                messages.warning(request,'ไม่มีบัญชีนี้ในระบ')
                return redirect('/login')
    
    else:
        return render(request,'login.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if username == '' or password =='' or repassword =='' or first_name=='' or last_name =='':
            messages.warning(request,'กรุณาป้อนข้อมูลให้ครบ')
            return redirect('/register')
        else:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    messages.warning(request,'Username มีคนใช้แล้ว')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
                    messages.success(request,'สร้างบัญชีเรียบร้อย')
                    user.save()
                    return redirect('/register')
            else:
                messages.warning(request,'รหัสผ่านไม่ตรงกัน')
                return redirect('/register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')


