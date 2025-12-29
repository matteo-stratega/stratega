# Guida: Download Video da Corsi Online

**Caso d'uso:** Hai pagato un corso e vuoi i video offline.

---

## Setup (una tantum)

### 1. Installa yt-dlp
```bash
brew install yt-dlp
```

### 2. Installa estensione cookies
- Chrome: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
- Firefox: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

### 3. Esporta cookies
1. Vai sul sito del corso (loggato)
2. Click sull'estensione → Export
3. Salva come `cookies.txt`

---

## Download Singolo Video

```bash
yt-dlp --cookies ~/Downloads/cookies.txt "URL_DELLA_LEZIONE"
```

**Opzioni utili:**
```bash
# Scegli qualità
yt-dlp --cookies cookies.txt -f "best" "URL"

# Rinomina con titolo lezione
yt-dlp --cookies cookies.txt -o "%(title)s.%(ext)s" "URL"

# Cartella specifica
yt-dlp --cookies cookies.txt -o "~/Downloads/Corso/%(title)s.%(ext)s" "URL"
```

---

## Download Batch (più video)

### Opzione A: Lista manuale
Crea file `urls.txt` con un URL per riga:
```
https://corsi.example.com/lezione-1
https://corsi.example.com/lezione-2
https://corsi.example.com/lezione-3
```

Poi:
```bash
yt-dlp --cookies cookies.txt -a urls.txt -o "%(playlist_index)s - %(title)s.%(ext)s"
```

### Opzione B: Se la piattaforma ha playlist
```bash
yt-dlp --cookies cookies.txt "URL_PAGINA_CORSO_PRINCIPALE"
```
(yt-dlp tenta di trovare tutti i video automaticamente)

---

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| 403 Forbidden | Cookies scaduti → riesporta |
| Video non trovato | Apri Dev Tools → Network → trova URL diretto .mp4/.m3u8 |
| Qualità bassa | Aggiungi `-f "best"` o `-f "bestvideo+bestaudio"` |
| Nome file strano | Usa `-o "%(title)s.%(ext)s"` |

---

## Alternativa Veloce: Dev Tools

Se yt-dlp non funziona:
1. Apri corso nel browser
2. `Cmd + Option + I` (Dev Tools)
3. Tab **Network**
4. Play video
5. Filtra: `media` o `.mp4` o `.m3u8`
6. Click destro → Open in new tab → Salva

---

## Piattaforme Testate

| Piattaforma | Metodo |
|-------------|--------|
| Thinkific | yt-dlp + cookies |
| Teachable | yt-dlp + cookies |
| Kajabi | yt-dlp + cookies (a volte DRM) |
| Udemy | App mobile ha download nativo |
| Coursera | App mobile ha download nativo |

---

*Creato: 21 Dicembre 2025*
