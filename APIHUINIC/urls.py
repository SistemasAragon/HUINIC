"""APIHUINIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import(login,
                    detallesCurso,
                    formularioCurso,
                    homeCandidato,
                    homeCapacitador,
                    homeGeneral,
                    habilidadesLista,
                    homeSistemas,
                    recuperacionPass,
                    registroCapacitador,
                    resultadosVacantes,
                    solicitudesCurso, 
                    usuarioNuevo,
                    candidatoRegistro,
                    habilidadesCandidato,
                    perfilCandidato,
                    registroCandidato,
                    registroEmpresa,
                    homeEmpresa,
                    pruebaBusqueda,
                    postulaciones,
                    solicitudEmpresa)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postulaciones/', postulaciones.as_view(), name="postulaciones"),
    path('pruebaBusqueda/', pruebaBusqueda.as_view(), name="pruebaBusqueda"),
    path('habilidadesLista/', habilidadesLista.as_view(), name="habilidadesLista"),
    path('candidatoRegistro/', candidatoRegistro.as_view(), name="candidatoRegistro"),
    path('habilidadesCandidato/', habilidadesCandidato.as_view(), name="habilidadesCandidato"),
    path('perfilCandidato/', perfilCandidato.as_view(), name="perfilCandidato"),
    path('registroCandidato/', registroCandidato.as_view(), name="registroCandidato"),
    path('registroEmpresa/', registroEmpresa.as_view(), name="registroEmpresa"),
    path('solicitudEmpresa/', solicitudEmpresa.as_view(), name="solicitudEmpresa"),
    path('login/', login.as_view(), name="login"),
    path('detallesCurso/', detallesCurso.as_view(), name="detallesCurso"),
    path('formularioCurso/', formularioCurso.as_view(), name="formularioCurso"),
    path('homeCandidato/', homeCandidato.as_view(), name="homeCandidato"),
    path('homeCapacitador/', homeCapacitador.as_view(), name="homeCapacitador"),
    path('homeEmpresa/', homeEmpresa.as_view(), name="homeEmpresa"),
    path('homeGeneral/', homeGeneral.as_view(), name="homeGeneral"),
    path('homeSistemas/', homeSistemas.as_view(), name="homeSistemas"),
    path('recuperacionPass/', recuperacionPass.as_view(), name="recuperacionPass"),
    path('registroCapacitador/', registroCapacitador.as_view(), name="registroCapacitador"),
    path('resultadosVacantes/', resultadosVacantes.as_view(), name="resultadosVacantes"),
    path('solicitudesCurso/', solicitudesCurso.as_view(), name="solicitudesCurso"),
    path('usuarioNuevo/', usuarioNuevo.as_view(), name="usuarioNuevo"),
]
