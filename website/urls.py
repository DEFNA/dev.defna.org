from django.urls import path

from website import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("events/djangocon/", views.DjangoConView.as_view(), name="djangocon"),
    path("events/sponsored/", views.SponsoredEventsView.as_view(), name="sponsored-events"),
    path("donate/", views.DonateView.as_view(), name="donate"),
    path("grants/", views.GrantsView.as_view(), name="grants"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
