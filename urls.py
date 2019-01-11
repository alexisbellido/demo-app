from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.article_total_count, name='index'),
    path('add-tv-program', views.add_tv_program, name='add_tv_program'),
    path('<int:question_id>/', views.detail, name='detail'),
]
