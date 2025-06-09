from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django_mysql.models import EnumField
from django.utils import timezone
from django.contrib.auth.models import User


class Paziente(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    #emailfield verifica che l'indirizzo ha tutti i requisiti di un email valido
    #unique serve per non avere indirizzi duplicati
    password = models.CharField(max_length=128, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    cognome = models.CharField(max_length=100, blank=False, null=False)
    codice_fiscale = models.CharField(max_length=16, validators=[MinLengthValidator(16)], unique=True, blank=False, null=False)
    #codice fiscale deve avere 16 caratteri

    patologie = models.TextField(null=True)
    allergie = models.TextField(null=True)
    cellulare = models.CharField(max_length=20, null=False, blank=False)
    indirizzo = models.CharField(max_length=255, null=False, blank=False)
    data_nascita = models.DateField(null=False, blank=False)



class Personale(models.Model):
    class Ruolo(models.TextChoices):
        MEDICO = 'Medico'
        OPERATORE_SANITARIO = 'Operatore Sanitario'

    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    ruolo = EnumField(choices=Ruolo.choices, default=Ruolo.MEDICO)
    codice_fiscale = models.CharField(max_length=16, validators=[MinLengthValidator(16)],
                                      unique=True, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    cognome = models.CharField(max_length=100, blank=False, null=False)
    data_nascita = models.DateField(null=False, blank=False)
    orario_lavoro = models.CharField(max_length=100, blank=False)
    cellulare = models.CharField(max_length=20, null=False, blank=False)

    # Campi specifici
    specializzazione = models.CharField(max_length=100, blank=True, null=True) # Solo per medici
    reparto = models.CharField(max_length=100, blank=True, null=True) # Solo per medici
    qualifica = models.CharField(max_length=100, blank=True, null=True) # Solo per operatori sanitari
    mansione = models.CharField(max_length=100, blank=True, null=True)# Solo per operatori sanitari


class Cartella_Clinica(models.Model):
    paziente = models.OneToOneField(Paziente, on_delete=models.CASCADE)
    #onetoonefield crea una relazione uno a uno tra paziente e cartella clinica, solo un paziente alla volta identifica
    #cascade significa che se il paziente viene eliminato, anche la cartella clinica viene eliminata

    data_apertura = models.DateField(null=False, blank=False)
    diagnosi = models.TextField(null=False, blank=False)
    prescrizioni = models.TextField(null=True, blank=True)
    trattamento = models.ForeignKey('Trattamento', on_delete=models.SET_NULL, null=True, blank=True)
    data_chiusura = models.DateField(blank=True, null=True)

class Amministratore_Clinica(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    codice_fiscale = models.CharField(max_length=16, unique=True, validators=[MinLengthValidator(16)])
    cellulare = models.CharField(max_length=20)
    data_nascita = models.DateField()


class Trattamento(models.Model):
    class Tipo(models.TextChoices):
        RICOVERO = 'Ricovero'
        RIABILITAZIONE = 'Riabilitazione'

    nome = models.CharField(max_length=100, default="")
    tipo = EnumField(choices=Tipo.choices, default=Tipo.RICOVERO)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=True, blank=True)
    costo = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    note = models.TextField(blank=True, null=True)
    gestore = models.ForeignKey(Amministratore_Clinica, on_delete=models.SET_NULL, null=True, blank=True)
    # Ricovero
    data_inizio = models.DateField(blank=True, null=True)
    data_fine = models.DateField(blank=True, null=True)
    stanza = models.CharField(max_length=10, blank=True, null=True)

    # Riabilitazione
    durata = models.IntegerField(blank=True, null=True)



class Prenotazione(models.Model):
    class Stato(models.TextChoices):
        RICHIESTA = 'richiesta', 'Richiesta'
        CONFERMATA = 'confermata', 'Confermata'
        CANCELLATA = 'cancellata', 'Cancellata'
        #MODIFICATA = 'modificata', 'Modificata'

    data = models.DateField()
    ora = models.TimeField()
    durata = models.PositiveIntegerField(default=30)#in minuti
    stato = models.CharField(max_length=30, choices=Stato.choices, default=Stato.RICHIESTA)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE)
    personale = models.ForeignKey(Personale, on_delete=models.SET_NULL, null=True)
    trattamento = models.ForeignKey(Trattamento, on_delete=models.CASCADE, null=False, blank=False)


class Evento(models.Model):
    data = models.DateField()
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField()
    presenze_effettive = models.IntegerField(default=0)



class Iscrizione(models.Model):
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=True, blank=True)
    personale = models.ForeignKey(Personale, on_delete=models.SET_NULL, null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_iscrizione = models.DateField(auto_now_add=True) # Data di iscrizione automatica quando si clicca
    presente = models.BooleanField(default=False)

    class Stato(models.TextChoices):
        ISCRITTO = 'iscritto', 'Iscritto'
        ANNULLATO = 'annullato', 'Annullato'
        #IN_ATTESA = 'in_attesa', 'In attesa'

    stato = models.CharField(max_length=50, choices=Stato.choices, default=Stato.ISCRITTO)



class Recensione(models.Model):
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE)
    trattamento = models.ForeignKey(Trattamento, on_delete=models.CASCADE)
    testo = models.TextField()
    valutazione = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class Gestione(models.Model):
    cartella = models.ForeignKey(Cartella_Clinica, on_delete=models.CASCADE)
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)


class Svolgimento(models.Model):
    trattamento = models.ForeignKey(Trattamento, on_delete=models.CASCADE)
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)

