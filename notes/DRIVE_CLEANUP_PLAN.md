# Piano Pulizia Drive + AI-Projects

**Data:** 5 Dicembre 2025
**Status:** ✅ COMPLETATO (Fase 1)
**Priorità:** Alta - rischio HDD pieno

---

## Esecuzione 5 Dic 2025

### Fase 1 Completata ✅

**Symlink rimossi (13 totali):**
- `stratega/Clients` (vuoto dal Feb 2023)
- `stratega/Stratega - Templates` (vuoto)
- `stratega/Newsletter` (vuoto)
- `stratega/archive/niccolo@strategaco.com/Video`
- `stratega/archive/niccolo@strategaco.com/Loghi Fixed Size`
- `stratega/archive/massimo@strategaco.com/*` (5 symlink)
- `stratega/archive/drive-duplicates/Clients (1)/Startup-Pack/Partner Kit`
- `stratega/archive/Clients - Archive/Drivio`
- `stratega/assets/logos/.../LeadDelta logo and Icon`

**Symlink mantenuto:** `stratega/videos` (Academy videos)

**Backup salvato:** `notes/symlink-backup-20251205.txt`

**Risultato:** 32GB → 36GB liberi (+4GB)

### Fase 2: Stream Mode (OPZIONALE)

Se vuoi recuperare altri ~6-8GB:
1. Apri Google Drive Desktop
2. Preferenze → cartelle in Mirror
3. Per "Drive Stratega/Archive" → cambia in "Stream files"
4. I file restano in cloud, scaricati on-demand

**Nota:** Con symlink rimossi, ora è SAFE farlo senza rompere nulla.

---

---

## Situazione Attuale

| Cosa | Spazio Locale |
|------|---------------|
| Drive Stratega | 10 GB |
| Drive Personale | 1.1 GB |
| My Drive PickEat | 0.9 GB |
| AI-Projects/stratega | 15 GB |
| AI-Projects/pickeat | 3.4 GB |
| **Totale** | ~30 GB |

**Problema:** Symlink da AI-Projects → Drive creano dipendenze e potenziali duplicazioni.

### Symlink Esistenti

```
AI-Projects/stratega/Clients → Drive (mirror-symlink)
AI-Projects/stratega/archive/drive-duplicates/... → Drive
AI-Projects/stratega/archive/niccolo@strategaco.com/... → Drive
AI-Projects/stratega/archive/massimo@strategaco.com/... → Drive
AI-Projects/pickeat/archivio/drive-links/... → Drive
```

---

## Opzioni

### Opzione A: Single Source in AI-Projects
1. Copia file essenziali da Drive → AI-Projects
2. Rimuovi symlink
3. Switch Drive a Stream mode → **+12GB liberi**
4. Drive solo per sharing esterno

**Pro:** AI-Projects autonomo, no dipendenze
**Contro:** Gestione versioning manuale

### Opzione B: Single Source in Drive
1. Sposta AI-Projects dentro Drive Stratega
2. Git repo rimane, file in cloud
3. Stream/Mirror selettivo

**Pro:** Backup automatico Google
**Contro:** Dipendenza sync, possibili conflitti git

### Opzione C: Hybrid - Elimina Archive (RACCOMANDATO)
1. Tieni AI-Projects com'è
2. Rimuovi symlink agli archivi vecchi
3. Switch solo Archive in Stream mode → **+6GB liberi**
4. Mirror solo cartelle attive

**Pro:** Minimo cambiamento, buon recupero spazio
**Contro:** Setup ibrido

---

## Prima di Procedere

### Consulto CTO Richiesto

Domande per CTO:
1. Quali symlink sono realmente usati vs archivio morto?
2. Rischi di rompere workflow esistenti?
3. Opzione C è safe o serve approccio diverso?
4. Come gestire backup/versioning post-migrazione?

---

## Checklist Esecuzione (dopo OK CTO)

- [ ] Audit completo symlink: quali sono attivi?
- [ ] Backup stato attuale (lista symlink + target)
- [ ] Rimuovere symlink archivio
- [ ] Testare che AI-Projects funzioni
- [ ] Cambiare Archive in Stream mode su Google Drive
- [ ] Verificare spazio liberato
- [ ] Documentare nuova architettura

---

## Note

- Spazio attuale libero: 32GB (29% capacity)
- Target: mantenere >50GB liberi per sicurezza
- Stream mode potrebbe recuperare 10-12GB extra

---

*Creato: 5 Dic 2025*
*Da eseguire: 6 Dic 2025 con supervisione CTO*
