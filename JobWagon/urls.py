from django.urls import path # type: ignore
from django.urls import path
from .views import view_booking, update_booking_status

from . import views

urlpatterns =[

  path('',views.home_page,name='home'),
  path('login_page/',views.login_page,name='login_page'),
  path('register_page/',views.register_page,name='register_page'),
  path('logout_page/',views.logout_page,name='logout_page'),
  path('booking/',views.booking_view,name='booking'),
  path('test/',views.test,name='test'),
  path('view_bookings/',views.view_booking,name='view_booking'),
  path('update_status/<int:booking_id>/', views.update_booking_status, name='update_status'),
  path('success/',views.success,name='success'),
  path('partner/',views.partner_home,name='partner_home'),
  path('partner_login/',views.partner_login,name='partner_login'),
  path('partnermain/',views.partner_main,name='partner_main'),
  path('partner/work/', views.partner_work_list, name='partner_work_list'),
  path('partner/update_status/<int:booking_id>/', views.update_partner_status, name='update_partner_status'),
  path('index/',views.index,name='index'),
  path('partner_message/',views.partner_message),

  
]