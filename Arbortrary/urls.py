from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('new/tree', views.add_new_tree),
    path('create_tree', views.create_tree),
    path('show/<int:tree_id>', views.read_tree_details),
    path('user/account/', views.user_trees),
    path('delete/<int:tree_id>', views.delete_tree),
    path('edit/<int:tree_id>', views.edit_tree),
    path('update/<int:tree_id>', views.update_tree),

]
