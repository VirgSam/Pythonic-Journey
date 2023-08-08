from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
month_dict={
        "jan":"Slay the Nemean lion",
        "feb":"Slay the nine-headed Lernaean Hydra",
        "mar":"Capture the Ceryneian Hind",
        "apr":"Capture the Erymanthian Boar",
        "may":"Clean the Augean stables in a single day",
        "jun":"Slay the Stymphalian birds.",
        "jul":"Capture the Cretan Bull",
        "aug":"Steal the Mares of Diomedes",
        "sep":"Obtain the girdle of Hippolyta, queen of the Amazon",
        "oct":"Obtain the cattle of the three-bodied giant Geryon",
        "nov":"Steal three of the golden apples of the Hesperides",
        "dec":None,#"Capture and bring back Cerberus"
    }

def index(request):
    list_items= ""
    months = list(month_dict.keys())
    # for month in months:
    #     capitalized_month= month.capitalize()
    #     month_path= reverse("month-challenge",args=[month])
    #     list_items += f"<li><a href=\'{month_path}\'>{capitalized_month}</a></li>"
    # response_data = f"<ol>{list_items}</ol>"
    # return HttpResponse(response_data)

    # using the for tag in the html doc
    return render (request,"challenges/index.html",{"months":months})

def monthly_challenges_by_numbers(request,month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("<H1>invalid month</H1>")
    else:
        redirect_month = months[month -1]
        redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenges/jan
        return HttpResponseRedirect(redirect_path)

    
def monthly_challenges(request,month):
    #output = None
    #if month in month_dict:
        #output = month_dict[month]
        #new_response=render_to_string("challenges/challenge.html")
        #return HttpResponse(f"<H1>{output}</H1>")
        #return HttpResponse(new_response)
    #else:
    #    return HttpResponseNotFound("Error")

    # another approach with render
    try:
        output = month_dict[month]
        cap_month=month.capitalize()
        return render(request, "challenges/challenge.html", {"text":output, "month": cap_month})
    except:
        #new_response=render_to_string("404.html")
        #return HttpResponseNotFound(new_response)
        raise Http404()

