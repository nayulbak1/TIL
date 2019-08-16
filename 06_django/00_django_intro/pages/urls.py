from django.urls import path
from . import views

urlpatterns = [
    # 원래 app url은 아래로 작성
    path('throw/', views.throw),
    path('isitgwangbok/', views.isitgwangbok),
    path('template_language/', views.template_language,),
    path('area/<int:r>/', views.area),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('hello/<str:name>/', views.hello),
    path('dinner/', views.dinner),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('index/', views.index),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
    path('image/', views.image),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('catch/', views.catch),
]