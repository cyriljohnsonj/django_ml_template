from django.shortcuts import render


def index(request):
    context = {
        "title": "ML Predictor",
        "application": "Predict the MPG"
    }

    return render(
        request,
        "index.html",
        context
    )
