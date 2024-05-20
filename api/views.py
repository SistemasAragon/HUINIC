from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class login(APIView):
    template_name= "login.html"
    def get(self,request):
        return render(request,self.template_name)

class detallesCurso(APIView):
    template_name= "detallesCurso.html"
    def get(self,request):
        return render(request,self.template_name)

class formularioCurso(APIView):
    template_name= "formularioCurso.html"
    def get(self,request):
        return render(request,self.template_name)

class homeCandidato(APIView):
    template_name= "homeCandidato.html"
    def get(self,request):
        return render(request,self.template_name)

class homeCapacitador(APIView):
    template_name= "homeCapacitador.html"
    def get(self,request):
        return render(request,self.template_name)

class homeGeneral(APIView):
    template_name= "homeGeneral.html"
    def get(self,request):
        return render(request,self.template_name)

class homeSistemas(APIView):
    template_name= "homeSistemas.html"
    def get(self,request):
        return render(request,self.template_name)

class recuperacionPass(APIView):
    template_name= "recuperacionPass.html"
    def get(self,request):
        return render(request,self.template_name)

class registroCapacitador(APIView):
    template_name= "registroCapacitador.html"
    def get(self,request):
        return render(request,self.template_name)

class resultadosVacantes(APIView):
    template_name= "resultadosVacantes.html"
    def get(self,request):
        return render(request,self.template_name)

class solicitudesCurso(APIView):
    template_name= "solicitudesCurso.html"
    def get(self,request):
        return render(request,self.template_name)
