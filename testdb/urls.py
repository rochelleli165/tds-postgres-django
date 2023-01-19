from django.urls import re_path
from testdb import views

urlpatterns = [
    re_path(r'^api.testdb$', views.teacher_list),
    re_path(r'^api/testdb/(?P<pk>[0-9]+)$', views.teacher_detail),
    re_path(r'^api/testdb/published$', views.teacher_list_published)
]