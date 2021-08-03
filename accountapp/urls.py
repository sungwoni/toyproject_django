from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'  #앞으로 함수호출할 때 더 간단해지니까 해보기

urlpatterns=[
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create'),
]