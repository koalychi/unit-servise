from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_unit, name="get_unit"),
    path("<UserId>/", views.get_unit_by_id, name="get_unit_by_id"),
    path("create/", views.create_unit, name="create_unit"),
    path("edit_unit/<UserId>/", views.edit_unit, name="edit_unit"),
    path("choose_executor/<UnitId>/", views.choose_executor, name="choose_executor"),
    path("execute_unit/<UnitId>/", views.execute_unit, name="execute_unit"),
    path("<UnitId>/comments/", views.get_comments, name="get_comments"),
    path("<UnitId>/response/", views.get_responses, name="get_responses"),
    path("<UnitId>/comments/<CommentId>/", views.get_comments_by_id, name="get_comments_by_id"),
    path("<UnitId>/response/<ResponseId>/", views.get_responses_by_id, name="get_responses_by_id"),
    path("<UnitId>/createComments/", views.create_comments, name="create_comments"),
    path("<UnitId>/createResponse/", views.create_responses, name="create_responses"),
    path("downloadfile/<UnitId>/<filename>", views.download_file, name="download_file"),
]