from django import forms

class EmployeeSearchForm(forms.Form):
    keyword = forms.CharField(max_length=200, required=True)
    page = forms.IntegerField(min_value=1, required=False, initial=1)
    page_size = forms.IntegerField(min_value=1, max_value=100, required=False, initial=10)

    location_ids = forms.CharField(required=False)
    organization_ids = forms.CharField(required=False)
    department_ids = forms.CharField(required=False)
    position_ids = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        query_dict = kwargs.pop("query_dict", None)
        if query_dict:
            data = query_dict.copy()
            for field in ["location_ids", "organization_ids", "department_ids", "position_ids"]:
                data[field] = ",".join(query_dict.getlist(field))
            kwargs["data"] = data
        super().__init__(*args, **kwargs)
