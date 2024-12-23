from django.urls import path

from apps.pizza.views import PizzaListCreateView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaListCreateView.as_view()),
    path('<int:pk>', PizzaRetrieveUpdateDestroyView.as_view()),
]
