# from django.shortcuts import render
#
# from kandy.models import Application
#
# from django.http import HttpResponse
#
# from django.template.loader import get_template
#
# from xhtml2pdf import pisa

# def showcareers(request):
#     return render(request, 'pdf-report.html')


# def show_careers(request):
#     application = Application.objects.all()
#
#     return render(request, 'pdf_convert.html', context={'application': application})
#
# def pdf_report_create(request):
#     application = Application.objects.all()
#
#     template_path = '../templates/pdf_report.html'
#
#     context = {'application': application}
#
#     response = HttpResponse(content_type='application/pdf')
#     # load: attachment;
#     response['Content-Disposition'] = 'filename="application_report.pdf"'
#
#     template = get_template(template_path)
#
#     html = template.render(context)
#
#
#     pisa_status = pisa.CreatePDF(
#         html, dest=response)
#     # if error then show some funny view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

