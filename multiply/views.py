from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .DataInterface import DataJobs

def index(request):
    
    if request.method == "POST":
       # name = request.POST['Name']
        status = DataJobs.GetStatus()
     #   context = {'name': name, 'status': status}
        if 'btnStart' in request.POST:
            name = request.POST['Name']
            if status == 'Live':
                id = DataJobs.AddPlayer(name)
                context = {'status': status, 'PersonID': id}
                return render(request, 'multiply/index.html', context)
            context = {'status': status, 'PersonID': 0, 'name': name}
            return render(request, 'multiply/index.html', context)
        if 'btnResult' in request.POST:
            id = request.POST['ID']
            if status == 'Done':
                winnersYou = DataJobs.GetWinners(id)
                context = {'winnersYou': winnersYou}
                return render(request, 'multiply/results.html', context)
            else: 
              #  seconds = float(request.POST['Seconds'])
                
              #  if seconds > 0:
                #    wrongs = request.POST['Wrongs']
                #    DataJobs.UpdatePlayer(id, wrongs, seconds)
                status = 'Wait'
                context = {'status': status, 'PersonID': id}
                return render(request, 'multiply/index.html', context)
        if 'btnSubmit' in request.POST:
                seconds = float(request.POST['Seconds'])
                id = request.POST['ID']
                if seconds > 0:
                    wrongs = request.POST['Wrongs']
                    DataJobs.UpdatePlayer(id, wrongs, seconds)
                status = 'Wait'
                context = {'status': status, 'PersonID': id}
                return render(request, 'multiply/index.html', context)
        if 'btnLaunch' in request.POST:
            return render(request, 'multiply/launcher.html')
    status = DataJobs.GetStatus()
    if(status == 'Live' or status == 'Done'):
        status = 'None' 
    context = {'status': status}
    return render(request, 'multiply/index.html', context)

def launcher(request):
    if request.method == "POST":
        if 'btnLaunch' in request.POST:
            DataJobs.UpdateStatus('Live')
        if 'btnReveal' in request.POST:
            DataJobs.UpdateStatus('Done')
            DataJobs.UpdateWinners()
            winnersYou = DataJobs.GetWinners(0)
            print(winnersYou)
            context = {'winnersYou': winnersYou}
            return render(request, 'multiply/results.html', context)
        if 'btnLock' in request.POST:
            DataJobs.UpdateStatus('Off')
            DataJobs.DeletePlayers()
    return render(request, 'multiply/launcher.html')

def results(request):
    if request.method == "POST":
        return render(request, 'multiply/results.html')
    return render(request, 'multiply/results.html')
