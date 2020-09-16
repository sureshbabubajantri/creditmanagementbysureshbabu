from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .forms import Add_User_Form
from .models import Add_User_Model,Transfer_Table_Model
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = Add_User_Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()#messages.info(request,"success")
			return redirect("/")
	else:
		form = Add_User_Form()
	return render(request,"home.html",{'form':form})#return render(request,'home.html')
def viewuser(request):
	objs=Add_User_Model.objects.all()
	# c=Add_User_Model.objects.count()

	#args={'user':request.Add_User_Model}
	return render(request,"viewuser.html",{'objs':objs})
def transfer(request,name):
	c=Add_User_Model.objects.count()
	print(c)
	objs=Add_User_Model.objects.all()
	obj=Add_User_Model.objects.filter(name=name).first()
	context={
	'obj':obj,
	'objs':objs
	}
	return render(request,"transfer.html",context)
mes=""
l=[1,2,3,4,5]
def confirmation(request, name):
    recipient = request.POST.get("recipient")
    credit = request.POST.get("credit")
    sender = Add_User_Model.objects.filter(name=name).first()
    receiver = Add_User_Model.objects.filter(name=recipient).first()
    updatedReceiverCredit = receiver.credit_amount+int(credit)
    updatedSenderCredit = sender.credit_amount-int(credit)
    if sender.credit_amount>=int(credit):
        status = True
        # update credits to database
        updateSender = Add_User_Model.objects.get(name=sender.name)
        updateSender.credit_amount = updatedSenderCredit
        updateSender.save()
        updateReceiver = Add_User_Model.objects.get(name=receiver.name)
        updateReceiver.credit_amount = updatedReceiverCredit
        updateReceiver.save()
        message=messages.success(request,''+credit+' credits have been sent to '+recipient+' from '+name)
        transfers=Transfer_Table_Model.objects.create(name=name,recipient=recipient,credit=credit)
        #messages.add_message(request,messages.INFO,''+credit+' credits have been sent to '+recipient+' from '+name)
        
        # for i in messages:
        # 	mes=+str(i)+'\n'
    else:
        status = False

    objs = Add_User_Model.objects.all()
    trans=Transfer_Table_Model.objects.all()

    context = {
        'status': status,
        'name': name,
        'recipient': recipient,
        'credit': credit,
        'objs':objs,
        'trans':trans,
        'transfers':transfers,
        'message':message
    }
    print(messages)
    return render(request, 'confirmation.html', context)
def transfertable(request):
	trans=Transfer_Table_Model.objects.all()
	context={
	'trans':trans
	}
	return render(request,'transfertable.html',context)