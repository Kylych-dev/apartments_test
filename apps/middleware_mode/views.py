from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    # context = {}
    # return render(request, 'index.html', context)
    return TemplateResponse(request, 'index.html')


'''

<!-- {% extends 'base.html' %}
{% block content %}

<div class="container">
    <h1> We're in!</h1>
    {% lorem 5%}
</div>


{% endblock %} -->




from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    template = loader.get_template('index.html')
    response = HttpResponse(template.render(context, request))
    return response




'''