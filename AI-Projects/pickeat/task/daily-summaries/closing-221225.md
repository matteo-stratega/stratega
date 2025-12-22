# Closing 22-12-25

## TL;DR
- **Done**: Varese G6 debrief analizzato, 2 email voucher pronte, Google Analytics MCP configurato
- **Pending**: Inviare 2 voucher email, riavviare Claude per attivare GA MCP, report Varese completo
- **Next**: Riaprire sessione → test GA MCP → completare report Varese con dati analytics

## Details

### Done
1. **Varese G6 Debrief** - Analizzato report Giacomo:
   - Revenue: €219.56 (target €1.250) = -82%
   - Ordini: 14 (target 50) = -72%
   - AOV: €15.68 (target €25) = -37%
   - Solo 2 ordini ≥€25 (Davide Macchi €34.99, Catherine Flumiani €28.99)
   - Problema: Hot dog sold out 40 min + bar chiuso 20 min durante intervallo

2. **Email Voucher** - Preparate 2 email pronte da inviare:
   - davide@macchivarese.it (€34.99)
   - kat.flu25@gmail.com (€28.99)
   - Codice voucher da inserire: [DA LORENZO]

3. **Google Analytics MCP Setup**:
   - Service account trovato: `claude@n8npe-474619.iam.gserviceaccount.com`
   - File spostato in `~/.config/google/ga-service-account.json`
   - MCP server configurato in `~/.claude/claude_desktop_config.json`
   - GA4 Property ID: 467442633
   - Matteo ha dato editor access al service account in GA4
   - Serve riavvio sessione per attivare

### Pending
- [ ] Inviare 2 email voucher (inserire codice da Lorenzo)
- [ ] Riavviare Claude Code per attivare GA MCP
- [ ] Completare report Varese G6 con dati GA (post-riavvio)
- [ ] Analisi clienti ricorrenti (Catherine ordina 2x, alcuni "abbonati")

### Files
- task/daily-summaries/closing-221225.md
- docs/GOOGLE_ANALYTICS_MCP_SETUP.md (creato da agente)
- ~/.claude/claude_desktop_config.json (modificato - aggiunto GA MCP)
- ~/.config/google/ga-service-account.json (spostato da temp)

### Notes
- Giacomo ignora clienti ricorrenti nel debrief
- Bar Varese ha gestito male lo stock (hot dog out 40 min = ordini persi)
- Platform PickEat: 5/5 performance, nessun bug nostro
- Prossima partita: 3 gen vs Napoli

---

**Session Status**: Pausa per riavvio (GA MCP)
**Prepared by**: Basilio
