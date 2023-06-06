# views
import zeep
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/object-list',
        'Detail': '/object-detail/<str:pk>',
    }


# List
@api_view(['GET'])
def the_list_of_customers(request):
    all_client = client.objects.all()
    data = ClientSerializer(all_client, many=True).data
    return Response( data)


@api_view(['GET'])
def the_list_of_services(request):
    all_services = service.objects.all()
    data = ServiceSerializer(all_services, many=True).data
    return Response( data)


@api_view(['GET'])
def the_list_of_offers(request):
    all_offres = offre.objects.all()
    data = OffreSerializer(all_offres, many=True).data
    return Response(data)


@api_view(['GET'])
def the_list_of_contracts(request):
    all_contracts = contrat.objects.all()
    data = ContratSerializer(all_contracts, many=True).data
    return Response( data)


@api_view(['GET'])
def the_list_of_bills(request):
    all_bills = facture.objects.all()
    data = FactureSerializer(all_bills, many=True).data
    return Response( data)


# Detail
@api_view(['GET'])
def the_details_about_a_customer(request, pk):
    try:
        a_client = client.objects.get(client_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = ClientSerializer(a_client, many=False).data
    return Response( data)


@api_view(['GET'])
def the_details_about_a_service(request, pk):
    try:
        a_service = service.objects.get(service_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = ServiceSerializer(a_service, many=False).data
    return Response( data )


@api_view(['GET'])
def the_details_about_an_offer(request, pk):
    try:
        an_offer = offre.objects.get(offre_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = OffreSerializer(an_offer, many=False).data
    return Response(data)


@api_view(['GET'])
def the_details_about_a_contract(request, pk):
    try:
        a_contract = contrat.objects.get(contrat_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = ContratSerializer(a_contract, many=False).data
    return Response(data)


@api_view(['GET'])
def the_details_about_a_bill(request, pk):
    try:
        a_bill = facture.objects.get(facture_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = FactureSerializer(a_bill, many=False).data
    return Response(data)


# list contract by customer


@api_view(['GET'])
def the_list_of_contracts_for_a_given_customer(request, pk):
    try:
        a_contract = contrat.objects.filter(client_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = ContratSerializer(a_contract, many=True).data
    return Response(data)


# list bills by customer


@api_view(['GET'])
def the_list_of_bills_for_a_given_customer(request, pk):
    try:
        a_bill = facture.objects.filter(client_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = FactureSerializer(a_bill, many=True).data
    return Response(data)


# somme
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
operations = zeep.Client(wsdl=wsdl)

# somme d'une facture donnée par leur id
@api_view(['PUT',])  # PUT
def the_amount_to_be_paid_for_a_bill(request, pk):
    somme_total = 0
    try:
        a_bill = facture.objects.get(facture_id=pk)

    except:
        return Response('NOT FOUND    check the id ! ')
    bill_data = FactureSerializer(a_bill, many=False).data
    Client_ID = bill_data['client_id']
    try:
        contracts = contrat.objects.filter(client_id=Client_ID)
    except:
        return Response('NOT FOUND    check the id ! ')
    contrat_data = ContratSerializer(contracts, many=True).data

    for elt in contrat_data:
        elements = list(elt.items())
        OFFRE_ID = elements[2][1]
        try:
            offers = offre.objects.get(offre_id=OFFRE_ID)
        except:
            return Response('NOT FOUND    check the id ! ')
        offre_data = OffreSerializer(offers, many=False).data
        #        print(offre_data)
        offre_data = list(offre_data.items())
        offer_parents = offre_data[1][1]
        offers = offre.objects.filter(offre_parent=offer_parents)
        offre_data = OffreSerializer(offers, many=True).data
        for elt in offre_data:
            elts = list(elt.items())
            Serice_ID = elts[2][1]
            SERVICE = service.objects.get(service_id=Serice_ID)
            SERVICIE_data = ServiceSerializer(SERVICE, many=False).data
            print(SERVICIE_data)
            if (SERVICIE_data["designation"] == 'SMS'):
                somme_sms = operations.service.Multiply(SERVICIE_data["prix_unite"], bill_data['consom_sms'])
                somme_total = operations.service.Add(somme_total, somme_sms)
            elif (SERVICIE_data["designation"] == 'Appel'):
                somme_appel = operations.service.Multiply(SERVICIE_data["prix_unite"], bill_data['consom_appel'])
                somme_total = operations.service.Add(somme_total, somme_appel)
            elif (SERVICIE_data["designation"] == 'Internet'):
                somme_internet = operations.service.Multiply(SERVICIE_data["prix_unite"], bill_data['consom_internet'])
                somme_total = operations.service.Add(somme_total, somme_internet)
    print(somme_total)
    facture_object = facture.objects.get()
    bill_data["somme_tot"] = somme_total   
    facture_object.somme_tot = bill_data["somme_tot"] 
    facture_object.save()
    serializer = FactureSerializer(facture_object)
    return Response(serializer.data)


# facture Payé ou non
@api_view(['PUT'])
def bill_paid(request, pk):
    try:
        a_bill = facture.objects.get(facture_id=pk)
    except:
        return Response('NOT FOUND    check the id ! ')
    data = FactureSerializer(a_bill, many=False).data
    check =data['paid']
    facture_object = facture.objects.get()
    data["paid"] = 1   
    facture_object.paid = data["paid"] 
    facture_object.save()
    serializer = FactureSerializer(facture_object)
    return Response(serializer.data)


# Check User 
@api_view(['POST'])
def check_user(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    user_serializer = user_serializer
    if user_serializer.is_valid():
        return Response( {"login": False, "userName": False , "password" :False })
    pk1 =user_serializer.data["userName"]
    pk =user_serializer.data["password"]
    try:
            a_user = User.objects.get(userName=pk1,password=pk)
    except:
            return Response({"login": False, "userName": True , "password" :False })
    
    return Response({"login": True, "userName": True , "password" :True })
