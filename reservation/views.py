from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from reservation.models import studentdetails
from reservation.models import bookdetails
from reservation.models import bookreservation
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
#checks if user logged in. if yes, it will proceed, if not it will go to login page
# Create your views here.

#only authenthicated users on page 
@login_required
def dashboard(request):
	studentdata = studentdetails.objects.all()
	noofseniors= studentdetails.objects.filter(year='Senior').count()
	noofsoph= studentdetails.objects.filter(year='Sophomore').count()
	noofjuniors= studentdetails.objects.filter(year='Junior').count()
	chem = studentdetails.objects.filter(major='Chemistry').count()
	context = {'seniors':noofseniors, 'soph':noofsoph, 'juniors':noofjuniors, 'chem':chem}	
	return render(request, 'reservation/dashboard.html', context)
	


# css images video javacript
@login_required
def studentdata(request):
	studentdata = studentdetails.objects.all()
	paginator = Paginator(studentdata,10)
	page = request.GET.get('page')
	pagedata = paginator.get_page(page)
	context = {'data': pagedata}
	return render(request, 'reservation/studentdetails.html', context)

#def dictfetchall(cursor):
#    "Return all rows from a cursor as a dict"
#   columns = [col[0] for col in cursor.description]
#    return [
#       dict(zip(columns, row))
#        for row in cursor.fetchall()
#   ]
#def studentdetails(request):
#	cursorobj = connection.cursor
#	cursorobj.execute("SELECT * FROM reservation_studentdetails")
#	studentdata = cursorobj.fetchall()
#	context = {'data' : studentdata}
#	return render(request, 'reservation/studentdetails.html', context)
@login_required
def bookdata(request):
	bookdata = bookdetails.objects.all()
	paginator = Paginator(bookdata,10)
	page = request.GET.get('page')
	pagedata = paginator.get_page(page)
	context = {'data': pagedata}
	return render(request, 'reservation/bookdetails.html', context)

@login_required
def reserve(request):
	studentdata = studentdetails.objects.all()
	bookdata = bookdetails.objects.all()
	reservationdata = bookreservation.objects.all()
	context = {'studentnames': studentdata,'booknames': bookdata, 'reservationdata':reservationdata}
	return render(request, 'reservation/bookreservation.html', context)

@login_required
def savereservation(request):
	if('studentname' and 'bookname' in request.GET):
		studentnames = request.GET.get('studentname')
		booknames = request.GET.get('bookname')
		#reserved = bookdetails.objects.filter(reserved='0').count()
		#checks number times student name has occured in bookreservation table 
		num = bookreservation.objects.filter(studentname = studentnames).count()
		if num <= 2:
			dataobj = bookreservation(studentname = studentnames, bookname = booknames)
			dataobj.save()
			return HttpResponse('Success')
		else:
			return HttpResponse('Failure')
	

