from django.http import HttpResponse
from App_TestModel.models import Test

def testdb(request):
    response = ""
    response1 = ""

    result_all = Test.objects.all()  # return datatype QuerySet
    response += "<p>1.Test.objects.all()</p>"
    for var in result_all:
        response += "<p>"+var.name+"</p><br/>"

    response2 = Test.objects.filter(id=1)  # return datatype QuerySet
    response += "<p>2.Test.objects.filter(id=1)</p>"
    for var in response2:
        response += "<p>"+var.name+"</p><br/>"

    response3 = Test.objects.get(id=1)  # return a data
    response += "<p>3.Test.objects.get(id=1)</p>"
    response += "<p>"+response3.name+"</p><br/>"

    response4 = Test.objects.order_by("id")  # return QuerySet
    response += "<p>4.Test.objects.order_by('id')</p>"
    for var in response4:
        response += "<p>"+var.name+"</p><br/>"

    response5 = Test.objects.order_by('name')[0:2]  # return QuerySet
    response += "<p>5.Test.objects.order_by('name')[0:2]</p>"
    for var in response5:
        response += "<p>"+var.name+"</p><br/>"

    response6 = Test.objects.filter(name="runoob").order_by('id')  # return QuerySet
    response += "<p>6.Test.objects.filter(name='runoob').order_by('id')</p>"
    for var in response6:
        response += "<p>"+var.name+"</p><br/>"

    responseu = Test.objects.get(id=2)  # return a data
    response += "<p>before update</p>"
    response += "<p>"+responseu.name+"</p><br/>"
    responseu.name = "Baidu"
    responseu.save()
    testu = Test.objects.get(id=2)  # return a data
    response += "<p>after update</p>"
    response += "<p>"+testu.name+"</p><br/>"

    return HttpResponse(response)