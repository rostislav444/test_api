from rest_framework import routers

from . import views

app_name = 'portfolio'

router = routers.SimpleRouter()

router.register('photo', views.PhotoView, basename='photo')
router.register('comment', views.CommentsView, basename='comment')
router.register('', views.PortfolioView, basename='portfolio')

urlpatterns = [] + router.urls
