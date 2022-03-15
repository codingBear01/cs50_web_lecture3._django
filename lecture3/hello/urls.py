from django.urls import path

from . import views

urlpatterns = [
    # first arg: end of the route
    # second arg: what should be rendered when this URL is visited
    # third arg(optional): give a name to a particular URL pattern to make it easy to reference it from other parts of the app
    path("", views.index, name="index"),
    # hello/{name} 주소에 입력한 {name}이 Hello, {name} 형식으로 표기됨.
    path("<str:name>", views.greet, name="greet"),
    path("kang", views.kang, name="kang"),
    path("han", views.han, name="han")
]
