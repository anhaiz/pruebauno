import win_inet_pton
from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip
from ipware.utils import is_valid_ipv4

def index(request):
	address = get_client_ip(request)
	addr = is_valid_ipv4(address[0])
	if addr == True:
		return render(request, "home.html", {})	
	else:
		return HttpResponse("Sorry, only reachable by IPv6")