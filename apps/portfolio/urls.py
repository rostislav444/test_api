from rest_framework import routers

from . import views

app_name = 'portfolio'

router = routers.SimpleRouter()

router.register('photos', views.PhotosView, basename='photos')
router.register('comments', views.CommentsView, basename='comments')
router.register('', views.PortfolioView, basename='portfolio')

urlpatterns = [] + router.urls
