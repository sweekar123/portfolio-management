from django.shortcuts import get_object_or_404, render,redirect
from stocks.models import Stock
from stocks.forms import StockForm
# Create your views here.

def stock_add_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StockForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("stock-add")
            else:
                form = StockForm(request.POST)
                context = {
                    "form" : form
                }
                return render(request,"stocks/stock_add.html",context)
        else:
            form = StockForm()
            context = {
                "form" : form
            }
            return render(request,"stocks/stock_add.html",context)
    else:
        return redirect("login")

def stock_list_view(request):
    if request.user.is_authenticated:
        queryset = Stock.objects.all().order_by("id")
        print(queryset)
        context = {
            "objects" : queryset
        }
        return render(request,"stocks/stock_list.html",context)
    else:
        return redirect("login")


def overall_stock_dashboard(request):
    if request.user.is_authenticated:
        queryset = Stock.objects.filter(transaction_type="SELL")
        total_investment = 0
        total_unit = 0
        total_current_amount = 0
        total_profit = 0
        for instance in queryset:
            total_investment = 0 + instance.investment
            total_unit = 0 + instance.no_of_stocks
            total_current_amount = 0 + instance.current_amount
            total_profit = 0 + instance.profit
        context = {
            "investment" : total_investment,
            "units" : total_unit,
            "current_amount" : total_current_amount,
            "profit" : total_profit
        }
        return render(request,"stocks/overall_stock_dashboard.html",context)
    else:
        return redirect("login")

def individual_stock_dashboard(request):
    if request.user.is_authenticated:
        queryset = Stock.objects.filter(transaction_type="SELL")
        context = {
            "objects" : queryset
        }
        return render(request,"stocks/stock_detail.html",context)
    else:
        return render("login")

def stock_update_view(request,id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Stock,id=id)
        if request.method == "POST":
            form = StockForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("stock-add")
            else:
                form = StockForm(request.POST,instance=obj)
                context = {
                    "form" : form
                }
                return render(request,"stocks/stock_add.html",context)
        else:
            form = StockForm(instance=obj)
            context = {
                "form" : form
            }
            return render(request,"stocks/stock_add.html",context)
    else:
        return redirect("login")


def stock_delete_view(request,id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Stock,id=id)
        if request.method == "POST":
            obj.delete()
            return redirect("stock-list")
        else:
            context = {
                "object" : obj
            }
            return render(request,"stocks/stock_delete.html",context)
    else:
        return redirect("login")

            
            

