from django.shortcuts import render
from.models import FeedbackData
from django.contrib import messages

def feedback_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ramnaamjap = request.POST.get('ramnaamjap')

        FeedbackData(
            name=name,
            ramnaamjap=ramnaamjap,
        ).save()

        messages.success(request, "Post Was Created Successfully")

        feedbacks2 = FeedbackData.objects.order_by("-feedback_date")
        return render(request, 'feedbacks.html', {'narayana': feedbacks2})

    else:
        feedbacks2 = FeedbackData.objects.order_by("-feedback_date")
        return render(request, 'feedbacks.html', {'narayana': feedbacks2})
