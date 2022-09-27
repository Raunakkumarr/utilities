from django.shortcuts import render
from notice_updates.models import subscription
from django.contrib import messages

# Create your views here.
def app(request):
    context = {}
    if request.method == 'POST':
        u_email = request.POST['emails']
        u_category = request.POST['category']
        subscription.objects.create(emails=u_email, category=u_category)
        context['subscription_added']='True'
        context['s_email'] = u_email
        if u_category=='pu':
            context['s_category'] = 'Pokhara University - Scholarships'
        elif u_category=='ioe':
            context['s_category'] = 'IOE - Entrance Notices'
        elif u_category=='wrc':
            context['s_category'] = 'IOE Pulchowk Campus - Admission Notices'
        elif u_category=='pcampus':
            context['s_category'] = 'IOE WRC - Admission Notices'
    return render(request, 'app/home.html', context)
