import hashlib
from datetime import datetime, time, timedelta
from io import BytesIO

from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from reportlab.pdfgen import canvas

from Clinica.models import Evento, Paziente, Personale, Amministratore_Clinica, Trattamento, Iscrizione, \
    Cartella_Clinica, Gestione, Prenotazione, Recensione, Svolgimento


#PAGINA INIZIALE
def pagina_iniziale(request):
    return render(request, 'pagina_iniziale.html')

#EVENTI PAGINA INIZIALE
def evento_pagina_iniziale(request):
    eventi = Evento.objects.all().order_by('data')
    return render(request, 'eventi.html', {'eventi': eventi})

#TRATTAMENTI PAGINA INIZIALE
def trattamenti_pagina_iniziale(request):
    trattamenti = Trattamento.objects.all().order_by('nome')
    return render(request, 'trattamenti.html', {'trattamenti': trattamenti})

#RECENSIONI PAGINA INIZIALE

def recensioni_utenti(request):
    recensioni = Recensione.objects.select_related('paziente', 'trattamento').order_by('-id')

    return render(request, 'recensioni_utenti.html', {
        'recensioni': recensioni
    })

#AREA PRIVATA
def area_privata(request):
    return render(request, 'area_privata.html')


#AUTENTICAZIONE UTENTI
def autenticazione_paziente(email, password):
    return Paziente.objects.filter(email=email, password=password).exists()


def autenticazione_personale(email, password):
    return Personale.objects.filter(email=email, password=password).exists()

def autenticazione_amministratore(email, password):
    return Amministratore_Clinica.objects.filter(email=email, password=password).exists()

#REGISTRAZIONE PAZIENTE
def registrazione_paziente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        codice_fiscale = request.POST.get('codice_fiscale')
        patologie = request.POST.get('patologie')
        allergie = request.POST.get('allergie')
        cellulare = request.POST.get('cellulare')
        indirizzo = request.POST.get('indirizzo')
        data_nascita_str = request.POST.get('data_nascita')
        # poichè deve essere y/m/d e il browser la da in g/m/a devo:
        try:
            data_nascita = datetime.strptime(data_nascita_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'registrazione_paziente.html', {
                'error': "Data non valida deve essere in formato Y-M-D"
            })

        # print(email," : ", hashed_password)
        if Paziente.objects.filter(email=email).exists():
            return render(request, 'registrazione_paziente.html',
                          {'error': "Email già in uso"})
        else:
            paziente = Paziente.objects.create(
                email=email,
                password=hashed_password,
                nome=nome,
                cognome=cognome,
                codice_fiscale=codice_fiscale,
                patologie=patologie,
                allergie=allergie,
                cellulare=cellulare,
                indirizzo=indirizzo,
                data_nascita=data_nascita
            )

            return render(request, 'area_riservata_paziente.html', {
                'success': "Registrazione avvenuta con successo",
                'paziente': paziente
            })
    else:
        return render(request, 'registrazione_paziente.html')


#LOGIN PAZIENTE
def login_paziente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        #print (email, " : ", hashed_password)
        if autenticazione_paziente(email, hashed_password):
            request.session['paziente_email'] = email
            return redirect('area_riservata_paziente')
        else:
            return render(request, 'login_paziente.html',
                          {'error': "Credenziali non valide, riprova",
                           'email': email})
    else:
        return render(request, 'login_paziente.html')



#LOGIN PERSONALE
def login_personale(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        #print (email, " : ", hashed_password)
        if autenticazione_personale(email, hashed_password):
            request.session['personale_email'] = email
            return redirect('area_riservata_personale')
        else:
            return render(request, 'login_personale.html',
                          {'error': "Credenziali non valide, riprova",
                           'email': email})
    else:
        return render(request, 'login_personale.html')

#LOGIN  AMMINISTRATORE
def login_amministratore(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        #print(email, " : ", hashed_password)

        if autenticazione_amministratore(email, hashed_password):
            # Salva l'email nella sessione
            request.session['amministratore_email'] = email
            return redirect('area_riservata_amministratore')
        else:
            return render(request, 'login_amministratore.html', {
                'error': "Credenziali non valide, riprova",
                'email': email
            })
    else:
        return render(request, 'login_amministratore.html')

# LOGOUT
def logout_paziente(request):
    request.session.flush()
    return redirect('login_paziente')


def logout_personale(request):
    request.session.flush()
    return redirect('login_personale')

def logout_amministratore(request):
    request.session.flush()
    return redirect('login_amministratore')

#AREA RISERVATA PAZIENTE
def area_riservata_paziente(request):
    if 'paziente_email' in request.session:
        email = request.session['paziente_email']
        paziente = Paziente.objects.get(email=email)
        return render(request, 'area_riservata_paziente.html', {'paziente': paziente})
    else:
        return redirect('login_paziente')

#AREA  RISERVATA PERSONALE
def area_riservata_personale(request):
    if 'personale_email' in request.session:
        email = request.session['personale_email']
        personale = Personale.objects.get(email=email)
        return render(request, 'area_riservata_personale.html', {'personale': personale})
    else:
        return redirect('login_personale')

#AREA  RISERVATA AMMINISTRATORE
def area_riservata_amministratore(request):
    if 'amministratore_email' in request.session:
        email = request.session['amministratore_email']
        amministratore = Amministratore_Clinica.objects.get(email=email)
        return render(request, 'area_riservata_amministratore.html', {'amministratore': amministratore})
    else:
        return redirect('login_amministratore')


#LISTA TRATTAMENTI AMMINISTRATORE
def lista_trattamenti_amministratore(request):
    # Controllo sessione amministratore
    amministratore_email = request.session.get('amministratore_email')
    if not amministratore_email:
        return redirect('login_amministratore')

    # Recupera tutti i trattamenti
    trattamenti = Trattamento.objects.all()

    # Passa i dati al template
    return render(request, 'lista_trattamenti.html', {
        'trattamenti': trattamenti,
        'amministratore_email': amministratore_email
    })

#ELIMINA TRATTAMENTO AMMINISTRATORE
@require_POST
def elimina_trattamento_amministratore(request, trattamento_id):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    # Cerca o restituisce 404
    trattamento = get_object_or_404(Trattamento, id=trattamento_id)
    trattamento.delete()
    messages.success(request, "Trattamento eliminato con successo.")
    return redirect('lista_trattamenti_amministratore')


#AGGIUNGI TRATTAMENTO AMMINISTRATORE
def aggiungi_trattamento_amministratore(request):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    context = {}

    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        costo = request.POST.get('costo')
        note = request.POST.get('note')

        # Campi Ricovero
        data_inizio = request.POST.get('data_inizio')
        data_fine = request.POST.get('data_fine')
        stanza = request.POST.get('stanza')

        # Campo Riabilitazione
        durata = request.POST.get('durata')

        context = {
            'nome': nome,
            'tipo': tipo,
            'costo': costo,
            'note': note,
            'data_inizio': data_inizio,
            'data_fine': data_fine,
            'stanza': stanza,
            'durata': durata,
        }

        try:
            costo_float = float(costo)
        except (ValueError, TypeError):
            context['error'] = "Costo non valido."
            return render(request, 'aggiungi_trattamento.html', context)

        try:
            amministratore = Amministratore_Clinica.objects.get(email=request.session['amministratore_email'])
        except ObjectDoesNotExist:
            return redirect('login_amministratore')

        # Creazione Trattamento base
        trattamento = Trattamento.objects.create(
            nome=nome,
            tipo=tipo,
            costo=costo_float,
            note=note,
            gestore=amministratore
        )

        # Salvataggio dati specifici in base al tipo
        if tipo == "Ricovero":

            trattamento.data_inizio = data_inizio or None
            trattamento.data_fine = data_fine or None
            trattamento.stanza = stanza or ''
            trattamento.save()
        elif tipo == "Riabilitazione":
            # durata come integer
            try:
                durata_int = int(durata) if durata else None
            except ValueError:
                context['error'] = "Durata non valida."
                return render(request, 'aggiungi_trattamento.html', context)

            trattamento.durata = durata_int
            trattamento.save()

        messages.success(request, "Trattamento aggiunto con successo.")
        return redirect('lista_trattamenti_amministratore')

    # Metodo GET: prendi tipo
    context['tipo'] = request.GET.get('tipo', 'Ricovero')

    return render(request, 'aggiungi_trattamento.html', context)

#LISTA EVENTI AMMINISTRATORE
def lista_eventi_amministratore(request):
    # Controllo sessione amministratore
    amministratore_email = request.session.get('amministratore_email')
    if not amministratore_email:
        return redirect('login_amministratore')

    eventi = Evento.objects.all().order_by('data')

    # Aggiungo a ogni evento il numero di iscritti con stato ISCRITTO
    for evento in eventi:
        evento.presenze_effettive = Iscrizione.objects.filter(
            evento=evento,
            stato=Iscrizione.Stato.ISCRITTO
        ).count()

    return render(request, 'lista_eventi.html', {
        'eventi': eventi,
        'amministratore_email': amministratore_email
    })


#ELIMINA EVENTO AMMINISTRATORE
@require_POST
def elimina_evento_amministratore(request, evento_id):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    # Cerca o restituisce 404
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "Evento eliminato con successo.")
    return redirect('lista_eventi_amministratore')


#AGGIUNGI EVENTO AMMINISTRATORE
def aggiungi_evento_amministratore(request):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    if request.method == 'POST':
        titolo = request.POST.get('titolo')
        descrizione = request.POST.get('descrizione')
        data_str = request.POST.get('data')
        presenze_effettive = request.POST.get('presenze_effettive') or 0

        try:
            data = datetime.strptime(data_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Data non valida, deve essere in formato Y-M-D.")
            return render(request, 'aggiungi_evento.html')

        amministratore = Amministratore_Clinica.objects.get(email=request.session['amministratore_email'])

        Evento.objects.create(
            titolo=titolo,
            descrizione=descrizione,
            data=data,
            presenze_effettive=presenze_effettive,

        )

        messages.success(request, "Evento aggiunto con successo.")
        return redirect('lista_eventi_amministratore')

    return render(request, 'aggiungi_evento.html')

#AGGIORNA PRESENZE EVENTO
def aggiorna_presenze(request, evento_id):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    evento = get_object_or_404(Evento, id=evento_id)
    iscrizioni = Iscrizione.objects.filter(evento=evento, stato=Iscrizione.Stato.ISCRITTO)

    if request.method == 'POST':
        presenti_ids = request.POST.getlist('presente')
        for iscrizione in iscrizioni:
            iscrizione.presente = str(iscrizione.id) in presenti_ids
            iscrizione.save()

        messages.success(request, "Presenze aggiornate con successo.")
        return redirect('lista_eventi_amministratore')

    return render(request, 'aggiorna_presenze.html', {
        'evento': evento,
        'iscrizioni': iscrizioni,
    })




#VISUALIZZA EVENTO PERSONALE
def visualizza_eventi_personale(request):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = Personale.objects.filter(email=request.session['personale_email']).first()
    if not personale:
        return redirect('login_personale')

    eventi = Evento.objects.all().order_by('data')


    iscrizioni = Iscrizione.objects.filter(
        personale=personale,
        stato=Iscrizione.Stato.ISCRITTO
    ).values_list('evento_id', flat=True)

    #presenze effettive
    for evento in eventi:
        evento.presenze_effettive = Iscrizione.objects.filter(
            evento=evento,
            stato=Iscrizione.Stato.ISCRITTO
        ).count()

    context = {
        'eventi': eventi,
        'iscrizioni': iscrizioni,
        'personale': personale,
    }

    return render(request, 'visualizza_eventi.html', context)

#ISCRIZIONE EVENTO PERSONALE
@require_POST
def iscrizione_evento_personale(request, evento_id):
    # Verifica login personale tramite sessione
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = Personale.objects.filter(email=request.session['personale_email']).first()
    if not personale:
        return redirect('login_personale')

    evento = get_object_or_404(Evento, id=evento_id)

    # Controlla se è già iscritto
    iscrizione, creata = Iscrizione.objects.get_or_create(
        personale=personale,
        evento=evento,
        defaults={'stato': Iscrizione.Stato.ISCRITTO}
    )

    if not creata:
        # Se l'iscrizione esiste ma non è attiva, aggiorna lo stato
        if iscrizione.stato != Iscrizione.Stato.ISCRITTO:
            iscrizione.stato = Iscrizione.Stato.ISCRITTO
            iscrizione.save()

    return redirect('visualizza_eventi_personale')


#ANNULLA ISCRIZIONE EVENTO PERSONALE
@require_POST
def annulla_iscrizione_evento_personale(request, evento_id):
    # Verifica che il personale sia loggato
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = Personale.objects.filter(email=request.session['personale_email']).first()
    if not personale:
        return redirect('login_personale')

    evento = get_object_or_404(Evento, id=evento_id)

    try:
        iscrizione = Iscrizione.objects.get(personale=personale, evento=evento)
        iscrizione.stato = Iscrizione.Stato.ANNULLATO
        iscrizione.save()
    except Iscrizione.DoesNotExist:
        # Nessuna iscrizione trovata: ignora o gestisci diversamente
        pass

    return redirect('visualizza_eventi_personale')

#CARTELLA CLINICA PERSONALE
def lista_cartelle_personale(request):
    if 'personale_email' not in request.session:
        return redirect('login_personale')
    cartelle = Cartella_Clinica.objects.select_related('paziente', 'trattamento').all()
    return render(request, 'cartelle_personale.html', {'cartelle': cartelle})

#MODIFICA CARTELLA CLINICA
def modifica_cartella_clinica(request, cartella_id):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale_email = request.session['personale_email']
    personale = get_object_or_404(Personale, email=personale_email)

    gestione = Gestione.objects.filter(cartella_id=cartella_id, personale=personale).first()
    if not gestione:
        messages.error(request, "Non sei autorizzato a modificare questa cartella clinica.")
        return redirect('lista_cartelle_personale')

    cartella = get_object_or_404(Cartella_Clinica, id=cartella_id)
    trattamenti = Trattamento.objects.all()

    if request.method == 'POST':
        diagnosi = request.POST.get('diagnosi', '').strip()
        prescrizioni = request.POST.get('prescrizioni', '').strip()
        data_apertura_str = request.POST.get('data_apertura', '').strip()
        data_chiusura_str = request.POST.get('data_chiusura', '').strip()
        trattamento_id = request.POST.get('trattamento')

        if not diagnosi:
            messages.error(request, "La diagnosi è obbligatoria.")
            return render(request, 'modifica_cartella_clinica.html', {'cartella': cartella, 'trattamenti': trattamenti})

        try:
            data_apertura = datetime.strptime(data_apertura_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Data apertura non valida. Usa il formato YYYY-MM-DD.")
            return render(request, 'modifica_cartella_clinica.html', {'cartella': cartella, 'trattamenti': trattamenti})

        data_chiusura = None
        if data_chiusura_str:
            try:
                data_chiusura = datetime.strptime(data_chiusura_str, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, "Data chiusura non valida. Usa il formato YYYY-MM-DD.")
                return render(request, 'modifica_cartella_clinica.html', {'cartella': cartella, 'trattamenti': trattamenti})

        cartella.diagnosi = diagnosi
        cartella.prescrizioni = prescrizioni
        cartella.data_apertura = data_apertura
        cartella.data_chiusura = data_chiusura

        if trattamento_id:
            try:
                trattamento = Trattamento.objects.get(id=trattamento_id)
                cartella.trattamento = trattamento
            except Trattamento.DoesNotExist:
                cartella.trattamento = None
        else:
            cartella.trattamento = None

        cartella.save()
        messages.success(request, "Cartella clinica aggiornata con successo.")
        return redirect('lista_cartelle_personale')

    return render(request, 'modifica_cartella_clinica.html', {'cartella': cartella, 'trattamenti': trattamenti})


#ELIMINA CARTELLA CLINICA
@require_POST
def elimina_cartella_clinica(request, cartella_id):
        if 'personale_email' not in request.session:
            return redirect('login_personale')

        # Recupera il personale corrente
        personale_email = request.session['personale_email']
        personale = get_object_or_404(Personale, email=personale_email)
        # Verifica se il personale è autorizzato a gestire la cartella
        gestione = Gestione.objects.filter(cartella_id=cartella_id, personale=personale).first()
        if not gestione:
            messages.error(request, "Non sei autorizzato a eliminare questa cartella clinica.")
            return redirect('lista_cartelle_personale')
        #elimina la cartella clinica
        cartella = get_object_or_404(Cartella_Clinica, id=cartella_id)
        cartella.delete()
        messages.success(request, "Cartella clinica eliminata con successo.")
        return redirect('lista_cartelle_personale')


#CREA CARTELLA CLINICA
def crea_cartella_clinica(request):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        email = request.POST.get('email')
        data_nascita_str = request.POST.get('data_nascita')
        codice_fiscale = request.POST.get('codice_fiscale')
        cellulare = request.POST.get('cellulare')
        indirizzo = request.POST.get('indirizzo')

        # Validazione data di nascita
        try:
            data_nascita = datetime.strptime(data_nascita_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, "Data di nascita non valida, deve essere nel formato YYYY-MM-DD.")
            return render(request, 'crea_cartella_clinica.html', {'trattamenti': Trattamento.objects.all()})

        # Validazione data apertura cartella
        data_apertura_str = request.POST.get('data_apertura')
        try:
            data_apertura = datetime.strptime(data_apertura_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, "Data di apertura non valida, deve essere nel formato YYYY-MM-DD.")
            return render(request, 'crea_cartella_clinica.html', {'trattamenti': Trattamento.objects.all()})

        # Validazione data chiusura
        data_chiusura_str = request.POST.get('data_chiusura')
        data_chiusura = None
        if data_chiusura_str:
            try:
                data_chiusura = datetime.strptime(data_chiusura_str, '%Y-%m-%d').date()
            except (ValueError, TypeError):
                messages.error(request, "Data di chiusura non valida, deve essere nel formato YYYY-MM-DD.")
                return render(request, 'crea_cartella_clinica.html', {'trattamenti': Trattamento.objects.all()})

            if data_chiusura < data_apertura:
                messages.error(request, "La data di chiusura non può essere precedente alla data di apertura.")
                return render(request, 'crea_cartella_clinica.html', {'trattamenti': Trattamento.objects.all()})

        # Recupera o crea il paziente
        paziente, created = Paziente.objects.get_or_create(
            email=email,
            defaults={
                'nome': nome,
                'cognome': cognome,
                'data_nascita': data_nascita,
                'codice_fiscale': codice_fiscale,
                'cellulare': cellulare,
                'indirizzo': indirizzo,
                # no password
            }
        )

        if not created:
            messages.warning(request, "Attenzione: paziente con questa email già esistente.")

        # Controlla se il paziente ha già una cartella clinica
        if Cartella_Clinica.objects.filter(paziente=paziente).exists():
            messages.error(request, "Questo paziente ha già una cartella clinica.")
            return render(request, 'crea_cartella_clinica.html', {'trattamenti': Trattamento.objects.all()})

        diagnosi = request.POST.get('diagnosi')
        prescrizioni = request.POST.get('prescrizioni', '')
        trattamento_id = request.POST.get('trattamento_id')
        trattamento = None

        if trattamento_id:
            try:
                trattamento = Trattamento.objects.get(id=trattamento_id)
            except Trattamento.DoesNotExist:
                trattamento = None

        # Crea la cartella clinica
        cartella = Cartella_Clinica.objects.create(
            paziente=paziente,
            data_apertura=data_apertura,
            diagnosi=diagnosi,
            prescrizioni=prescrizioni,
            data_chiusura=data_chiusura,
            trattamento=trattamento
        )
        # Collega il personale alla cartella tramite Gestione
        personale_email = request.session['personale_email']
        personale = get_object_or_404(Personale, email=personale_email)
        Gestione.objects.create(cartella=cartella, personale=personale)

        messages.success(request, "Cartella clinica creata con successo.")
        return redirect('lista_cartelle_personale')

    # Se GET, mostra form con tutti i trattamenti
    trattamenti = Trattamento.objects.all()
    return render(request, 'crea_cartella_clinica.html', {'trattamenti': trattamenti})

#CARTELLA CLINICA PAZIENTE
def visualizza_cartella_paziente(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    # Prendi il paziente dalla sessione
    email = request.session['paziente_email']
    paziente = get_object_or_404(Paziente, email=email)

    # Prendi la cartella clinica associata
    try:
        cartella = Cartella_Clinica.objects.get(paziente=paziente)
    except Cartella_Clinica.DoesNotExist:
        messages.info(request, "Non è stata trovata alcuna cartella clinica associata.")
        cartella = None

    # Prendi le prenotazioni completate
    trattamenti_completati = Prenotazione.objects.select_related(
        'trattamento', 'personale'
    ).filter(
        paziente=paziente,
        stato=Prenotazione.Stato.CONFERMATA
    ).order_by('-data', '-ora')

    context = {
        'paziente': paziente,
        'cartella': cartella,
        'trattamenti_completati': trattamenti_completati,
    }

    return render(request, 'cartella_clinica.html', context)


#VISUALIZZA EVENTO PAZIENTE
def visualizza_eventi_paziente(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = Paziente.objects.filter(email=request.session['paziente_email']).first()
    if not paziente:
        return redirect('login_paziente')

    eventi = Evento.objects.all().order_by('data')


    iscrizioni = Iscrizione.objects.filter(
        paziente=paziente,
        stato=Iscrizione.Stato.ISCRITTO
    ).values_list('evento_id', flat=True)

    #presenze effettive
    for evento in eventi:
        evento.presenze_effettive = Iscrizione.objects.filter(
            evento=evento,
            stato=Iscrizione.Stato.ISCRITTO
        ).count()

    context = {
        'eventi': eventi,
        'iscrizioni': iscrizioni,
        'paziente': paziente,
    }

    return render(request, 'visualizza_eventi_paziente.html', context)

#ISCRIZIONE EVENTO PERSONALE
@require_POST
def iscrizione_evento_paziente(request, evento_id):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = Paziente.objects.filter(email=request.session['paziente_email']).first()
    if not paziente:
        return redirect('login_paziente')

    evento = get_object_or_404(Evento, id=evento_id)

    # Controlla se è già iscritto
    iscrizione, creata = Iscrizione.objects.get_or_create(
        paziente=paziente,
        evento=evento,
        defaults={'stato': Iscrizione.Stato.ISCRITTO}
    )

    if not creata:
        # Se l'iscrizione esiste ma non è attiva, aggiorna lo stato
        if iscrizione.stato != Iscrizione.Stato.ISCRITTO:
            iscrizione.stato = Iscrizione.Stato.ISCRITTO
            iscrizione.save()

    return redirect('visualizza_eventi_paziente')


#ANNULLA ISCRIZIONE EVENTO PERSONALE
@require_POST
def annulla_iscrizione_evento_paziente(request, evento_id):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = Paziente.objects.filter(email=request.session['paziente_email']).first()
    if not paziente:
        return redirect('login_paziente')

    evento = get_object_or_404(Evento, id=evento_id)

    try:
        iscrizione = Iscrizione.objects.get(paziente=paziente, evento=evento)
        iscrizione.stato = Iscrizione.Stato.ANNULLATO
        iscrizione.save()
    except Iscrizione.DoesNotExist:
        # Nessuna iscrizione trovata: ignora o gestisci diversamente
        pass

    return redirect('visualizza_eventi_paziente')

#VISUALIZZA PRENOTAZIONI PAZIENTE
def visualizza_prenotazioni_paziente(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])

    prenotazioni_attive = Prenotazione.objects.filter(
        paziente=paziente,
        stato__in=[
            Prenotazione.Stato.RICHIESTA,
            Prenotazione.Stato.CONFERMATA
        ]
    ).order_by('data', 'ora')

    context = {
        'prenotazioni': prenotazioni_attive,
        'paziente': paziente,
    }
    return render(request, 'prenotazioni_paziente.html', context)


#ANNULLA PRENOTAZIONE PAZIENTE
@require_POST
def annulla_prenotazione(request, prenotazione_id):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])

    prenotazione = get_object_or_404(Prenotazione, id=prenotazione_id, paziente=paziente)

    prenotazione.stato = Prenotazione.Stato.CANCELLATA
    prenotazione.save()
    messages.success(request, "Prenotazione annullata con successo.")

    return redirect('visualizza_prenotazioni_paziente')

#CREAZIONE PRENOTAZIONE PAZIENTE
def genera_orari():
    # Genera una lista di orari ogni 30 minuti dalle 8:00 alle 20:00
    orari = []
    start_hour = 8
    end_hour = 20
    for h in range(start_hour, end_hour):
        orari.append(datetime.strptime(f"{h}:00", "%H:%M").time())
        orari.append(datetime.strptime(f"{h}:30", "%H:%M").time())
    return orari

def crea_prenotazione(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])
    trattamenti = Trattamento.objects.all()
    orari_generati = genera_orari()

    if request.method == 'POST':
        data_str = request.POST.get('data')
        ora_str = request.POST.get('ora')
        trattamento_id = request.POST.get('trattamento_id')

        try:
            data = datetime.strptime(data_str, '%Y-%m-%d').date()
            ora = datetime.strptime(ora_str, '%H:%M').time()
        except (ValueError, TypeError):
            messages.error(request, "Data o ora non valida.")
            return render(request, 'prenotazione.html', {
                'paziente': paziente,
                'trattamenti': trattamenti,
                'orari_disponibili': orari_generati
            })

        if data.weekday() == 6:  # Domenica
            messages.error(request, "La clinica è chiusa la domenica.")
            return render(request, 'prenotazione.html', {
                'paziente': paziente,
                'trattamenti': trattamenti,
                'orari_disponibili': orari_generati
            })

        prenotazioni_giorno = Prenotazione.objects.filter(
            data=data,
            stato__in=[Prenotazione.Stato.RICHIESTA, Prenotazione.Stato.CONFERMATA]
        ).values_list('ora', flat=True)

        orari_disponibili = [o for o in orari_generati if o not in prenotazioni_giorno]

        if ora not in orari_disponibili:
            messages.error(request, "Orario non disponibile.")
            return render(request, 'prenotazione.html', {
                'paziente': paziente,
                'trattamenti': trattamenti,
                'orari_disponibili': orari_disponibili
            })

        try:
            trattamento = Trattamento.objects.get(id=trattamento_id)
        except (Trattamento.DoesNotExist, ValueError):
            messages.error(request, "Trattamento non valido.")
            return render(request, 'prenotazione.html', {
                'paziente': paziente,
                'trattamenti': trattamenti,
                'orari_disponibili': orari_disponibili
            })

        # Seleziona personale in base al tipo di trattamento
        if trattamento.tipo == Trattamento.Tipo.RICOVERO:
            personale_disponibile = Personale.objects.filter(
                ruolo=Personale.Ruolo.MEDICO
            ).exclude(
                prenotazione__data=data,
                prenotazione__ora=ora,
                prenotazione__stato__in=[Prenotazione.Stato.RICHIESTA, Prenotazione.Stato.CONFERMATA]
            ).first()

        elif trattamento.tipo == Trattamento.Tipo.RIABILITAZIONE:
            personale_disponibile = Personale.objects.filter(
                ruolo=Personale.Ruolo.OPERATORE_SANITARIO
            ).exclude(
                prenotazione__data=data,
                prenotazione__ora=ora,
                prenotazione__stato__in=[Prenotazione.Stato.RICHIESTA, Prenotazione.Stato.CONFERMATA]
            ).first()

        else:
            personale_disponibile = Personale.objects.exclude(
                prenotazione__data=data,
                prenotazione__ora=ora,
                prenotazione__stato__in=[Prenotazione.Stato.RICHIESTA, Prenotazione.Stato.CONFERMATA]
            ).first()

        if not personale_disponibile:
            messages.error(request, "Nessun personale disponibile a quest'orario.")
            return render(request, 'prenotazione.html', {
                'paziente': paziente,
                'trattamenti': trattamenti,
                'orari_disponibili': orari_disponibili
            })

        Prenotazione.objects.create(
            paziente=paziente,
            trattamento=trattamento,
            data=data,
            ora=ora,
            stato=Prenotazione.Stato.RICHIESTA,
            personale=personale_disponibile
        )

        messages.success(request, "Prenotazione richiesta con successo.")
        return redirect('visualizza_prenotazioni_paziente')

    # Metodo GET
    oggi = datetime.now().date()
    prenotazioni_oggi = Prenotazione.objects.filter(
        data=oggi,
        stato__in=[Prenotazione.Stato.RICHIESTA, Prenotazione.Stato.CONFERMATA]
    ).values_list('ora', flat=True)

    orari_disponibili = [o for o in orari_generati if o not in prenotazioni_oggi]

    return render(request, 'prenotazione.html', {
        'paziente': paziente,
        'trattamenti': trattamenti,
        'orari_disponibili': orari_disponibili
    })

#CREA PDF PRENOTAZIONE
def pdf_prenotazione(request, prenotazione_id):
    prenotazione = get_object_or_404(Prenotazione, id=prenotazione_id)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Riepilogo Prenotazione Clinica Privata «ReViva»")

    p.setFont("Helvetica", 12)
    p.drawString(100, 760, f"Paziente: {prenotazione.paziente.nome} {prenotazione.paziente.cognome}")
    p.drawString(100, 740, f"Data: {prenotazione.data.strftime('%d/%m/%Y')}")
    p.drawString(100, 720, f"Orario: {prenotazione.ora.strftime('%H:%M')}")
    p.drawString(100, 700, f"Trattamento: {prenotazione.trattamento.nome}")
    p.drawString(100, 680, f"Personale assegnato: {prenotazione.personale.nome} {prenotazione.personale.cognome}")

    p.drawString(100, 640, "Grazie per aver scelto la nostra clinica!")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="prenotazione_{prenotazione.id}.pdf"'
    return response



#TRATTAMENTO PAZIENTE RECENSITI
def visualizza_recensioni(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])

    recensioni = Recensione.objects.filter(paziente=paziente).select_related('trattamento')

    return render(request, 'trattamenti_recensiti.html', {'recensioni': recensioni})

#RECENSIONE TRATTAMENTO PAZIENTE
def crea_recensione(request):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])

    # Recupera trattamenti prenotati dal paziente (stato confermato)
    trattamenti_prenotati = Prenotazione.objects.filter(
        paziente=paziente,
        stato=Prenotazione.Stato.CONFERMATA
    ).values_list('trattamento', flat=True).distinct()

    # Recupera trattamenti già recensiti dal paziente
    trattamenti_recensiti = Recensione.objects.filter(
        paziente=paziente
    ).values_list('trattamento', flat=True)

    # Trattamenti prenotati ma non ancora recensiti
    trattamenti_da_recensire = Trattamento.objects.filter(
        id__in=trattamenti_prenotati
    ).exclude(id__in=trattamenti_recensiti)

    if request.method == 'POST':
        trattamento_id = request.POST.get('trattamento_id')
        voto = request.POST.get('voto')
        commento = request.POST.get('commento')

        try:
            trattamento = trattamenti_da_recensire.get(id=trattamento_id)
        except Trattamento.DoesNotExist:
            messages.error(request, "Trattamento non valido o già recensito.")
            return render(request, 'recensione.html', {'trattamenti': trattamenti_da_recensire})

        try:
            voto = int(voto)
            if voto < 1 or voto > 5:
                raise ValueError
        except ValueError:
            messages.error(request, "Inserisci un voto valido da 1 a 5.")
            return render(request, 'recensione.html', {'trattamenti': trattamenti_da_recensire})

        Recensione.objects.create(
            paziente=paziente,
            trattamento=trattamento,
            valutazione=voto,
            testo=commento
        )
        messages.success(request, "Recensione salvata con successo.")
        return redirect('trattamenti_recensiti')

    return render(request, 'recensione.html', {'trattamenti': trattamenti_da_recensire})


#ELIMINA RECENSION EPAZIENTE
@require_POST
def elimina_recensione_paziente(request, recensione_id):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    paziente = get_object_or_404(Paziente, email=request.session['paziente_email'])
    recensione = get_object_or_404(Recensione, id=recensione_id, paziente=paziente)

    recensione.delete()
    messages.success(request, "Recensione eliminata con successo.")
    return redirect('trattamenti_recensiti')


#CONFERMA PRENOTAZIONE PERSONALE
def conferma_visita(request, prenotazione_id):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = get_object_or_404(Personale, email=request.session['personale_email'])
    prenotazione = get_object_or_404(Prenotazione, id=prenotazione_id, personale=personale)

    if not prenotazione.trattamento:
        messages.error(request, "Prenotazione senza trattamento associato.")
        return redirect('visualizza_prenotazioni_personale')

    trattamento = prenotazione.trattamento

    if request.method == 'POST':
        # Aggiorna i campi modificabili del trattamento
        trattamento.note = request.POST.get('note', trattamento.note)
        trattamento.data_inizio = request.POST.get('data_inizio', trattamento.data_inizio) or None
        trattamento.data_fine = request.POST.get('data_fine', trattamento.data_fine) or None
        trattamento.stanza = request.POST.get('stanza', trattamento.stanza)
        durata = request.POST.get('durata')
        trattamento.durata = int(durata) if durata and durata.isdigit() else trattamento.durata
        trattamento.save()

        # Conferma prenotazione
        prenotazione.stato = Prenotazione.Stato.CONFERMATA
        prenotazione.save()

        # Crea svolgimento solo se non esiste già
        if not Svolgimento.objects.filter(personale=personale, trattamento=trattamento).exists():
            Svolgimento.objects.create(personale=personale, trattamento=trattamento)

        messages.success(request, "Visita confermata e trattamento aggiornato.")
        return redirect('visualizza_prenotazioni_personale')

    # GET: mostra form con i dati correnti del trattamento
    return render(request, 'conferma_visita.html', {
        'prenotazione': prenotazione,
        'trattamento': trattamento,
    })


#VISUALIZZA PRENOTAZIONI PERSONALE

def visualizza_prenotazioni_personale(request):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = get_object_or_404(Personale, email=request.session['personale_email'])

    prenotazioni = Prenotazione.objects.filter(personale=personale).order_by('data', 'ora')

    return render(request, 'prenotazioni_personale.html', {
        'personale': personale,
        'prenotazioni': prenotazioni
    })


#ANNULLA PRENOTAZIONE PERSONALE
def annulla_conferma_visita(request, prenotazione_id):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    personale = get_object_or_404(Personale, email=request.session['personale_email'])
    prenotazione = get_object_or_404(Prenotazione, id=prenotazione_id, personale=personale)

    if prenotazione.stato == Prenotazione.Stato.CONFERMATA:
        prenotazione.stato = Prenotazione.Stato.RICHIESTA  # o lo stato iniziale che usi
        prenotazione.save()


        Svolgimento.objects.filter(personale=personale, trattamento=prenotazione.trattamento).delete()

        messages.success(request, "Conferma della visita annullata.")
    else:
        messages.info(request, "La visita non è confermata, quindi non può essere annullata.")

    return redirect('visualizza_prenotazioni_personale')

"""
#LOGIN VULNERABILE
@csrf_exempt
def login_vulnerabile_paziente(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        #query SQL vulnerabile
        query = f"SELECT * FROM clinica_paziente WHERE email = '{email}' AND password = '{password}'"

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
        if row:
            return render(request, 'area_riservata_paziente.html', {'paziente':row})
        else:
            return render(request, 'login_vulnerabile_paziente.html', {'error': 'Credenziali non valide.'})
    else:
        return render(request, 'login_vulnerabile_paziente.html')
"""

def trattamenti_prenotati_amministratore(request):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    svolgimenti = Svolgimento.objects.select_related('trattamento', 'personale')
    prenotazioni = Prenotazione.objects.filter(stato__in=['confermata']).select_related('paziente', 'trattamento')


    dati = []
    for prenotazione in prenotazioni:
        # Cerca chi svolge il trattamento
        svolgente = svolgimenti.filter(trattamento=prenotazione.trattamento).first()
        if svolgente:
            dati.append({
                'trattamento_nome': prenotazione.trattamento.nome,
                'paziente': f"{prenotazione.paziente.nome} {prenotazione.paziente.cognome}",
                'personale': f"{svolgente.personale.nome} {svolgente.personale.cognome}",
                'data': prenotazione.data,
                'ora': prenotazione.ora,
                'tipo': prenotazione.trattamento.tipo,
                'stato': prenotazione.stato,
            })
#visualizza solo le prenotazioni confermate
    return render(request, 'trattamenti_prenotati_amministratore.html', {'dati': dati})