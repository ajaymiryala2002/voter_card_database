# from django.shortcuts import render, redirect
# from app1.forms import VoterForm

# def voter_form(request):
#     if request.method == 'POST':
#         form = VoterForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.save()
#             return redirect('card', id=data.id)
#     else:
#         form = VoterForm()

#     return render(request, 'voter_form.html', {'form': form})


# def voter_card(request, id):
#     from .models import Voter
#     data = Voter.objects.get(id=id)
#     return render(request, 'voter_card.html', {'data': data})



from django.shortcuts import render
from .forms import VoterForm
from .models import Voter

def voter_form(request):
    if request.method == "POST":
        form = VoterForm(request.POST, request.FILES)
        if form.is_valid():
            voter = form.save()
            return render(request, "voter_card.html", {"data": voter})
    else:
        form = VoterForm()
    return render(request, "voter_form.html", {"form": form})

def voter_card(request, id):
    data = Voter.objects.get(id=id)
    return render(request, "voter_card.html", {"data": data})
