from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category    

class SubCategory(models.Model):     
    subCategory = models.CharField(max_length=200) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    def __str__(self):
        return self.subCategory

class State(models.Model):     
    states = models.CharField(max_length=200)

    def __str__(self):
        return self.states          

class CompanyDetail(models.Model):
    company = models.CharField(max_length=200)
    description = models.TextField(null=True)
    no_of_emp = models.CharField(max_length=200, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company

class Job(models.Model):
    company = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE)
    jobPosition = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Location
