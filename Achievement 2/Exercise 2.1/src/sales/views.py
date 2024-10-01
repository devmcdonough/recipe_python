from django.shortcuts import render
# to protect function based views
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sales
import pandas as pd
from .utils import get_booknamefrom_id, get_chart

# Create your views here.
def home(request):
    # Renders home.html file
    return render(request, 'sales/home.html')

# Define function based view
@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    # initialize dataframe to None
    sales_df = None
    chart = None
    # check if the button is clicked
    if request.method == 'POST':
        # read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        # display in terminal - only needed for debugging
        print(book_title, chart_type)

        print('Exploring querysets:')
        print('Case 1: Output of Sales.object.all()')
        qs=Sales.objects.all()
        print (qs)

        print("Case 2: Output of Sales.objects.filter(book__name=book_title)")
        qs = Sales.objects.filter(book__name=book_title)
        print (qs)

        # Convert queryset to pandas dataframe if there are results
        if qs:
            # Convert qs values to a pandas dataframe
            sales_df = pd.DataFrame(qs.values())
            # convert book ID to name of book
            sales_df['book_id']=sales_df['book_id'].apply(get_booknamefrom_id)
            print(sales_df)

            chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)

            # Convert dataframe to HTML
            sales_df = sales_df.to_html()

        print("Case 3: Output of qs.values")
        print(qs.values())

        print("Case 4: Output of qs.values_list()")
        print(qs.values_list())

        print("Case 5: Output of Sales.objects.get(id=1)")
        obj = Sales.objects.get(id=1)
        print(obj)

    context = {
        'form': form,
        'sales_df': sales_df,
        'chart': chart
    }
    
    # Simply display page
    return render(request, 'sales/records.html', context)