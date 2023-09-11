from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
import pandas as pd
from django.conf import settings

def index(request):
    # ... some code to handle the year
    # data = 'App.Index'
    # return HttpResponse(data)

    # ********************* read data
    df = pd.read_csv(str(settings.BASE_DIR) + "/data/car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)
    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"', "class='table table-striped'")
    table_content = table_content.replace('border="1"', "")

    context = {"categories": categories, 'values': values, 'table_data': table_content}
    return render(request, 'index.html', context=context)


def view(request, myid):
    # ... some code to handle the year
    # data = 'App.View'
    # return HttpResponse(data)
    df = pd.read_csv(str(settings.BASE_DIR) + "/data/olist_orders_dataset.csv")
    rs = df.groupby("customer_id")["order_status"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)
    table_content = df.to_html(index=None)
    context = {"categories": categories, 'values': values, 'table_data': table_content}
    return render(request, 'index.html', context=context)

def check(request):
    data = 'App.Check'

    data += "<br>* " + reverse("application:index")
    data += "<br>* " + reverse("application:detail", kwargs={'myid': 123})
    data += "<br>* " + reverse("employee:index")
    data += "<br>* " + reverse("employee:detail", kwargs={'myid': 456})


    return HttpResponse(data)


