from django.views.generic import ListView, TemplateView

from website.models import Announcement, BoardMember, DjangoConEdition, GrantCycle, SponsoredEvent


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["announcements"] = Announcement.objects.all()[:4]
        ctx["featured"] = Announcement.objects.filter(is_featured=True).first()
        return ctx


BOARD_PLACEHOLDER_ROLES = [
    "President",
    "Vice President",
    "Secretary",
    "Treasurer",
    "Director",
    "Director",
    "Director",
    "Director",
    "Director",
]


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["board"] = BoardMember.objects.filter(is_current=True)
        ctx["alumni"] = BoardMember.objects.filter(is_current=False)
        ctx["board_placeholder_roles"] = BOARD_PLACEHOLDER_ROLES
        return ctx


class DjangoConView(ListView):
    template_name = "events/djangocon.html"
    context_object_name = "editions"
    queryset = DjangoConEdition.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["upcoming"] = DjangoConEdition.objects.filter(status=DjangoConEdition.Status.UPCOMING).first()
        return ctx


class SponsoredEventsView(ListView):
    template_name = "events/sponsored.html"
    context_object_name = "events"
    queryset = SponsoredEvent.objects.filter(is_published=True)


class DonateView(TemplateView):
    template_name = "donate.html"


GRANT_ELIGIBILITY = [
    "The event must be Django-related (meetup, workshop, conference, or sprint).",
    "Events of all sizes are welcome — from small local meetups to regional conferences.",
    "Grant funds must be used for event costs.",
]


class GrantsView(TemplateView):
    template_name = "grants.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cycle"] = GrantCycle.objects.order_by("-id").first()
        ctx["eligibility_items"] = GRANT_ELIGIBILITY
        return ctx


class ContactView(TemplateView):
    template_name = "contact.html"
