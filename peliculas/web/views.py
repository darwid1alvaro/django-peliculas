from django.shortcuts import render

# Create your views here.


def index(request):
    peliculas = [
        {
            'titulo': 'AVATAR 2',
            'imagen': 'https://fotografias.larazon.es/clipping/cmsimages02/2021/12/17/A856C949-2A30-4AB5-A0FB-23043A0B8B22/98.jpg?crop=3317,1866,x0,y0&width=1900&height=1069&optimize=low&format=webply',

        },
        {
            'titulo': 'MARIO BROSS',
            'imagen': 'https://i.blogs.es/b9f542/1500x500-5-/840_560.jpeg'
        },
        {
            'titulo': 'shazam 2',
            'imagen': 'https://media.vandalsports.com/i/640x360/3-2023/202332282811_1.jpg'
        }

    ]
    context = {
        'peliculas': peliculas
    }

    return render(request,'index.html',context)


