from rest_framework import response


def echo(request):
    if request.method.lower() == "get":
        data = request.GET.dict()
    else:
        data = request.data
    return response.Response(data=data)
