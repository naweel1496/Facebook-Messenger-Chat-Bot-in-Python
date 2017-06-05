from django.conf.urls import url, include
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^<your random url?$', YoMamaBotView.as_view())
               ]