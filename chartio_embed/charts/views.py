# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from .models import Chart

class ChartDetailView(LoginRequiredMixin, DetailView):

    model = Chart

    slug_field = "title"
    slug_url_kwarg = "title"

    def get_context_data(self, **kwargs):
        context = super(ChartDetailView, self).get_context_data(**kwargs)

        # Add jwt with single title to context here.
        return context

class ChartListView(LoginRequiredMixin, ListView):
    model = Chart

    def get_context_data(self, **kwargs):
        context = super(ChartListView, self).get_context_data(**kwargs)

        # Add jwt with all titles to context here.
        return context
