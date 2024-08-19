from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
# Create your views here.
from django.core.paginator import Paginator


class login(APIView):
    template_name= "login.html"
    def get(self,request):
        return render(request,self.template_name)
   
    def post(self,request):
        correo = request.POST.get('correo').strip()
        password = request.POST.get('password').strip()
        if correo == 'julian.romero@outlook.com' and password == '5PG1azVR':
            # Generar la URL completa
            redirect_url = request.build_absolute_uri(reverse('homeCandidato'))
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        elif correo == 'noemi.hernandez@gmail.com' and password == 'i4xjkeQ4':
            # Generar la URL completa
            redirect_url = request.build_absolute_uri(reverse('homeCapacitador'))
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        elif correo == 'correo@autotechmanufacturing.com' and password == 'zs0xENQ1':
            # Generar la URL completa
            redirect_url = request.build_absolute_uri(reverse('homeEmpresa'))
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        elif correo == 'rh@partsandmore.com' and password == 'NxDdD4ON':
            # Generar la URL completa
            redirect_url = request.build_absolute_uri(reverse('homeEmpresaCursos'))
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        elif correo == 'careers@autotechsolutions.com' and password == 'nDhchExY':
            # Generar la URL completa
            redirect_url = request.build_absolute_uri(reverse('homeEmpresaVC'))
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        else:
            return JsonResponse({'success': False, 'message': 'Correo y/o contraseña incorrectos.'})
    
class homeEmpresaVC(APIView):
    template_name= "homeEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class capacitadorRegistroVC(APIView):
    template_name= "capacitadorRegistroVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class perfilEmpresaCurso(APIView):
    template_name= "perfilEmpresaCurso.html"
    def get(self,request):
        return render(request,self.template_name)
    
class postulacionesEmpresaVC(APIView):
    template_name= "postulacionesEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosEmpresaVC(APIView):
    template_name= "cursosEmpresaVC.html"
    def get(self, request):
        # Simulación de cursos como una lista de diccionarios
        cursos = [
            {'nombre': 'Motores de inyección', 'imagen': 'images/1.jpg'},
            {'nombre': 'Tuning de motos', 'imagen': 'images/4.jpg'},
            {'nombre': 'Motos general', 'imagen': 'images/3.jpg'},
            {'nombre': 'Motores de inyección', 'imagen': 'images/1.jpg'},
            {'nombre': 'Tuning de motos', 'imagen': 'images/4.jpg'},
            {'nombre': 'Motos general', 'imagen': 'images/3.jpg'},
            {'nombre': 'Curso 7', 'imagen': 'images/1.jpg'},
            {'nombre': 'Curso 8', 'imagen': 'images/4.jpg'},
            {'nombre': 'Curso 9', 'imagen': 'images/3.jpg'},
            # Añade más cursos si es necesario
        ]

        # Paginación: mostrar 6 cursos por página
        paginator = Paginator(cursos, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Pasar la página de objetos al template
        return render(request, self.template_name, {'page_obj': page_obj})
    
class listaCapacitadoresVC(APIView):
    template_name= "listaCapacitadoresVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class solicitudesCursoVC(APIView):
    template_name= "solicitudesCursoVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
    
class perfilEmpresaVC(APIView):
    template_name= "perfilEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class formularioCursoVC(APIView):
    template_name= "formularioCursoVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class editarFormularioCursoVC(APIView):
    template_name= "editarFormularioCursoVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosListaEmpresaVC(APIView):
    template_name= "cursosListaEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosInscritoEmpresaVC(APIView):
    template_name= "cursosInscritoEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class detallesCursoEmpresaVC(APIView):
    template_name= "detallesCursoEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
class solicitudEmpresaVC(APIView):
    template_name= "solicitudEmpresaVC.html"
    def get(self,request):
        return render(request,self.template_name)
    
    
class listaEmpresas(APIView):
    template_name= "listaEmpresas.html"
    def get(self,request):
        return render(request,self.template_name)
    
class listaCapacitadores(APIView):
    template_name= "listaCapacitadores.html"
    def get(self,request):
        return render(request,self.template_name)


class capacitadorRegistro(APIView):
    template_name= "capacitadorRegistro.html"
    def get(self,request):
        return render(request,self.template_name)


class homeEmpresaCursos(APIView):
    template_name= "homeEmpresaCursos.html"
    def get(self,request):
        return render(request,self.template_name)

class detallesCurso(APIView):
    template_name= "detallesCurso.html"
    def get(self,request):
        return render(request,self.template_name)
    
class datosEmpresa(APIView):
    template_name= "datosEmpresa.html"
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
        
class candidatoLista(APIView):
    template_name= "candidatoLista.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosListaEmpresa(APIView):
    template_name= "cursosListaEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    
class capacitadoresLista(APIView):
    template_name= "capacitadoresLista.html"
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
    
class vehiculosLista(APIView):
    template_name= "vehiculosLista.html"
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

class perfilEmpresa(APIView):
    template_name= "perfilEmpresa.html"
    def get(self,request):
        return render(request,self.template_name)
    
class solicitudesCursoCapacitador(APIView):
    template_name= "solicitudesCursoCapacitador.html"
    def get(self,request):
        return render(request,self.template_name)
    
class cursosEmpresa(APIView):
    template_name = "cursosEmpresa.html"

    def get(self, request):
        # Simulación de cursos como una lista de diccionarios
        cursos = [
            {'nombre': 'Motores de inyección', 'imagen': 'images/1.jpg'},
            {'nombre': 'Tuning de motos', 'imagen': 'images/4.jpg'},
            {'nombre': 'Motos general', 'imagen': 'images/3.jpg'},
            {'nombre': 'Motores de inyección', 'imagen': 'images/1.jpg'},
            {'nombre': 'Tuning de motos', 'imagen': 'images/4.jpg'},
            {'nombre': 'Motos general', 'imagen': 'images/3.jpg'},
            {'nombre': 'Curso 7', 'imagen': 'images/1.jpg'},
            {'nombre': 'Curso 8', 'imagen': 'images/4.jpg'},
            {'nombre': 'Curso 9', 'imagen': 'images/3.jpg'},
            # Añade más cursos si es necesario
        ]

        # Paginación: mostrar 6 cursos por página
        paginator = Paginator(cursos, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Pasar la página de objetos al template
        return render(request, self.template_name, {'page_obj': page_obj})
    
        
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
    

