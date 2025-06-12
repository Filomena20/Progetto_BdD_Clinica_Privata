
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
- **Prenotazione e gestione degli appuntamenti**.
- **Organizzazione di eventi sanitari e formativi**, aperti al pubblico o riservati al personale.
- **Recensioni dei pazienti** sui trattamenti ricevuti.
- **Interfaccia differenziata** per visitatori, pazienti, personale sanitario e amministratori, ciascuno con accesso a funzionalità specifiche.  

L'architettura **garantisce sicurezza e controllo degli accessi**, oltre a offrire un’esperienza utente personalizzata.

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
![Modello_E/R](https://github.com/user-attachments/assets/e9ecd5c1-9abb-4bed-bcd1-fa526afae3d5)

---

## **Installazione**
Per eseguire l’applicazione, è necessario:  
1. **Avere Python installato** nel proprio ambiente.  
2. **Avere accesso a un server MySQL/MariaDB**, preferibilmente con phpMyAdmin.  
3. **Clonare il progetto** nella propria directory locale.  
```bash
git clone https://github.com/Filomena20/Progetto_BdD_Clinica_Privata.git
cd clinica
```
4. **Creare e attivare un ambiente virtuale (consigliato)**
```bash
python -m venv env
# Linux/macOS
source env/bin/activate
# Windows
.\env\Scripts\activate
```
5. **Installare le dipendenze**
```bash
pip install -r requirements.txt
```
Se non si vuole usare il file requirements.txt, installare manualmente eseguendo:
```bash
   pip install django mysqlclient
```
---
## **Configurazione del Database**
1. **Importare il database da dump SQL***
Se disponi di un file `.sql` con il dump del database puoi importarlo nel tuo server MySQL/MariaDB.
- Metodo 1: via phpMyAdmin
* Accedi a phpMyAdmin
* Crea un nuovo database 
* Clicca su Importa e carica il file dump.sql

2. **Configurazione Database su Django**
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


A questo punto è possibile creare utenti, gestire prenotazioni e accedere alle funzionalità disponibili in base al profilo selezionato cliccando sul pulsante “Area Privata” al centro della pagina.

**Homepage**:
La homepage offre un accesso rapido alle principali funzionalità della clinica:
- **Storia clinica**, per informare gli utenti sulla clinica.
- **Accesso all'area privata**, dove pazienti, personale e amministratore possono accedere.
- **Orari e contatti**, per facilitare la comunicazione con la struttura.
In alto a destra, gli utenti possono:
- Consultare i trattamenti disponibili e prenotarli.
- Visualizzare gli eventi e iscriversi.
- Leggere le recensioni sui trattamenti.

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
Questo progetto è stato realizzato e distribuito a scopo didattico con licenza [MIT](LICENSE).
Puoi usarlo, modificarlo e distribuirlo liberamente, a patto che venga mantenuta la nota di copyright.
