import os
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from moneyapp.models import Statement
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError


@login_required(login_url='/login')
def index(request):
    data = Statement.objects.filter(manager=request.user)
    # if Statement.objects.get() is not None:
    #ผลรวมทั้งหมดของรายรับ-รายจ่าย แล้วนำแค่ในส่วนของจำนวนเงินมาบวกกันทั้งหมด
    total_income = Statement.objects.filter(category='income',manager=request.user).aggregate(Sum('amount'))
    total_expense = Statement.objects.filter(category='expense',manager=request.user).aggregate(Sum('amount'))

  
    total = float(total_income['amount__sum'] or 0) - float(total_expense['amount__sum'] or 0)
    return render(request,'index.html',{'total_income':total_income,'total_expense':total_expense,'total':total,'data':data})


@login_required(login_url='/login')
def account(request):
    

    data = Statement.objects.all()
    return render(request,'account.html',{'data':data })

@login_required(login_url='/login')
def input(request):
    if request.method =='POST':
        #ดึงข้อมูลจาก form 
         #เช็คค่าว่าง
        name = request.POST['name']
        amount = request.POST['amount']
        category = request.POST['flexRadioDefault']
        # pic = request.FILES['pic']
        try: pic = request.FILES['pic']
        except MultiValueDictKeyError:
            pic = 'nopic'
        if amount == '' or name =='':
            
            #ส่งข้อความแจ้งเตือน
            messages.warning(request,'กรุณาป้อนชื่อรายการ')
            return redirect('forninput')
            
        else:
            data = Statement.objects.create(name=name,amount=amount,category=category,cover=pic,manager=request.user)
            data.save()
            messages.success(request,'บันทึกข้อมูลเสร็จสิ้น')
            return redirect('/')
            
   
    else:
        return render(request,'input.html')

def delete(request,statement_id):
    data = Statement.objects.get(id=statement_id)
    if data.manager == request.user:
        data.delete()
        messages.success(request,"ลบข้อมูลเรียบร้อย")
        return redirect("/")
    else:
        messages.warning(request,'คุณไม่มีสิทธื์การเข้าถึง')
        return redirect("/")
    

