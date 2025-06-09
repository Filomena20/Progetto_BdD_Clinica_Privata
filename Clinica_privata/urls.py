"""
URL configuration for Clinica_privata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

from Clinica.views import pagina_iniziale, evento, login_paziente, registrazione_paziente, area_privata, \
    login_personale, login_amministratore, lista_eventi, iscrizione_evento, \
    visualizza_eventi, area_riservata_paziente, area_riservata_personale, area_riservata_amministratore, \
    logout_paziente, logout_amministratore, logout_personale, gestione_trattamenti, lista_trattamenti, \
    aggiungi_trattamento, elimina_trattamento, cartella_clinica, annulla_iscrizione_evento

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', pagina_iniziale, name='pagina_iniziale'),
    path('area_privata/', area_privata, name='area_privata'),
    path('eventi/', evento, name='eventi'),
    path('registrazione_paziente/', registrazione_paziente, name='registrazione_paziente'),
    path('login_paziente/', login_paziente, name='login_paziente'),
    path('login_personale/', login_personale, name='login_personale'),
    path('login_amministratore/', login_amministratore, name='login_amministratore'),
    #path('area_riservata/', area_riservata, name='area_riservata'),

    path('area_riservata_paziente/', area_riservata_paziente, name='area_riservata_paziente'),
    path('area_riservata_personale/', area_riservata_personale, name='area_riservata_personale'),
    path('area_riservata_amministratore/', area_riservata_amministratore, name='area_riservata_amministratore'),
    #path('logout/', logout, name='logout'),
    path('logout_paziente/', logout_paziente, name='logout_paziente'),
    path('logout_amministratore/', logout_amministratore, name='logout_amministratore'),
    path('logout_personale/', logout_personale, name='logout_personale'),
    path('eventi/', lista_eventi, name='lista_eventi'),
    path('visualizza_eventi/', visualizza_eventi, name='visualizza_eventi'),

    path('eventi/<int:evento_id>/iscriviti/', iscrizione_evento, name='iscrizione_evento'),
    path('eventi/<int:evento_id>/annulla/', annulla_iscrizione_evento, name='annulla_iscrizione_evento'),

    #path('scegli_login/', scegli_login, name='scegli_login'),
    path('gestione-trattamenti/',gestione_trattamenti, name='gestione_trattamenti'),
    path('lista_trattamenti/', lista_trattamenti, name='lista_trattamenti'),
    path('aggiungi/', aggiungi_trattamento, name='aggiungi_trattamento'),
    path('elimina/', elimina_trattamento, name='elimina_trattamento'),
    path('cartella_clinica/', cartella_clinica, name='cartella_clinica'),




]

"""
    

    path('eventi/', evento, name='eventi'),
    path('eventi/<int:evento_id>/iscriviti/', iscrizione_evento, name='iscrizione_evento'),
    path('eventi/<int:evento_id>/annulla_iscrizione/', annulla_iscrizione_evento, name='annulla_iscrizione_evento'),

    path('cartella_clinica/', cartella_clinica, name='cartella_clinica'),
    path('recensioni/', trattamenti_recensibili, name='trattamenti_recensibili'),
    path('recensioni/nuova/<int:trattamento_id>/', lascia_recensione, name='lascia_recensione'),
    path('prenota/',crea_prenotazione, name='crea_prenotazione'),
    path('cartelle/', cartelle_personale_view, name='cartelle_personale')

"""






