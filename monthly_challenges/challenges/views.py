from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


challenge_text = {
    "january": "It's January",
    "february": "It's February",
    "march": "It's March",
    "april": "It's April",
    "may": "It's May",
    "june": "It's June",
    "july": "It's July",
    "august": "It's August",
    "september": "It's September",
    "october": "It's October",
    "november": "It's November",
    "december": "It's December"
}

# Create your views here.

def january(request):
    return HttpResponse("Indeed January")



def february(request):
    return HttpResponse("Indeed February")


def monthly_challenges_by_int(request, month):
    months_list = list(challenge_text.keys())
    redirect_month = months_list[month]
    
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# month has to match the exact <month>
def monthly_challenges_by_string(request, month):
    # print(month)
    try: 
        res_text = challenge_text[month]
        response_data = f"<h1>{res_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This is not a valid month")
    