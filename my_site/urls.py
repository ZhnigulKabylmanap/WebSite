from django.urls import path
from . import views

from project1.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('About us',views.about,name='about'),
    path('hi', views.hi, name='hi'),
    path('art', views.art, name='art'),

    path('intro', views.intro, name='intro'),
    path('movie', views.movie, name='movie'),
    path('test', views.test, name='test'),

    path('index', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),

    path('addpage/', views.addpage, name='addpage'),
    path('send/', views.send_message, name='send'),




]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)












