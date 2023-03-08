from django.conf.urls import url

from apps.notebooks.views import (
    ListNotebooks,
    RetrieveNotebook,
    RetrieveNotebookWithSlug,
    GetNbIframes,
)

notebooks_urlpatterns = [
    url(
        "api/v1/(?P<site_id>.+)/notebooks/(?P<notebook_id>.+)",
        RetrieveNotebook.as_view(),
    ),
    url(
        "api/v1/(?P<site_id>.+)/getnb/(?P<notebook_slug>.+)",
        RetrieveNotebookWithSlug.as_view(),
    ),
    url("api/v1/(?P<site_id>.+)/notebooks", ListNotebooks.as_view()),
    url("api/v1/(?P<site_id>.+)/nb-iframes", GetNbIframes.as_view()),
]
