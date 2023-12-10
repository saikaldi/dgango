from django.urls import path
from post import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('products/create/', views.product_create),
    path('products/<int:product_id>/', views.product_detail_view),

    path('categories/', views.category_view),
    path('categories/create/', views.category_create),
    path('reviews/', views.review_view),
    path('reviews/review/', views.reviews),
    
]