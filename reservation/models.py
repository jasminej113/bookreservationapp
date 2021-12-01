from django.db import models

#class dashboardstats(models.Model):
#	seniors = models.CharField(max_length=500, null=True)
#	freshman = models.CharField(max_length=500, null=True)
#	juniors = models.CharField(max_length=500, null=True)
#	chem = models.CharField(max_length=500, null=True)
	
	
# Create your models here.
class studentdetails(models.Model):
	firstname = models.CharField(max_length=500)
	lastname = models.CharField(max_length=500)
	year = models.CharField(max_length=500)
	major = models.CharField(max_length=500)
	gpa = models.DecimalField(decimal_places=2,max_digits=3)
	

class bookdetails(models.Model):
	bookid = models.IntegerField()
	booktitle = models.CharField(max_length=500)
	bookauthor = models.CharField(max_length=500)
	reserved = models.IntegerField()
	
	
class bookreservation(models.Model):
	studentname = models.CharField(max_length=500)
	bookname = models.CharField(max_length=500)
	