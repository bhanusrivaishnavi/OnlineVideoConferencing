from django.contrib import admin
from django.urls import path,include
from videoapp import views
from django.contrib.auth import views as v
from videoapp.views import *
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf.urls.static import static
urlpatterns = [
  path('admin1/', admin.site.urls),
  path('sample/',views.sample),
  path('',views.home,name='home'),
  path('about/',views.about,name='about'),
  path('contact/',views.contact,name='contact'),
  path('register/',views.register,name='register'),
  path('login/',v.LoginView.as_view(template_name='videoapp/login.html'),name='login'),
  path('logout/',v.LogoutView.as_view(template_name='videoapp/logout.html'),name='logout'),
  path('dashboard/',views.dashboard,name='dashboard'),
  path('discuss/',views.discuss,name='discuss'),
  path('profile/',views.profile,name='profile'),
  path('update/',views.update,name='update'),
  path('display/',views.display,name='display'),
  path('studentjoin/',views.studentjoin,name='studentjoin'),
  path('teacherjoin/',views.teacherjoin,name='teacherjoin'),
  path('forumhome/',views.forumhome,name='forumhome'),
  path('addInForum/',views.addInForum,name='addInForum'),
 path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
 path('uploaddoc/',views.simple_upload,name='uploaddoc'),
 path('displayfiles/',views.display_files,name='displayfiles'),
 path('delete/',views.delete,name='delete'),
 url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
