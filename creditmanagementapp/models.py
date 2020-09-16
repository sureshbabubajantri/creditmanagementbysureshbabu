from django.db import models

# Create your models here.
class Add_User_Model(models.Model):
	# cus_id=models.AutoField(primary_key=True,editable=True)
	name=models.CharField(max_length=50)
	credit_amount=models.IntegerField(default="")
class Transfer_Table_Model(models.Model):
	name=models.CharField(max_length=50)
	recipient=models.CharField(max_length=50)
	credit=models.IntegerField(default="")