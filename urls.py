from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.article_total_count, name='index'),
    path('add-tv-program', views.add_tv_program, name='add-tv-program'),
    path('<int:tv_program_id>/', views.detail, name='tv-program-detail'),
]
