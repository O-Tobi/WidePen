from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("publish", views.publish, name="publish"),
    path("publish_edit/<int:post_id>/", views.publish_edit, name="publish_edit"),
    path("post_read/<int:post_id>/", views.post_read, name="post_read"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("edit_profile/<int:user_id>/", views.edit_profile, name="edit_profile"),
    path("category/<str:category_name>/", views.category, name="category"),
    path("add_to_bookmark/<int:post_id>", views.add_to_bookmark, name="add_to_bookmark"),
    path("remove_from_bookmark/<int:post_id>", views.remove_from_bookmark, name="remove_from_bookmark"),
    path("view_bookmark", views.view_bookmark, name="view_bookmark"),
    path("post_delete/<int:post_id>/", views.post_delete, name="post_delete"),
    path("search_post", views.search_post, name="search_post"),
    #path("staff_pick", views.staff_pick, name="staff_pick")

]
