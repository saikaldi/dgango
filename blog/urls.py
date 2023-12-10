from django.contrib import admin
from django.urls import path, include
from post import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('users/', include('users.urls'))
    # path('', views.main_view),
    # path('products/', views.products_view),
    # path('products/create/', views.product_create),
    # path('products/<int:product_id>/', views.product_detail_view),

    # path('categories/', views.category_view),
    # path('categories/create/', views.category_create),
    # path('reviews/', views.review_view),
    # path('reviews/review/', views.reviews),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
