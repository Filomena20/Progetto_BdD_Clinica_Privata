
# **Sistema Informativo – Clinica Privata “ReViva”**
Questo lavoro nasce con l’obiettivo di progettare e implementare un sistema informativo moderno per la clinica privata **ReViva**, specializzata in ricoveri e trattamenti riabilitativi.  
L’intento è quello di **sostituire le attuali procedure cartacee** con un’applicazione web intuitiva, capace di supportare il personale medico e amministrativo nella gestione quotidiana della struttura, migliorando **efficienza, sicurezza e accessibilità** ai dati sanitari.

---

## **Indice**
1. [Obiettivo del Sistema](#obiettivo-del-sistema)  
2. [Tecnologie Utilizzate](#tecnologie-utilizzate)  
3. [Installazione](#installazione)  
4. [Configurazione del Database](#configurazione-del-database)  
5. [Utilizzo](#utilizzo)  
6. [Licenza](#licenza)  

---

## **Obiettivo del Sistema**
La piattaforma è progettata per rispondere in modo flessibile e modulare alle esigenze operative della clinica, offrendo funzionalità quali:
- **Gestione centralizzata dei pazienti**, con storico clinico, allergie, patologie e trattamenti ricevuti.
- **Cartelle cliniche elettroniche**, accessibili sia dal personale sanitario che dai pazienti.
- **Prenotazione e gestione degli appuntamenti**, con visibilità sulla disponibilità del personale.
- **Organizzazione di eventi sanitari e formativi**, aperti al pubblico o riservati al personale.
- **Recensioni dei pazienti** sui trattamenti ricevuti.
- **Interfaccia differenziata** per visitatori, pazienti, personale sanitario e amministratori, ciascuno con accesso a funzionalità specifiche.  

L'architettura basata sui ruoli **garantisce sicurezza e controllo degli accessi**, oltre a offrire un’esperienza utente personalizzata.

---

## **Tecnologie Utilizzate**
### **Backend**
- **Python** – Linguaggio di programmazione principale.
- **Django** – Framework web per la logica server-side.
- **mysqlclient** – Libreria per collegare Django a MySQL/MariaDB.  

### **Database**
- **MariaDB / MySQL** – Database relazionale esterno, gestito tramite phpMyAdmin per facilitare l’inserimento e gestione dei dati.  

### **Frontend**
- **HTML / CSS** – Utilizzati per l’interfaccia utente.  

### **Modellazione Dati**
- **Modello E/R** progettato con generalizzazioni disgiunte e totali, garantendo una **struttura dati coerente e scalabile**.  
![Modello_E/R](https://github.com/user-attachments/assets/e435b765-9129-4f98-aca5-bac7ef4a4404)

---

## **Installazione**
Per eseguire l’applicazione, è necessario:  
1. **Avere Python installato** nel proprio ambiente.  
2. **Avere accesso a un server MySQL/MariaDB**, preferibilmente con phpMyAdmin.  
3. **Clonare il progetto** nella propria directory locale.  
```
git clone https://github.com/tuo-utente/reviva-clinica.git
cd clinica
```
4. **Installare i pacchetti richiesti** eseguendo:  
```bash
   pip install django
   pip install mysqlclient
```
---

## **Configurazione del Database**
All’interno del file settings.py del progetto Django, è necessario configurare correttamente la connessione al database MySQL/MariaDB. I parametri da inserire sono:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_database',
        'USER': 'nome_utente',
        'PASSWORD': ‘ ’,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Il database può essere creato preventivamente via phpMyAdmin o tramite terminale, prima di eseguire le migrazioni.

---

## **Utilizzo**
Dopo la configurazione, eseguire i seguenti comandi da terminale per applicare le migrazioni:
```bash
python manage.py makemigrations
python manage.py migrate
```
Una volta completato, si può avviare il server locale con:
```bash
manage.py runserver
```
L'applicazione sarà accessibile all'indirizzo: http://localhost:8000.

![Pagina_iniziale](https://github.com/user-attachments/assets/cd324c27-7606-4bb6-81ad-bcdc3009fa0f)


A questo punto è possibile creare utenti, gestire prenotazioni e accedere alle funzionalità disponibili in base al ruolo selezionato cliccando sul pulsante “Area Privata” al centro della pagina.

**Homepage**:
La homepage offre un accesso rapido alle principali funzionalità della clinica:
- **Storia clinica**, per informare gli utenti sulla clinica e i suoi servizi.
- **Accesso all'area privata**, dove pazienti, personale e amministratore possono accedere.
- **Orari e contatti**, per facilitare la comunicazione con la struttura.
In alto a destra, gli utenti possono:
- Consultare i trattamenti disponibili e prenotarli.
- Visualizzare gli eventi e iscriversi.
- Leggere le recensioni dei clienti sui trattamenti ricevuti.

**Area Riservata:** L'applicazione prevede accessi differenziati in base al ruolo dell'utente:
1. **Login Amministratore**
- Gestione dei trattamenti: visualizzazione, aggiunta ed eliminazione.
- Organizzazione degli eventi della clinica: creazione ed eliminazione, aggiornamento presenze.
- Lista Prenotazioni Clinica

2. **Login Personale**
- Gestione della cartella clinica dei pazienti (aggiunta, modifica ed eliminazione).
- Iscrizione agli eventi della clinica.
- Visualizzazione degli appuntamenti dei pazienti.

3. **Login Paziente**
- Registrazione (se non ha già un account).
- Accesso alla propria cartella clinica.
- Iscrizione agli eventi disponibili.
- Recensione di trattamenti effettuati.
- Prenotazione e annullamento di appuntamenti.

![Area_riservata](https://github.com/user-attachments/assets/19e40c4b-7b27-42f7-903d-9b316808e213)


*Paziente*
![Area_riservata_paziente](https://github.com/user-attachments/assets/5ffa73b3-f54e-46d4-be0c-9e6b06ec0469)


*Personale*
![Area_riservata_personale](https://github.com/user-attachments/assets/9509ee64-8db4-46a1-a8fb-243a3bfb5769)

	
*Amministratore*
![Area_riservata_amministratore](https://github.com/user-attachments/assets/53e65e84-9b7e-468c-b222-f84883bf6d3a)

---

## **Licenza**
Questo progetto è stato realizzato a scopo didattico.
