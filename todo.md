# Expense Tracker CLI — TODO

Obiettivo: Costruire un'applicazione da riga di comando per gestire le spese personali. I dati devono essere salvati in un file `expenses.json`.

---

## Fase 1 — Setup Storage e Modello Dati

Prima di fare qualsiasi comando, dobbiamo decidere come salvare i soldi.

- [x] Implementa la logica per creare/leggere il file `expenses.json` (esattamente come nel Task Tracker).
- [x] Definisci la struttura di una singola spesa nel JSON. Deve avere:
  - `id`: intero univoco
  - `date`: stringa in formato "YYYY-MM-DD"
  - `description`: stringa testuale
  - `amount`: numero decimale (float)

Criterio "done":

- Il programma sa leggere e scrivere una lista di spese nel file JSON senza crashare.

---

## Fase 2 — Aggiunta e Visualizzazione (Add & List)

Iniziamo con l'inserimento base e la visualizzazione tabellare.

- [ ] Configura `argparse` per accettare il comando `add`.
  - Richiede l'argomento `--description` (testo).
  - Richiede l'argomento `--amount` (numero > 0).
- [ ] Implementa la funzione `add`: crea la spesa con la data odierna (`datetime.now().strftime("%Y-%m-%d")`), genera un ID, salvala e stampa: `Expense added successfully (ID: 1)`.
- [ ] Configura `argparse` per il comando `list`.
- [ ] Implementa la funzione `list`: stampa tutte le spese in un formato tabellare ben allineato.
  - Esempio di header: `ID  Date       Description  Amount`
  - Esempio riga: `1   2026-03-08 Lunch        $20.50`

Criterio "done":

- Riesco ad aggiungere una spesa e a vederla in lista formattata correttamente.

---

## Fase 3 — Modifica ed Eliminazione (Update & Delete)

Gestiamo gli errori umani (se ho sbagliato a inserire una spesa).

- [ ] Configura `argparse` per il comando `delete`.
  - Richiede l'argomento `--id`.
- [ ] Implementa `delete`: cerca la spesa per ID, rimuovila e salva. Se l'ID non esiste, stampa un errore.
- [ ] Configura `argparse` per il comando `update` (opzionale per roadmap.sh, ma utile).
  - Richiede `--id` e può accettare `--description` e/o `--amount`.
- [ ] Implementa `update`: cerca la spesa e modifica solo i campi passati dall'utente.

Criterio "done":

- Le spese possono essere eliminate e modificate, e il JSON si aggiorna di conseguenza.

---

## Fase 4 — Analisi e Aggregazione (Summary)

Questa è la parte nuova e più importante del progetto: la matematica.

- [ ] Configura `argparse` per il comando `summary`.
- [ ] Implementa il calcolo totale: fai un ciclo su tutte le spese, somma la chiave `amount` e stampa `Total expenses: $XX.XX`.
- [ ] Modifica il comando `summary` per accettare un argomento opzionale `--month`.
  - L'argomento accetta un numero da 1 a 12 (es. `--month 8`).
- [ ] Implementa il calcolo mensile: se l'utente passa `--month 8`, somma solo le spese la cui `date` cade nel mese di Agosto dell'anno corrente.
  - Stampa: `Total expenses for August: $XX.XX`.

Criterio "done":

- I calcoli matematici sono corretti, inclusi i filtri per mese.

---

## Fase 5 — Gestione Errori (Edge Cases)

Rendiamo il programma "a prova di stupido".

- [ ] Impedisci l'inserimento di importi negativi (es. `amount < 0`).
- [ ] Gestisci l'errore se l'utente digita `--month 13` o una stringa invece di un numero.
- [ ] Gestisci il caso in cui il comando `list` viene chiamato ma `expenses.json` è vuoto o non ha ancora spese.

Criterio "done":

- La CLI non restituisce mai il traceback rosso di Python, ma solo messaggi di errore puliti e leggibili.

---

## Fase 6 — README

- [ ] Rimuovi stampe di debug.
- [ ] Crea un file `README.md` che spiega i comandi principali con esempi concreti.
- [ ] Fai un commit finale e un push su GitHub.
