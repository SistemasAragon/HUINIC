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
    
class detallesCursoEmpresa(APIView):
    template_name= "detallesCursoEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosInscritoEmpresa(APIView):
    template_name= "cursosInscritoEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)

class editarFormularioCurso(APIView):
    template_name= "editarFormularioCurso.html"
    def get(self,request):
        return render(request,self.template_name)


class cursosInscritoCandidato(APIView):
    template_name= "cursosInscritoCandidato.html"
    def get(self,request):
        return render(request,self.template_name)

class conocimientosLista(APIView):
    template_name= "conocimientosLista.html"
    def get(self,request):
        return render(request,self.template_name)
    
class empresasLista(APIView):
    template_name= "empresasLista.html"
    def get(self,request):
        return render(request,self.template_name)
        
class cursosListaEmpresa(APIView):
    template_name= "cursosListaEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)

class cursosListaCandidato(APIView):
    template_name= "cursosListaCandidato.html"
    def get(self,request):
        return render(request,self.template_name)
    

class cursosListaCapacitador(APIView):
    template_name= "cursosListaCapacitador.html"
    def get(self,request):
        return render(request,self.template_name)
    
class editarPerfil(APIView):
    template_name= "editarPerfil.html"
    def get(self,request):
        return render(request,self.template_name)
    

class editarPerfilCapacitador(APIView):
    template_name= "editarPerfilCapacitador.html"
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
class homeEmpresa(APIView):
    template_name= "homeEmpresa.html"
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

class postulacionesEmpresa(APIView):
    template_name= "postulacionesEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    

    
class perfilEmpresaLogo(APIView):
    template_name= "perfilEmpresaLogo.html"
    def get(self,request):
        return render(request,self.template_name)
    
class habilidadesLista(APIView):
    template_name= "habilidadesLista.html"
    def get(self,request):
        return render(request,self.template_name)

class postulaciones(APIView):
    template_name= "postulaciones.html"
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
    
class usuarioNuevo(APIView):
    template_name= "usuarioNuevo.html"
    def get(self,request):
        return render(request,self.template_name)
    
class candidatoRegistro(APIView):
    template_name= "candidatoRegistro.html"
    def get(self,request):
        return render(request,self.template_name)
    
class habilidadesCandidato(APIView):
    template_name= "habilidadesCandidato.html"
    def get(self,request):
        return render(request,self.template_name)
    
class perfilCandidato(APIView):
    template_name= "perfilCandidato.html"
    def get(self,request):
        return render(request,self.template_name)
    
class registroCandidato(APIView):
    template_name= "registroCandidato.html"
    def get(self,request):
        return render(request,self.template_name)
    
class registroEmpresa(APIView):
    template_name= "registroEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    
    
class solicitudEmpresa(APIView):
    template_name= "solicitudEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    

class pruebaBusqueda(APIView):
    template_name= "pruebaBusqueda.html"
    def get(self,request):
        return render(request,self.template_name)
    

class habilidadesCandidatoN2(APIView):
    template_name= "habilidadesCandidatoN2.html"
    def get(self,request):
        return render(request,self.template_name)
    

