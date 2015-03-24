# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

class ChartDetailView(LoginRequiredMixin, DetailView):

    # def get_template_names(self):
    #     ['Chart_detail.html']

    def get_queryset(self):
        []

    def get_context_data(self, **kwargs):
        context = super(ChartDetailView, self).get_context_data(**kwargs)
        context['data'] = 'details'
        return context

class ChartListView(LoginRequiredMixin, ListView):

    # def get_template_names(self):
    #     ['Chart_list']

    def get_queryset(self):
        []

    def get_context_data(self, **kwargs):
        context = super(ChartListView, self).get_context_data(**kwargs)
        context['data'] = 'list'
        return context
