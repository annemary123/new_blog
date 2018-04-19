from django.urls import path
from . import views

urlpatterns=[
path('',views.index),
path('register/',views.regist),
path('login/vblog/blogid=<int:pk>', views.editBlog,name='editblog'),
path('editblog/',views.update,name='update'),
path('login/',views.login),
path('login/rp/',views.rstpwd),
path('login/blog/',views.cblog),
path('logout/',views.logout),
path('login/vblog/',views.viewBlog),
path('login/vablog/',views.viewallblogs)
]




