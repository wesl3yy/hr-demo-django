from django.views import View
from django.http import JsonResponse

from department.forms import DepartmentSearchForm
from department.serializers import DepartmentSerializer
from department.services import DepartmentService
from utils import filter_allowed_fields, paginate
from utils.rate_limiter import rate_limit


# Create your views here.
class DepartmentViews(View):
    @filter_allowed_fields("department")
    def serialize(self, results):
        return [DepartmentSerializer(department).to_dict() for department in results]

    @rate_limit(max_requests=10, window_seconds=60)
    def get(self, request, *args, **kwargs):
        form = DepartmentSearchForm(request.GET)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        data = form.cleaned_data
        keyword = data.get("keyword")
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        qs = DepartmentService.search_departments(keyword)

        paginated, total, page, page_size = paginate(qs, page, page_size)

        serialized_data = self.serialize(paginated)

        return JsonResponse({
            "total": total,
            "page": page,
            "page_size": page_size,
            "results": serialized_data
        })
