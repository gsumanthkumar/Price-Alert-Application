from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('alerts/all_alerts/',views.ListAllAlerts.as_view(),name='listallalerts'),
    path('alerts/deleted_alerts/',views.DeletedAlerts.as_view(),name='deletedalerts'),
    path('alerts/created_alerts/',views.CreatedAlerts.as_view(),name='createdalerts'),
    path('alerts/triggered_alerts/',views.TriggeredAlerts.as_view(),name='triggeredalerts'),
    path('alerts/applyalerts/',views.apply_alert_view,name='applyalerts'),
    path('alerts/create/',views.CreateAlerts.as_view(),name='createalerts'),
    path('alerts/<int:pk>/',views.RetrieveAlert.as_view(),name='retrievealert'),
    path('alerts/<int:pk>/delete/',views.UpdateAlert.as_view(),name='deletealert'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
]