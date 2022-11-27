from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Player, Status

class DataJobs:
    
    def GetStatus():
        S = Status.objects.all()
        for s in S:
            return s.status
        return 'None'
        
    def UpdateStatus(status):
        s = DataJobs.GetStatus()
        if s:
            Status.objects.update(status = status)
        else: Status.objects.create(status = status)
    
    def DeletePlayers():
        Player.objects.all().delete()
    
    def AddPlayer(name):
        post_instance = Player.objects.create(name = name)
        id = post_instance.pk
        return id
    
    def UpdatePlayer(id, wrongs, seconds):
        Player.objects.filter(id = id).update(wrong = wrongs, seconds = seconds)
        
    def UpdateWinners():
        lowWrongs = 10
        lowSecs = 1000
        P = Player.objects.all()
        for p in P:
            if p.wrong < lowWrongs:
                lowWrongs = p.wrong
        for p in P:
            if p.wrong == lowWrongs:
                if p.seconds < lowSecs:
                    lowSecs = p.seconds
        for p in P:
            if p.wrong == lowWrongs and p.seconds == lowSecs:
                Player.objects.filter(id = p.id).update(winner = True)

    def GetWinners(id):
        winnersYou = []
        winners = []
        P = Player.objects.filter(winner = True)  
        for p in P:
            winners.append([p.name, p.wrong, p.seconds])
        if id == 0:
            winnersYou = [winners, 0, 0]
        else:
            P = Player.objects.get(id = id)
            winnersYou = [winners, P.wrong, P.seconds]
            #winnersYou.append([winners, P.wrong, P.seconds])
        return winnersYou
                     