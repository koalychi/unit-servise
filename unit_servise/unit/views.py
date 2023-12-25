from django.http import HttpResponse


def get_unit(request):
    return HttpResponse("get_unit")


def get_unit_by_id(request):
    return HttpResponse("get_unit_by_id")


def create_unit(request):
    return HttpResponse("create_unit")


def edit_unit(request):
    return HttpResponse("edit_unit")


def choose_executor(request):
    return HttpResponse("choose_executor")


def execute_unit(request):
    return HttpResponse("execute_unit")


def get_comments(request):
    return HttpResponse("get_comments")


def get_responses(request):
    return HttpResponse("get_responses")


def get_comments_by_id(request):
    return HttpResponse("get_comments_by_id")


def get_responses_by_id(request):
    return HttpResponse("get_responses_by_id")


def create_comments(request):
    return HttpResponse("create_comments")


def create_responses(request):
    return HttpResponse("create_responses")


def download_file(request):
    return HttpResponse("download_file")