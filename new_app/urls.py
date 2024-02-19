from django.conf.urls.static import static
from django.urls import path

from finalEvaluationProject import settings
from new_app import views

urlpatterns = [
    path('', views.base, name ="base"),
    path('login1', views.login_view, name="login1"),
    path('adminReg', views.admin_register, name="adminReg"),
    path('studentReg', views.student_register, name="studentReg"),
    path('adminLogin', views.admin_login, name="adminLogin"),
    path('studentLogin', views.student_login, name="studentLogin"),
    path('viewStudList', views.viewStudentList, name='viewStudList'),
    path('viewInfo', views.viewInfo, name='viewInfo'),
    path('updateInfo/<int:id>/', views.updateInfo, name='updateInfo'),
    path('addMarks', views.add_marks, name="addMarks"),
    path('viewMarks', views.viewMarksbyAdmin, name="viewMarks"),
    path('updateMarks/<int:id>/', views.updateMarks, name="updateMarks"),


    path('studentDetails', views.studentDetails, name='studentDetails'),
    path('stddetail/<int:id>/', views.student_detail, name='student_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)