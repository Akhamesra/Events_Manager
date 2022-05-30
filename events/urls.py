from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='all-events'), # our-domain.com/events
  path('<slug:event_slug>/success', views.confirm_registration, name='confirm-registration'),
  path('<slug:event_slug>', views.event_details, name='event-detail'), # our-domain.com/events/<dynamic-path-segment>
]