from django.views import View
from django.http import JsonResponse

from organization.forms import OrganizationSearchForm
from utils.rate_limiter import rate_limit
from organization.services import OrganizationService
from organization.serializers import OrganizationSerializer
from utils import filter_allowed_fields, paginate


class OrganizationSearchView(View):
    @filter_allowed_fields('organization')
    def serialize(self, results):
        return [OrganizationSerializer(org).to_dict() for org in results]

    @rate_limit(max_requests=10, window_seconds=60)
    def get(self, request, *args, **kwargs):
        form = OrganizationSearchForm(request.GET)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        data = form.cleaned_data
        keyword = data.get("keyword")
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        qs = OrganizationService.search_organizations(keyword)

        paginated, total, page, page_size = paginate(qs, page, page_size)

        data = self.serialize(paginated)

        return JsonResponse({
            "total": total,
            "page": page,
            "page_size": page_size,
            "results": data
        })
