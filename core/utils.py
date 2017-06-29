from pure_pagination import Paginator, PageNotAnInteger


def pagination(request, object_list, num_per_page=7):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    _pagination = Paginator(object_list, per_page=num_per_page, request=request)
    object = _pagination.page(page)
    return object
