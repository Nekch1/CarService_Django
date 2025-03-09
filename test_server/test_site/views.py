from django.shortcuts import render
from django.templatetags.static import static

def index_page(request):
    context = {
        "page_name":"Автосервис",
        "services": [
            {
                "title" : 'Замена масла',
                "img" : static("images/zamena-masla.jpg"),
            },
                        
            {

                "title" : 'Диагностика двигателя',
                "img" : static("images/engine-diagnostics.jpg"),
            },

            {
                "title" : 'Покраска кузова',
                "img" : static("images/painting.png"),
            },

            {
                "title" : 'Балансировка колес',
                "img" : static("images/wheel-balancing.jpeg"),
            }
        ]
    }
    return render(request, 'index.html', context)

