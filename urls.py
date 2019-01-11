from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.article_total_count, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
