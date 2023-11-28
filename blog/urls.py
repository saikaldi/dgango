
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello_view),
    # path('current_date/', views.current_date_view ),
    # path('goodbye/', views.goodbye_view ),
    # path('goodmorning/', views.goodmorning_view )
    path('', views.main_view),
    path('products/', views.products_view),
    path('products/<int:product_id>/', views.review_view),
    path('categories/', views.category_view)
]
