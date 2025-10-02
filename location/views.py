from django.views import View
from django.http import JsonResponse

from location.forms import LocationSearchForm
from location.serializers import LocationSerializer
from location.services import LocationService
from utils import filter_allowed_fields, paginate
from utils.rate_limiter import rate_limit


# Create your views here.
class LocationViews(View):
    @filter_allowed_fields("location")
    def serialize(self, results):
        return [LocationSerializer(loc).to_dict() for loc in results]

    @rate_limit(max_requests=10, window_seconds=60)
    def get(self, request, *args, **kwargs):
        form = LocationSearchForm(request.GET)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        data = form.cleaned_data
        keyword = data.get("keyword")
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        qs = LocationService.search_location(keyword)

        paginated, total, page, page_size = paginate(qs, page, page_size)

        data = self.serialize(paginated)

        return JsonResponse({
            "total": total,
            "page": page,
            "page_size": page_size,
            "results": data
        })
