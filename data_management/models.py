from django.db import models

# Create your models here.


class School(models.Model):
    school_name = models.CharField(max_length=50)

class SchoolClass(models.Model):
    class_name = models.CharField(max_length=10)

class Subject(models.Model):
    subject = models.CharField(max_length=10)
    # subject_score = models.FloatField(default=None)


class Student(models.Model):
    student_id = models.IntegerField()
    full_name =  models.CharField(max_length=50)

class AssesmentArea(models.Model):
    assesment_area_name = models.CharField(max_length=20)

class Answer(models.Model):
    answeres =  models.CharField(max_length=1)

class Award(models.Model):
    award_name =  models.CharField(max_length=10)

class Summary(models.Model):
    school =  models.ForeignKey(School,on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.IntegerField()
    assesment_area = models.ForeignKey(AssesmentArea,on_delete=models.CASCADE)
    award = models.ForeignKey(Award,on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass,on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='summary_answers')
    correct_answer = models.ForeignKey(Answer,on_delete=models.CASCADE, related_name='summary_correct_answers')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.FloatField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    # Couln't Identify what was meant by category in the dataset
    year_level_name = models.CharField(max_length=1)
    question_no = models.IntegerField(default=None)



    
