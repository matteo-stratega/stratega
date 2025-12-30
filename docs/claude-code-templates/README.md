# Claude Code - Templates Pronti

Copia questa cartella nel tuo nuovo progetto per avere tutto configurato.

## Setup Rapido

```bash
# 1. Crea cartella progetto
mkdir mio-progetto
cd mio-progetto

# 2. Inizializza git
git init

# 3. Copia questi template
cp -r /percorso/a/questi/templates/* .

# 4. Crea le cartelle mancanti
mkdir -p notes/daily-summaries
mkdir -p docs

# 5. Avvia Claude Code
claude

# 6. Testa con /start
```

## Contenuto

```
templates/
├── CLAUDE.md                    # Istruzioni principali
├── brain/
│   └── context.md               # Stato persistente
├── .claude/
│   └── commands/
│       ├── start.md             # Comando /start
│       └── close.md             # Comando /close
├── .gitignore                   # File da ignorare
└── README.md                    # Questo file
```

## Dopo il Setup

1. Modifica `CLAUDE.md` per le tue esigenze specifiche
2. Compila `brain/context.md` con i tuoi progetti
3. Testa `/start` e `/close`

## Comandi Disponibili

| Comando | Cosa fa |
|---------|---------|
| `/start` | Carica contesto e propone priorita |
| `/close` | Salva report e aggiorna context |
| `/help` | Mostra aiuto Claude Code |
| `/clear` | Pulisce la conversazione |
