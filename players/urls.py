from django.urls import path
from .views import AgentInteraction

urlpatterns = [
    path('agent-action', AgentInteraction.as_view(), name='agent-action'),
]
