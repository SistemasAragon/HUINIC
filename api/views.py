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
    
class tipo_usuario_nuevo1(APIView):
    template_name= "tipo_usuario_nuevo1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class candidato_registro1(APIView):
    template_name= "candidato_registro1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class habilidades_candidato1(APIView):
    template_name= "habilidades_candidato1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class perfil_candidato1(APIView):
    template_name= "perfil_candidato1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class registro_candidato1(APIView):
    template_name= "registro_candidato1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class registro_empresa1(APIView):
    template_name= "registro_empresa1.html"
    def get(self,request):
        return render(request,self.template_name)
    
    
class solicitud_empresa1(APIView):
    template_name= "solicitud_empresa1.html"
    def get(self,request):
        return render(request,self.template_name)
    

