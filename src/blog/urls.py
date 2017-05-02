from django.conf.urls import url
from .views import PostDetail,archives, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^archives/$', archives, name='archives'),
    # url(r'^post/$', post_page_view, name='detail'),
    url(r'^post/(?P<pk>\d+)/$', PostDetail, name='PostDetail'),
    # url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post'),
    url(r'^post/create/$',PostCreate.as_view(), name='create'),
    url(r'^post/(?P<pk>\d+)/update/$',PostUpdate.as_view(), name='update'),
    url(r'^post/(?P<pk>\d+)/delete/$',PostDelete.as_view(), name='delete'),
]
