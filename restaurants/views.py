from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    		'my_list': [
    				{
    					'restaurant_name': 'Burger King',
    					'food_type': 'Burgers'
    				},
    				{
	    				'restaurant_name': "McDonald's",
	    				'food_type': 'Fries'
	    			},
    				{
	    				'restaurant_name': 'Subway',
	    				'food_type': 'Sandwiches'
    				},
				],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    		'my_object': {
					'restaurant_name': 'Burger King',
					'food_type': 'Burgers',
    		},
    }
    return render(request, 'detail.html', context)
