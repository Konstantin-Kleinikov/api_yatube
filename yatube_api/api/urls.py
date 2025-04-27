from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(
    'posts',
    PostViewSet,
    basename='posts',
)
router_v1.register(
    'groups',
    GroupViewSet,
    basename='groups',
)

# urlpatterns = [
#     path('v1/api-token-auth/', views.obtain_auth_token),
#     path('v1/', include(router_v1.urls)),
# ]
urlpatterns_v1 = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]