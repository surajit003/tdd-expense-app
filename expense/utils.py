from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def render_to_pdf(template_src, context_dict={}):
    log_prefix = "RENDER TO PDF"
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    else:
        logger.error(u"{} {}".format(log_prefix, str(pdf.err)))
        return None
