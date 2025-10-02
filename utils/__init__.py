from functools import wraps

from organization.models import Organization


def filter_allowed_fields(entity_name):
    """
    Filter serialized dicts based on Organization config for a given entity.
    Expects each item to have 'organization_id' (string).
    Efficiently fetches all orgs in one query.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)

            org_ids = {item.get("organization_id") for item in data if item.get("organization_id")}
            org_map = {str(org.id): org for org in Organization.objects.filter(id__in=org_ids)}

            filtered_data = []
            for item in data:
                org_id = item.get("organization_id")
                org = org_map.get(org_id)
                if org and hasattr(org, "config"):
                    allowed = org.config.get("allowed_fields").get(entity_name)
                    if allowed:
                        item = {k: v for k, v in item.items() if k in allowed}
                filtered_data.append(item)

            return filtered_data

        return wrapper

    return decorator

def paginate(queryset, page: int = 1, page_size: int = 10):
    total = len(queryset)
    start = (page - 1) * page_size
    end = start + page_size
    return queryset[start:end], total, page, page_size

