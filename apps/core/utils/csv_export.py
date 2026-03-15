"""The pieces shared by every CSV export in core.utils -- writing a
list of dict rows out as CSV text, in the column order each export's
own FIELDNAMES gives, and wrapping that text as a downloadable
response for the admin's own "Export selected to CSV" actions.

See core.utils.location_export, core.utils.project_export, and
core.utils.rule_export for the exports themselves -- each the mirror
of its own core.utils.*_import module, writing the same columns that
import reads back, identifying its own record the same way import
does (never by internal primary key -- see each export's own
docstring for its identifying fields).
"""

import csv
import io

from django.http import HttpResponse


def write_csv(fieldnames: list[str], rows: list[dict]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def csv_download_response(csv_text: str, filename: str) -> HttpResponse:
    response = HttpResponse(csv_text, content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
