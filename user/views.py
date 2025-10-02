from django.views import View
from django.http import JsonResponse

from user.forms import EmployeeSearchForm
from user.serializers import UserSerializer
from user.services import UserService
from utils import filter_allowed_fields, paginate
from utils.rate_limiter import rate_limit


# Create your views here.
class UserSearchView(View):
    @filter_allowed_fields('user')
    def serialize(self, results):
        return [UserSerializer(org).to_dict() for org in results]

    @rate_limit(max_requests=10, window_seconds=60)
    def get(self, request, *args, **kwargs):
        form = EmployeeSearchForm(query_dict=request.GET)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        data = form.cleaned_data
        keyword = data.get("keyword").strip()
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        location_ids = data["location_ids"]
        organization_ids = data["organization_ids"]
        department_ids = data["department_ids"]
        position_ids = data["position_ids"]

        qs = UserService.search(
            keyword=keyword,
            locations_ids=location_ids or None,
            organization_ids=organization_ids or None,
            department_ids=department_ids or None,
            position_ids=position_ids or None
        )

        paginated, total, page, page_size = paginate(qs, page, page_size)

        data = self.serialize(paginated)

        return JsonResponse({
            "total": total,
            "page": page,
            "page_size": page_size,
            "results": data
        })
