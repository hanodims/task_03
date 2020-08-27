from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list' : [
            {
                'restaurant_name': 'Bateel',
                'food_type':'Coffee & dessert',
            },
            {
                'restaurant_name': 'KFC',
                'food_type':'Fast Food',
            },
             
            {
                'restaurant_name': 'Nozomi',
                'food_type':'Sushi',
            }
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object' :  {
                'restaurant_name': 'Salt',
                'food_type':'Burger',
            }

    }
    return render(request, 'detail.html', context)
