from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.article_total_count, name='index'),
    path('add-tv-program', views.add_tv_program, name='add_tv_program'),
    path('tv-program-added', views.tv_program_added, name='tv_program_added'),
    path('<int:tv_program_id>/', views.detail, name='tv_program_detail'),
]
