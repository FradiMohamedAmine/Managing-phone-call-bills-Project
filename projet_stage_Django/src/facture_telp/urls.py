from django.urls import include, path

from . import api

app_name = 'facture'

urlpatterns = [
    path('clientlist/', api.the_list_of_customers, name='the list of customers'),
    path('servicelist/', api.the_list_of_services, name='the list of services'),
    path('offrelist/', api.the_list_of_offers, name='the list of offers'),
    path('contratlist/', api.the_list_of_contracts, name='the list of contracts'),
    path('facturelist/', api.the_list_of_bills, name='the list of bills'),
    path('clientdetail/<int:pk>/', api.the_details_about_a_customer, name='the details about a customer'),
    path('servicedetail/<int:pk>/', api.the_details_about_a_service, name='the details about a service'),
    path('offredetail/<int:pk>/', api.the_details_about_an_offer, name='the details about an offer'),
    path('contratdetail/<int:pk>/', api.the_details_about_a_contract, name='the details about a contract'),
    path('facturedetail/<int:pk>/', api.the_details_about_a_bill, name='the details about a bill'),
    path('contratlistbyClient/<int:pk>/', api.the_list_of_contracts_for_a_given_customer,name='the list of contracts for a given customer'),
    path('facturelistbyClient/<int:pk>/', api.the_list_of_bills_for_a_given_customer,name='the list of bills for a given customer'),
    path('sommefacturebyfactureID/<int:pk>/', api.the_amount_to_be_paid_for_a_bill,name='the amount to be paid for a bill '),
    path('checkpaidfacturebyID/<int:pk>/', api.bill_paid,name=' Bill paid or Not '),
    path('checkuser/', api.check_user,name=' Check user '),

]
