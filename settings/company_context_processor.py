from .models import Company


def get_company_data(request):
    data = Company.objects.last()   # firmen data 
    return({'company_data':data})