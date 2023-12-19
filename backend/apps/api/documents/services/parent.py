import io
import xlsxwriter
from django.views import View
from django.http import HttpResponse


class XLSXView(View):
    """
    Базовый класс для xlsx
    """

    file_name = "file.xlsx"

    def get(self, request, *args, **kwargs):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        self.create_file(
            self.get_context_data(**kwargs), workbook, worksheet, **kwargs,
        )

        workbook.close()
        output.seek(0)

        filename = self.get_file_name(**kwargs)
        response = HttpResponse(
            output,
            content_type=(
                "application/vnd.openxmlformats"
                "-officedocument.spreadsheetml.sheet"
            ),
        )
        response["Content-Disposition"] = "attachment; filename=%s" % filename

        return response

    def get_file_name(self, **kwargs):
        return self.file_name

    def get_context_data(self, **kwargs):
        return {}

    def create_file(self, context, workbook, worksheet, **kwargs):
        pass
