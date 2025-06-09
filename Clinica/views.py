import hashlib
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from Clinica.models import Evento, Paziente, Personale, Amministratore_Clinica, Trattamento, Iscrizione, \
    Cartella_Clinica
from django.views.decorators.http import require_POST
from functools import wraps
from django.contrib import messages
from decimal import Decimal



# PAGINA INIZIALE
def pagina_iniziale(request):
    return render(request, "pagina_iniziale.html")


# EVENTI
def evento(request):
    eventi = Evento.objects.all().order_by('data')
    return render(request, 'eventi.html', {'eventi': eventi})


#AREA PRIVATA
def area_privata(request):
    return render(request, 'area_privata.html')


#AUTENTICAZIONE CLIENTE, PERSONALE E AMMINISTRATORE
def authenticated_paziente(email, password):
    return Paziente.objects.filter(email=email, password=password).exists()

def authenticated_personale(email, password):
    return Personale.objects.filter(email=email, password=password).exists()

def authenticated_amministratore(email, password):
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
        #poichè deve essere y/m/d e il browser la da in g/m/a devo:
        try:
            data_nascita = datetime.strptime(data_nascita_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'registrazione_paziente.html', {
                'error_message': "Data non valida deve essere in formato Y-M-D"
            })

        # print(email," : ", hashed_password)
        if Paziente.objects.filter(email=email).exists():
            return render(request, 'registrazione_paziente.html', {'error_message': "Email già in uso"})
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
                'success_message': "Registrazione avvenuta con successo",
                'paziente': paziente
            })
    else:
        return render(request, 'registrazione_paziente.html', {'error_message': "Metodo non valido"})


#LOGIN PAZIENTE
def login_paziente(request):
    next_url = request.GET.get('next', '') if request.method == 'GET' else request.POST.get('next', '')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if authenticated_paziente(email, hashed_password):
            # Salva email
            request.session['paziente_email'] = email
            # Redirect a next_url se presente, altrimenti a area_riservata
            if next_url:
                return redirect(next_url)
            else:
                return redirect('area_riservata_paziente')
        else:
            return render(request, 'login_paziente.html', {
                'error': "Credenziali non valide, riprova",
                'email': email,
                'next': next_url,
            })
    else:
        return render(request, 'login_paziente.html', {'next': next_url})

#LOGIN PERSONALE
def login_personale(request):
    next_url = request.GET.get('next', '') if request.method == 'GET' else request.POST.get('next', '')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if authenticated_personale(email, hashed_password):
            # Salva l'email nella sessione
            request.session['personale_email'] = email
            # Redirect a next_url se presente, altrimenti a area_riservata_personale
            if next_url:
                return redirect(next_url)
            else:
                return redirect('area_riservata_personale')
        else:
            return render(request, 'login_personale.html', {
                'error': "Credenziali non valide, riprova",
                'email': email,
                'next': next_url,
            })
    else:
        return render(request, 'login_personale.html', {'next': next_url})


#LOGIN AMMINISTRATORE
def login_amministratore(request):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            #print("EMAIL:", email)
           # print("HASHED PASSWORD:", hashed_password)

            if authenticated_amministratore(email, hashed_password):
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

"""#SESSIONE
def login_required_multi(user_types):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            for user_type in user_types:
                session_key = f"{user_type}_email"
                if request.session.get(session_key):
                    request.user_type = user_type
                    return view_func(request, *args, **kwargs)
            return redirect('scegli_login')
        return _wrapped_view
    return decorator


#  AREA RISERVATA
@login_required_multi(['paziente', 'personale', 'amministratore'])
def area_riservata(request):
    user_type = getattr(request, 'user_type', None)

    if user_type == 'paziente':
        email = request.session.get('paziente_email')
        utente = get_object_or_404(Paziente, email=email)
        template = 'area_riservata_paziente.html'
        context = {'paziente': utente}

    elif user_type == 'personale':
        email = request.session.get('personale_email')
        utente = get_object_or_404(Personale, email=email)
        template = 'area_riservata_personale.html'
        context = {'personale': utente}

    elif user_type == 'amministratore':
        email = request.session.get('amministratore_email')
        utente = get_object_or_404(Amministratore_Clinica, email=email)
        template = 'area_riservata_amministratore.html'
        context = {'amministratore': utente}

    else:
        return redirect('scegli_login')

    return render(request, template, context)

"""

#AREA RISERVATA
def area_riservata_paziente(request):
    # Controllo che il paziente sia loggato (sessione valida)
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    email = request.session['paziente_email']

    # Recupera i dati del paziente dal database usando l'email
    paziente = get_object_or_404(Paziente, email=email)

    # Passa i dati paziente al template
    context = {
        'paziente': paziente
    }

    return render(request, 'area_riservata_paziente.html', context)

def area_riservata_personale(request):
    if 'personale_email' not in request.session:
        return redirect('login_personale')

    email = request.session['personale_email']
    personale = get_object_or_404(Personale, email=email)
    context = {
        'personale': personale
    }

    return render(request, 'area_riservata_personale.html', context)

def area_riservata_amministratore(request):
    if 'amministratore_email' not in request.session:
        return redirect('login_amministratore')

    email = request.session['amministratore_email']
    amministratore = get_object_or_404(Amministratore_Clinica, email=email)
    context = {'amministratore': amministratore}
    return render(request, 'area_riservata_amministratore.html', context)

# LOGOUT
def logout_paziente(request):
    try:
        del request.session['paziente_email']
    except KeyError:
        pass
    return redirect('pagina_iniziale')



def logout_personale(request):
    try:
        del request.session['personale_email']
    except KeyError:
        pass
    return redirect('pagina_iniziale')

def logout_amministratore(request):
    try:
        del request.session['amministratore_email']
    except KeyError:
        pass
    return redirect('pagina_iniziale')


"""def logout(request):
        request.session.flush()
        messages.success(request, "Logout effettuato con successo.")
        return redirect('pagina_iniziale')
"""

#EVENTI IN ALTO
def lista_eventi(request):
    eventi = Evento.objects.all().order_by('data')
    return render(request, 'eventi.html', {
        'eventi': eventi,
    })

#VISUALIZZA EVENTI
#@login_required_multi(['paziente', 'personale'])
def visualizza_eventi(request):
    eventi = Evento.objects.all().order_by('data')

    paziente = None
    personale = None

    if 'paziente_email' in request.session:
        paziente = Paziente.objects.filter(email=request.session['paziente_email']).first()
    elif 'personale_email' in request.session:
        personale = Personale.objects.filter(email=request.session['personale_email']).first()

    if not paziente and not personale:
        # Utente non loggato → redirect al login
        return redirect('scegli_login')

    # Recupera iscrizioni per questo utente
    iscrizioni = Iscrizione.objects.filter(
        Q(paziente=paziente) | Q(personale=personale),
        stato=Iscrizione.Stato.ISCRITTO
    ).values_list('evento_id', flat=True)

    context = {
        'eventi': eventi,
        'iscrizioni': iscrizioni,
    }

    return render(request, 'visualizza_eventi.html', context)




#ISCRIZIONE EVENTO

@require_POST
def iscrizione_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    print(f"Evento: {evento}")

    paziente = None
    personale = None

    if 'paziente_email' in request.session:
        email = request.session['paziente_email']
        print(f"Session paziente_email: {email}")
        paziente = get_object_or_404(Paziente, email=email)
    elif 'personale_email' in request.session:
        email = request.session['personale_email']
        print(f"Session personale_email: {email}")
        personale = get_object_or_404(Personale, email=email)
    else:
        print("Utente non loggato, redirect a scegli_login")
        request.session['next'] = request.path
        return redirect('scegli_login')

    if paziente:
        print(f"Iscrizione paziente: {paziente}")
        iscrizione_esiste = Iscrizione.objects.filter(
            evento=evento,
            paziente=paziente,
            stato=Iscrizione.Stato.ISCRITTO
        ).exists()
        print(f"Iscrizione esistente paziente: {iscrizione_esiste}")
        if not iscrizione_esiste:
            Iscrizione.objects.create(
                evento=evento,
                paziente=paziente,
                personale=None,
                stato=Iscrizione.Stato.ISCRITTO
            )
            print("Iscrizione paziente creata")
    elif personale:
        print(f"Iscrizione personale: {personale}")
        iscrizione_esiste = Iscrizione.objects.filter(
            evento=evento,
            personale=personale,
            stato=Iscrizione.Stato.ISCRITTO
        ).exists()
        print(f"Iscrizione esistente personale: {iscrizione_esiste}")
        if not iscrizione_esiste:
            Iscrizione.objects.create(
                evento=evento,
                paziente=None,
                personale=personale,
                stato=Iscrizione.Stato.ISCRITTO
            )
            print("Iscrizione personale creata")

    evento.presenze_effettive = Iscrizione.objects.filter(
        evento=evento,
        stato=Iscrizione.Stato.ISCRITTO
    ).count()
    evento.save()
    print(f"Presenze aggiornate: {evento.presenze_effettive}")

    return redirect('visualizza_eventi')

@require_POST
def annulla_iscrizione_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    paziente = None
    personale = None

    if 'paziente_email' in request.session:
        email = request.session['paziente_email']
        paziente = get_object_or_404(Paziente, email=email)
    elif 'personale_email' in request.session:
        email = request.session['personale_email']
        personale = get_object_or_404(Personale, email=email)
    else:
        return redirect('scegli_login')

    # Annulla iscrizione se esistente
    if paziente:
        Iscrizione.objects.filter(evento=evento, paziente=paziente).delete()
    elif personale:
        Iscrizione.objects.filter(evento=evento, personale=personale).delete()

    # Aggiorna il numero di presenze
    evento.presenze_effettive = Iscrizione.objects.filter(
        evento=evento, stato=Iscrizione.Stato.ISCRITTO
    ).count()
    evento.save()

    return redirect('visualizza_eventi')

"""
def iscrizione_evento(request, evento_id):
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    email = request.session['paziente_email']

    paziente = get_object_or_404(Paziente, email=email)
    # Recupera l'evento
    evento = get_object_or_404(Evento, pk=evento_id)

    # Controlla se è già iscritto
    iscrizione_esiste = Iscrizione.objects.filter(paziente=paziente, evento=evento).exists()
    if not iscrizione_esiste:
        Iscrizione.objects.create(paziente=paziente, evento=evento)

    # Dopo l'iscrizione, reindirizza alla lista eventi (o altra pagina)
    return redirect('visualizza_eventi')

"""

"""
#@login_required_multi(['paziente', 'personale'])
@require_POST
def iscrizione_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    paziente = None
    personale = None

    if 'paziente_email' in request.session:
        email = request.session['paziente_email']
        paziente = get_object_or_404(Paziente, email=email)
        print(f"Iscrizione per paziente: {email}")
    elif 'personale_email' in request.session:
        email = request.session['personale_email']
        personale = get_object_or_404(Personale, email=email)
        print(f"Iscrizione per personale: {email}")
    else:
        print("Utente non loggato, redirect a scegli_login")
        #return redirect(f"{reverse('scegli_login')}?next={request.path}")

    # Controllo iscrizione esistente a seconda del tipo
    if paziente:
        iscrizione_esistente = Iscrizione.objects.filter(
            evento=evento,
            paziente=paziente,
            stato=Iscrizione.Stato.ISCRITTO
        ).exists()
        print(f"Iscrizione esistente paziente: {iscrizione_esistente}")
        if not iscrizione_esistente:
            Iscrizione.objects.create(
                evento=evento,
                paziente=paziente,
                personale=None,
                stato=Iscrizione.Stato.ISCRITTO
            )
    elif personale:
        iscrizione_esistente = Iscrizione.objects.filter(
            evento=evento,
            personale=personale,
            stato=Iscrizione.Stato.ISCRITTO
        ).exists()
        print(f"Iscrizione esistente personale: {iscrizione_esistente}")
        if not iscrizione_esistente:
            Iscrizione.objects.create(
                evento=evento,
                paziente=None,
                personale=personale,
                stato=Iscrizione.Stato.ISCRITTO
            )

    # Aggiorna presenze effettive
    evento.presenze_effettive = Iscrizione.objects.filter(evento=evento, stato=Iscrizione.Stato.ISCRITTO).count()
    evento.save()
    print(f"Presenze aggiornate a: {evento.presenze_effettive}")

    return redirect('visualizza_eventi')
"""





def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('amministratore_email'):
            return redirect('login_amministratore')
        return view_func(request, *args, **kwargs)
    return wrapper


@admin_required
def lista_trattamenti(request):
    trattamenti = Trattamento.objects.all().order_by('nome')  # o come preferisci ordinarli
    return render(request, 'lista_trattamenti.html', {
        'trattamenti': trattamenti,
    })

@admin_required
def aggiungi_trattamento(request):
    error = None
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        tipo = request.POST.get('tipo', '').strip()
        tipo_lower = tipo.lower()
        costo = request.POST.get('costo', '').strip()
        durata = request.POST.get('durata', '').strip()
        data_inizio = request.POST.get('data_inizio', '').strip()
        data_fine = request.POST.get('data_fine', '').strip()
        stanza = request.POST.get('stanza', '').strip()

        if not nome or not tipo or not costo:
            error = 'Nome, tipo e costo sono obbligatori.'
        elif tipo_lower not in ['ricovero', 'riabilitazione']:
            error = 'Tipo non valido.'
        else:
            try:
                costo_val = float(costo)
                if costo_val < 0:
                    error = 'Costo deve essere positivo.'
            except ValueError:
                error = 'Costo deve essere un numero.'

            durata_val = None
            if tipo_lower == 'riabilitazione':
                if not durata:
                    error = 'Durata è obbligatoria per riabilitazione.'
                else:
                    try:
                        durata_val = int(durata)
                        if durata_val <= 0:
                            error = 'Durata deve essere un numero positivo.'
                    except ValueError:
                        error = 'Durata deve essere un numero intero.'

        if not error:
            # Salvataggio, considera che il modello Trattamento deve avere questi campi
            trattamento = Trattamento(
                nome=nome,
                tipo=tipo,
                costo=costo_val,
                durata=durata_val if tipo_lower == 'riabilitazione' else None,
                data_inizio=data_inizio if tipo_lower == 'ricovero' else None,
                data_fine=data_fine if tipo_lower == 'ricovero' else None,
                stanza=stanza if tipo_lower == 'ricovero' else None,
                note=request.POST.get('note', '').strip(),
            )
            trattamento.save()
            return redirect('lista_trattamenti')

    else:
        nome = tipo = costo = durata = data_inizio = data_fine = stanza = ''

    return render(request, 'aggiungi_trattamento.html', {
        'error': error,
        'nome': nome,
        'tipo': tipo,
        'costo': costo,
        'durata': durata,
        'data_inizio': data_inizio,
        'data_fine': data_fine,
        'stanza': stanza,
    })


@admin_required
def elimina_trattamento(request, pk):
    if request.method == 'POST':
        trattamento = get_object_or_404(Trattamento, pk=pk)
        trattamento.delete()
    return redirect('lista_trattamenti')



#TRATTAMENTI
def gestione_trattamenti(request):
    if request.method == "POST":
        if "aggiungi" in request.POST:
            nome = request.POST.get("nome")
            tipo_str = request.POST.get("tipo")  # stringa da form, es 'Ricovero'
            costo_str = request.POST.get("costo")
            note = request.POST.get("note")
            durata_str = request.POST.get("durata")
            data_inizio_str = request.POST.get("data_inizio")
            data_fine_str = request.POST.get("data_fine")
            stanza = request.POST.get("stanza")

            costo = Decimal(costo_str) if costo_str else Decimal('0.00')
            durata = int(durata_str) if durata_str else None
            data_inizio = datetime.strptime(data_inizio_str, '%Y-%m-%d').date() if data_inizio_str else None
            data_fine = datetime.strptime(data_fine_str, '%Y-%m-%d').date() if data_fine_str else None

            # Converti stringa a enum
            tipo_enum = Trattamento.Tipo(tipo_str)

            trattamento = Trattamento(
                nome=nome,
                tipo=tipo_enum,
                costo=costo,
                note=note
            )

            if tipo_enum == Trattamento.Tipo.RICOVERO:
                trattamento.data_inizio = data_inizio
                trattamento.data_fine = data_fine
                trattamento.stanza = stanza
            elif tipo_enum == Trattamento.Tipo.RIABILITAZIONE:
                trattamento.durata = durata

            trattamento.save()

        elif "elimina" in request.POST:
            trattamento_id = request.POST.get("trattamento_id")
            Trattamento.objects.filter(id=trattamento_id).delete()

        return redirect('gestione_trattamenti')

    trattamenti = Trattamento.objects.all()
    return render(request, "area_riservata_amministratore.html", {
        "trattamenti": trattamenti,
        "tipi": Trattamento.Tipo.choices
    })

def cartella_clinica(request):
    # Controllo che il paziente sia loggato (sessione valida)
    if 'paziente_email' not in request.session:
        return redirect('login_paziente')

    email = request.session['paziente_email']

    paziente = get_object_or_404(Paziente, email=email)
    cartella = get_object_or_404(Cartella_Clinica, paziente=paziente)

    context = {
        'paziente': paziente,
        'cartella': cartella,
    }

    return render(request, 'cartella_clinica.html', context)

"""



#ISCRIZIONE EVENTO
@login_required
def iscrizione_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    # Supponiamo che il paziente sia collegato all’utente loggato
    paziente = getattr(request.user, 'paziente', None)

    if not paziente:
        # Se l’utente non è un paziente, redirigi o mostra errore
        return redirect('login_paziente')

    # Controlla se è già iscritto
    iscrizione_esistente = Iscrizione.objects.filter(paziente=paziente, evento=evento).exists()

    if not iscrizione_esistente:
        # Crea l’iscrizione
        Iscrizione.objects.create(paziente=paziente, evento=evento)
        # Aumenta presenze_effettive o gestisci come vuoi
        evento.presenze_effettive += 1
        evento.save()
        # Messaggio di successo o redirect
        return render(request, 'iscrizione_successo.html', {'evento': evento})
    else:
        # Messaggio di errore o redirect
        return render(request, 'iscrizione_gia_effettuata.html', {'evento': evento})


def annulla_iscrizione_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    paziente = getattr(request.user, 'paziente', None)

    if not paziente:
        return redirect('login_paziente')

    iscrizione = Iscrizione.objects.filter(paziente=paziente, evento=evento).first()
    if iscrizione:
        iscrizione.delete()
        # Aggiorna presenze effettive
        if evento.presenze_effettive > 0:
            evento.presenze_effettive -= 1
            evento.save()
        return render(request, 'annulla_iscrizione_successo.html', {'evento': evento})
    else:
        return render(request, 'annulla_iscrizione_non_trovata.html', {'evento': evento})



def cartella_clinica(request):
        # Recupera il paziente associato all'utente loggato
        paziente = get_object_or_404(Paziente, user=request.user)

        # Recupera la cartella clinica del paziente
        cartella = get_object_or_404(Cartella_Clinica, paziente=paziente)

        context = {
            'paziente': paziente,
            'cartella': cartella,
        }

        return render(request, 'cartella_clinica.html', context)


#Lista dei trattamenti conclusi che il paziente può recensire
def trattamenti_recensibili(request):
    paziente = Paziente.objects.get(user=request.user)
    trattamenti_conclusi = Trattamento.objects.filter(
        paziente=paziente,
        data_fine__isnull=False,
        data_fine__lte=timezone.now().date()
    ).exclude(
        recensione__isnull=False
    )

    return render(request, "recensione_da_fare.html", {
        "trattamenti": trattamenti_conclusi
    })


#Inserire una recensione
def lascia_recensione(request):
    paziente = Paziente.objects.get(user=request.user)

    if request.method == 'POST':
        form = RecensioneForm(request.POST, paziente=paziente)
        if form.is_valid():
            recensione = form.save(commit=False)
            recensione.paziente = paziente
            recensione.save()
            return redirect('trattamenti_recensibili')
    else:
        form = RecensioneForm(paziente=paziente)

    return render(request, 'lascia_recensione.html', {'form': form})


@login_required
def crea_prenotazione(request):
    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        if form.is_valid():
            prenotazione = form.save(commit=False)
            prenotazione.paziente = request.user.paziente  # Assumendo che l'utente abbia un profilo Paziente
            prenotazione.stato = 'richiesta'
            try:
                prenotazione.clean()  # Chiama il controllo sovrapposizioni
                prenotazione.save()
                messages.success(request, "Prenotazione creata con successo.")
                return redirect('lista_prenotazioni')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = PrenotazioneForm()

    return render(request, 'prenotazione.html', {'form': form})




@login_required
def cartelle_personale_view(request):
    try:
        personale = request.user.personale
    except Personale.DoesNotExist:
        return HttpResponseForbidden("Non sei autorizzato a vedere questa pagina.")

    if personale.ruolo not in [personale.Ruolo.MEDICO, personale.Ruolo.OPERATORE_SANITARIO]:
        return HttpResponseForbidden("Accesso negato: solo personale medico e operatori sanitari possono accedere.")

    cartelle = personale.get_cartelle_cliniche()
    return render(request, 'cartelle_personale.html', {'cartelle': cartelle})

"""