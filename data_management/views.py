from django.shortcuts import render,redirect
from django.views.generic import View

from .models import School,AssesmentArea,Answer,Award,SchoolClass,Student,Subject,Summary
import csv


def handle_uploaded_file(csv_file):
    
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    row_count = 0
    for row in reader:
        print(f"{row_count}")
        if row_count == 0:
            row_count += 1
            pass
        else:
            school = row[0]
            student_id = row[2]
            student_first_name =row[3]
            student_last_name =row[4]
            class_name = row[6]
            assesment_area_name = row[12]
            answer = row[8]
            correct_answer = row[9]
            award_name = row[30]
            subject=row[7]
            sydney_participant = row[15]
            sydney_percentile = row[24]
            question_no = row[10]
            correct_answer_percentage_per_class = row[21]
            participant = row[29]
            student_score =  row[16]
            year_level_name = row[5]

            # Handling Schools
            school_exists = School.objects.filter(school_name=school).exists()
            if not school_exists:
                school_obj = School(school_name=school)
                school_obj.save()
            else:
                school_obj = School.objects.get(school_name=school)

            # Handling Students
            student_exists = Student.objects.filter(student_id=student_id).exists()
            if not student_exists:
                student_obj = Student(student_id=student_id,full_name = student_first_name + "" + student_last_name)
                student_obj.save()
            else:
                student_obj = Student.objects.get(student_id=student_id)
            
            # Handling Classes
            class_exists = SchoolClass.objects.filter(class_name=class_name).exists()
            if not class_exists:
                class_obj = SchoolClass(class_name=class_name)
                class_obj.save()
            else:
                class_obj = SchoolClass.objects.get(class_name=class_name)

            # Handling Assesment Areas
            assesment_area_exists = AssesmentArea.objects.filter(assesment_area_name=assesment_area_name).exists()
            if not assesment_area_exists:
                assesment_area_obj = AssesmentArea(assesment_area_name=assesment_area_name)
                assesment_area_obj.save()
            else:
                assesment_area_obj = AssesmentArea.objects.get(assesment_area_name=assesment_area_name)
            
            # Handling Answers
            answer_exists = Answer.objects.filter(answeres=correct_answer).exists()
            if not answer_exists:
                answer_obj = Answer(answeres=correct_answer)
                answer_obj.save()
            else:
                answer_obj = Answer.objects.get(answeres=correct_answer)

            # Handling Awards
            award_exists = Award.objects.filter(award_name=award_name).exists()
            if not award_exists:
                award_obj = Award(award_name=award_name)
                award_obj.save()
            else:
                award_obj = Award.objects.get(award_name=award_name)

            # Handling Subjects
            subject_exists = Subject.objects.filter(subject=subject).exists()
            if not subject_exists:
                subject_obj = Subject(subject=subject)
                subject_obj.save()
            else:
                subject_obj = Subject.objects.get(subject=subject)


            # Handeling Sumamry
            summary_exists = Summary.objects.filter(school=school_obj,student=student_obj,school_class=class_obj,subject=subject_obj,assesment_area=assesment_area_obj,question_no=question_no)
            if not summary_exists:
                summary = Summary(school=school_obj,
                                  student=student_obj,
                                  school_class=class_obj,
                                  subject=subject_obj,
                                  sydney_participant=sydney_participant,
                                  sydney_percentile=sydney_percentile,question_no=question_no,
                                  assesment_area=assesment_area_obj,
                                  award =award_obj,
                                  correct_answer_percentage_per_class=correct_answer_percentage_per_class,
                                  answer= Answer.objects.get(answeres =answer) ,
                                  correct_answer= Answer.objects.get(answeres=correct_answer) ,
                                  participant= participant ,
                                  year_level_name= year_level_name ,
                                  student_score=  student_score,
                                  )
                summary.save()
        row_count += 1
        
        # if row_count >= 5:
        #     break

class DataManagementMain(View):
    def get(sefl,request):
        return render(request,'data_management.html')
    
    def post(self,request):
        csv_file = request.FILES['csv_file']
        handle_uploaded_file(csv_file)
        return redirect('data_management_main_view')