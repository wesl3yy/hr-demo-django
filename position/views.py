from django.views import View
from django.http import JsonResponse

from position.forms import PositionSearchForm
from position.serializers import PositionSerializer
from position.services import PositionService
from utils import filter_allowed_fields, paginate
from utils.rate_limiter import rate_limit


# Create your views here.
class PositionViews(View):
    @filter_allowed_fields("position")
    def serialize(self, results):
        return [PositionSerializer(org).to_dict() for org in results]

    @rate_limit(max_requests=10, window_seconds=60)
    def get(self, request, *args, **kwargs):
        form = PositionSearchForm(request.GET)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        data = form.cleaned_data
        keyword = data.get("keyword")
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        qs = PositionService.search_position(keyword)

        paginated, total, page, page_size = paginate(qs, page, page_size)

        data = self.serialize(paginated)

        return JsonResponse({
            "total": total,
            "page": page,
            "page_size": page_size,
            "results": data
        })