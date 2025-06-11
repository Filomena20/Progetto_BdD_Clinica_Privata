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

from Clinica.views import pagina_iniziale, evento_pagina_iniziale, area_privata, registrazione_paziente, \
    login_personale, logout_paziente, logout_personale, logout_amministratore, area_riservata_paziente, \
    area_riservata_personale, area_riservata_amministratore, login_amministratore, lista_trattamenti_amministratore, \
    elimina_trattamento_amministratore, aggiungi_trattamento_amministratore, trattamenti_pagina_iniziale, \
    lista_eventi_amministratore, elimina_evento_amministratore, aggiungi_evento_amministratore, \
    visualizza_eventi_personale, iscrizione_evento_personale, annulla_iscrizione_evento_personale, \
    lista_cartelle_personale, elimina_cartella_clinica, crea_cartella_clinica, visualizza_cartella_paziente, \
    visualizza_eventi_paziente, iscrizione_evento_paziente, annulla_iscrizione_evento_paziente, \
    visualizza_prenotazioni_paziente, annulla_prenotazione, crea_prenotazione, crea_recensione, visualizza_recensioni, \
    recensioni_utenti, conferma_visita, visualizza_prenotazioni_personale, annulla_conferma_visita, \
    modifica_cartella_clinica, trattamenti_prenotati_amministratore, elimina_recensione_paziente, \
    pdf_prenotazione, aggiorna_presenze,  login_paziente

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', pagina_iniziale, name='pagina_iniziale'),
    path('eventi/', evento_pagina_iniziale, name='evento_pagina_iniziale'),
    path('trattamenti/', trattamenti_pagina_iniziale, name='trattamenti_pagina_iniziale'),
    path('recensioni/', recensioni_utenti, name='recensioni_utenti'),
    path('area_privata/', area_privata, name='area_privata'),
    path('registrazione_paziente/', registrazione_paziente, name='registrazione_paziente'),

    path('login_personale/', login_personale, name='login_personale'),
    path('login_amministratore/', login_amministratore, name='login_amministratore'),
    path('logout_paziente/', logout_paziente, name='logout_paziente'),
    path('logout_personale/', logout_personale, name='logout_personale'),
    path('logout_amministratore/', logout_amministratore, name='logout_amministratore'),
    path('area_riservata_paziente/', area_riservata_paziente, name='area_riservata_paziente'),
    path('area_riservata_personale/', area_riservata_personale, name='area_riservata_personale'),
    path('area_riservata_amministratore/', area_riservata_amministratore, name='area_riservata_amministratore'),
    path('lista_trattamenti_amministratore/', lista_trattamenti_amministratore, name='lista_trattamenti_amministratore'),
    path('elimina_trattamento_amministratore/<int:trattamento_id>/', elimina_trattamento_amministratore, name='elimina_trattamento_amministratore'),
    path('aggiungi_trattamento_amministratore/', aggiungi_trattamento_amministratore, name='aggiungi_trattamento_amministratore'),
    path('lista_eventi_amministratore/', lista_eventi_amministratore, name='lista_eventi_amministratore'),
    path('elimina_evento_amministratore/<int:evento_id>/', elimina_evento_amministratore, name='elimina_evento_amministratore'),
    path('aggiungi_evento_amministratore/', aggiungi_evento_amministratore, name='aggiungi_evento_amministratore'),
    path('visualizza_eventi_personale/', visualizza_eventi_personale, name='visualizza_eventi_personale'),
    path('iscrizione_evento_personale/<int:evento_id>/', iscrizione_evento_personale, name='iscrizione_evento_personale'),
    path('annulla_iscrizione_evento_personale/<int:evento_id>/', annulla_iscrizione_evento_personale, name='annulla_iscrizione_evento_personale'),
    path('cartelle_personale/', lista_cartelle_personale, name='lista_cartelle_personale'),
    path('elimina_cartella_personale/<int:cartella_id>/', elimina_cartella_clinica, name='elimina_cartella_clinica'),
    path('crea_cartella_clinica/', crea_cartella_clinica, name='crea_cartella_clinica'),
    path('cartella_paziente/', visualizza_cartella_paziente, name='visualizza_cartella_paziente'),
    path('visualizza_eventi_paziente/', visualizza_eventi_paziente, name='visualizza_eventi_paziente'),
    path('iscrizione_evento_paziente/<int:evento_id>/', iscrizione_evento_paziente, name='iscrizione_evento_paziente'),
    path('annulla_iscrizione_evento_paziente/<int:evento_id>/', annulla_iscrizione_evento_paziente, name='annulla_iscrizione_evento_paziente'),
    path('prenotazioni/', visualizza_prenotazioni_paziente, name='visualizza_prenotazioni_paziente'),
    path('annulla_prenotazione/<int:prenotazione_id>/', annulla_prenotazione, name='annulla_prenotazione'),
    path('crea_prenotazione/', crea_prenotazione, name='crea_prenotazione'),
    path('visualizza_recensioni/', visualizza_recensioni, name='trattamenti_recensiti'),
    path('crea_recensione/', crea_recensione, name='crea_recensione'),
    path('elimina_recensione_paziente/<int:recensione_id>/', elimina_recensione_paziente, name='elimina_recensione_paziente'),
    path('conferma_visita/<int:prenotazione_id>/', conferma_visita, name='conferma_visita'),
    path('appuntamenti/', visualizza_prenotazioni_personale, name='visualizza_prenotazioni_personale'),
    path('annulla_conferma_visita/<int:prenotazione_id>/', annulla_conferma_visita, name='annulla_conferma_visita'),
    path('modifica_cartella_clinica/<int:cartella_id>/', modifica_cartella_clinica, name='modifica_cartella_clinica'),
    path('trattamenti_prenotati_amministratore/', trattamenti_prenotati_amministratore, name='trattamenti_prenotati_amministratore'),
    path('pdf/<int:prenotazione_id>/', pdf_prenotazione, name='pdf_prenotazione'),
    path('aggiorna_presenze/<int:evento_id>/', aggiorna_presenze, name='aggiorna_presenze'),


    path('login_paziente/', login_paziente, name='login_paziente'),
    #login vulnerabile
    #path('login_vulnerabile_paziente/', login_vulnerabile_paziente, name='login_vulnerabile_paziente'),


]








