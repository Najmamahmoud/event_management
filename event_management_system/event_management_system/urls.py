
from django.contrib import admin
from django.urls import path, include
from events import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.list_events, name='list_events'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),  # Add this line
    path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URLs
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('profile/', views.user_profile, name='user_profile'),
]
