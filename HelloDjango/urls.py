from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    #url(r'^$', view.hello),
    url(r'^$', view.my_view),
    url(r'^test1', view.test1,name='test1'),
]
