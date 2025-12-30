#!/usr/bin/env python3
"""
Duomo 2025 Report - Slides Creator
Creates all slides using Google Slides API
"""

import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Config
PRESENTATION_ID = "1kQOES3FY4Q6VZZUq3NSBTakRFV_RpUaGYnHfZkM8CYs"
CREDENTIALS_PATH = "/Users/matteolombardi/AI-Projects/stratega/.credentials/duomo-analytics-668da1823fd3.json"

# Colors (RGB 0-1 scale)
BLACK = {"red": 0, "green": 0, "blue": 0}
CYAN = {"red": 0.137, "green": 0.757, "blue": 0.855}  # #23C1DA
WHITE = {"red": 1, "green": 1, "blue": 1}
GRAY = {"red": 0.5, "green": 0.5, "blue": 0.5}

# Page size in EMU (9144000 x 5143500 for 16:9)
PAGE_WIDTH = 9144000
PAGE_HEIGHT = 5143500

def get_service():
    """Create Google Slides API service"""
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=['https://www.googleapis.com/auth/presentations']
    )
    return build('slides', 'v1', credentials=creds)

def create_text_box(page_id, object_id, x, y, width, height, text, font_size=18,
                    bold=False, color=WHITE, alignment="START"):
    """Generate requests for a text box"""
    return [
        {
            "createShape": {
                "objectId": object_id,
                "shapeType": "TEXT_BOX",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size": {
                        "width": {"magnitude": width, "unit": "EMU"},
                        "height": {"magnitude": height, "unit": "EMU"}
                    },
                    "transform": {
                        "scaleX": 1, "scaleY": 1,
                        "translateX": x, "translateY": y,
                        "unit": "EMU"
                    }
                }
            }
        },
        {
            "insertText": {
                "objectId": object_id,
                "text": text,
                "insertionIndex": 0
            }
        },
        {
            "updateTextStyle": {
                "objectId": object_id,
                "style": {
                    "foregroundColor": {"opaqueColor": {"rgbColor": color}},
                    "fontSize": {"magnitude": font_size, "unit": "PT"},
                    "bold": bold,
                    "fontFamily": "Arial"
                },
                "fields": "foregroundColor,fontSize,bold,fontFamily"
            }
        },
        {
            "updateParagraphStyle": {
                "objectId": object_id,
                "style": {"alignment": alignment},
                "fields": "alignment"
            }
        }
    ]

def set_background_black(page_id):
    """Set slide background to black"""
    return {
        "updatePageProperties": {
            "objectId": page_id,
            "pageProperties": {
                "pageBackgroundFill": {
                    "solidFill": {"color": {"rgbColor": BLACK}}
                }
            },
            "fields": "pageBackgroundFill"
        }
    }

def create_slide(slide_id):
    """Create a blank slide"""
    return {
        "createSlide": {
            "objectId": slide_id,
            "slideLayoutReference": {"predefinedLayout": "BLANK"}
        }
    }

# Slide content definitions
SLIDES = [
    # Slide 1 - Cover (already exists as 'p', we'll update it)
    {
        "id": "p",
        "update_existing": True,
        "elements": [
            {"id": "elem_cover_title", "x": 500000, "y": 1500000, "w": 8000000, "h": 800000,
             "text": "2025 YEARLY REPORT", "size": 48, "bold": True, "color": WHITE, "align": "CENTER"},
            {"id": "elem_cover_subtitle", "x": 500000, "y": 2300000, "w": 8000000, "h": 600000,
             "text": "DUOMO DESIGN", "size": 72, "bold": True, "color": CYAN, "align": "CENTER"},
        ]
    },
    # Slide 2 - Indice
    {
        "id": "slide_02",
        "elements": [
            {"id": "elem_idx_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "Indice", "size": 48, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_idx_body", "x": 500000, "y": 1000000, "w": 8000000, "h": 3500000,
             "text": "1. I Numeri - Performance 2025\n2. Il Confronto - 2024 vs 2025\n3. Cosa ha Funzionato - I prodotti star\n4. 2026 - Prossimi passi\n5. Bonus - Il percorso dal 2022",
             "size": 28, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 3 - Section 01
    {
        "id": "slide_03",
        "elements": [
            {"id": "elem_s01_num", "x": 500000, "y": 1500000, "w": 3000000, "h": 1500000,
             "text": "01", "size": 120, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_s01_title", "x": 3500000, "y": 2000000, "w": 5000000, "h": 800000,
             "text": "I Numeri 2025", "size": 48, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 4 - Big Number 561
    {
        "id": "slide_04",
        "elements": [
            {"id": "elem_big561", "x": 500000, "y": 1000000, "w": 8000000, "h": 1500000,
             "text": "561", "size": 144, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_big561_sub", "x": 500000, "y": 2500000, "w": 8000000, "h": 600000,
             "text": "CONTATTI GENERATI", "size": 36, "bold": True, "color": WHITE, "align": "CENTER"},
            {"id": "elem_big561_desc", "x": 500000, "y": 3300000, "w": 8000000, "h": 500000,
             "text": "Il miglior anno di sempre per Duomo Design.", "size": 24, "bold": False, "color": GRAY, "align": "CENTER"},
        ]
    },
    # Slide 5 - KPI Grid
    {
        "id": "slide_05",
        "elements": [
            {"id": "elem_kpi1", "x": 500000, "y": 800000, "w": 4000000, "h": 1500000,
             "text": "561\nContatti", "size": 48, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_kpi2", "x": 4600000, "y": 800000, "w": 4000000, "h": 1500000,
             "text": "€17\nCosto/lead", "size": 48, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_kpi3", "x": 500000, "y": 2500000, "w": 4000000, "h": 1500000,
             "text": "463K\nRaggiunte", "size": 48, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_kpi4", "x": 4600000, "y": 2500000, "w": 4000000, "h": 1500000,
             "text": "2.1M\nViews", "size": 48, "bold": True, "color": CYAN, "align": "CENTER"},
        ]
    },
    # Slide 6 - La Portata
    {
        "id": "slide_06",
        "elements": [
            {"id": "elem_port_title", "x": 500000, "y": 300000, "w": 8000000, "h": 800000,
             "text": "2.1 Milioni", "size": 72, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_port_sub", "x": 500000, "y": 1100000, "w": 8000000, "h": 500000,
             "text": "DI VISUALIZZAZIONI", "size": 28, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_port_bars", "x": 500000, "y": 1800000, "w": 8000000, "h": 2000000,
             "text": "Visualizzazioni     2.100.000\nPersone raggiunte   463.000\nContatti            561",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
            {"id": "elem_port_note", "x": 500000, "y": 4000000, "w": 8000000, "h": 500000,
             "text": "Ogni contatto raggiunto in media 4.5 volte prima di compilare il form.",
             "size": 18, "bold": False, "color": GRAY, "align": "START"},
        ]
    },
    # Slide 7 - Section 02
    {
        "id": "slide_07",
        "elements": [
            {"id": "elem_s02_num", "x": 500000, "y": 1500000, "w": 3000000, "h": 1500000,
             "text": "02", "size": 120, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_s02_title", "x": 3500000, "y": 2000000, "w": 5000000, "h": 800000,
             "text": "Il Confronto", "size": 48, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 8 - Comparison Table
    {
        "id": "slide_08",
        "elements": [
            {"id": "elem_comp_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "L'ANNO DELLA SVOLTA", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_comp_table", "x": 500000, "y": 1000000, "w": 8000000, "h": 2500000,
             "text": "                    2024      2025      Delta\nContatti            203       561       +176%\nCosto/Lead          €32       €17       -48%\nVisualizzazioni     1.7M      2.1M      +20%\nRaggiunte           463K      463K      =",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
            {"id": "elem_comp_note", "x": 500000, "y": 3800000, "w": 8000000, "h": 500000,
             "text": "Con lo stesso pubblico, quasi 3 volte più contatti.",
             "size": 20, "bold": False, "color": GRAY, "align": "START"},
        ]
    },
    # Slide 9 - CPL Comparison
    {
        "id": "slide_09",
        "elements": [
            {"id": "elem_cpl_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "DA €32 A €17", "size": 48, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_cpl_sub", "x": 500000, "y": 900000, "w": 8000000, "h": 500000,
             "text": "IL COSTO PER CONTATTO SI È QUASI DIMEZZATO", "size": 24, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_cpl_bars", "x": 500000, "y": 1800000, "w": 8000000, "h": 1500000,
             "text": "2024:  €32\n2025:  €17\n\n-48%",
             "size": 36, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 10 - Trend Annuale
    {
        "id": "slide_10",
        "elements": [
            {"id": "elem_trend_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "LA SVOLTA DA LUGLIO", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_trend_body", "x": 500000, "y": 1000000, "w": 8000000, "h": 3000000,
             "text": "Primo semestre → Fase di ottimizzazione\nSecondo semestre → Record di efficienza\n\nMesi migliori:\n• Ottobre: record assoluto\n• Settembre: secondo miglior mese\n• Agosto: terzo miglior mese",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 11 - Section 03
    {
        "id": "slide_11",
        "elements": [
            {"id": "elem_s03_num", "x": 500000, "y": 1500000, "w": 3000000, "h": 1500000,
             "text": "03", "size": 120, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_s03_title", "x": 3500000, "y": 2000000, "w": 5000000, "h": 800000,
             "text": "Cosa ha Funzionato", "size": 48, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 12 - Prodotti Star
    {
        "id": "slide_12",
        "elements": [
            {"id": "elem_star_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "ELETTRA E GLADYS WOOD", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_star_sub", "x": 500000, "y": 900000, "w": 8000000, "h": 500000,
             "text": "I DUE LETTI PIÙ APPREZZATI", "size": 24, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_star_table", "x": 500000, "y": 1600000, "w": 8000000, "h": 2000000,
             "text": "Prodotto      Reazioni   Commenti\nGladys Wood   161        29\nElettra       71         14\nAtlante       39         2",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 13 - Interesse Organico
    {
        "id": "slide_13",
        "elements": [
            {"id": "elem_org_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "50+ RICHIESTE NEI COMMENTI", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_org_quotes", "x": 500000, "y": 1000000, "w": 8000000, "h": 2500000,
             "text": "\"Rivenditore a Padova?\"\n\"Prezzo? Misure disponibili?\"\n\"C'è un rivenditore a Milano?\"\n\"Rivenditore a Roma?\"\n\"Vorrei informazioni, sono di Bari\"",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
            {"id": "elem_org_note", "x": 500000, "y": 3800000, "w": 8000000, "h": 500000,
             "text": "POTENZIALI CLIENTI PRONTI ALL'ACQUISTO",
             "size": 20, "bold": True, "color": GRAY, "align": "START"},
        ]
    },
    # Slide 14 - Section 04
    {
        "id": "slide_14",
        "elements": [
            {"id": "elem_s04_num", "x": 500000, "y": 1500000, "w": 3000000, "h": 1500000,
             "text": "04", "size": 120, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_s04_title", "x": 3500000, "y": 2000000, "w": 5000000, "h": 800000,
             "text": "2026", "size": 48, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 15 - Opportunità (Upsell)
    {
        "id": "slide_15",
        "elements": [
            {"id": "elem_ups_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "GESTIRE I COMMENTI", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_ups_sub", "x": 500000, "y": 900000, "w": 8000000, "h": 400000,
             "text": "50-70 richieste commerciali identificate nel 2025", "size": 20, "bold": False, "color": GRAY, "align": "START"},
            {"id": "elem_ups_body", "x": 500000, "y": 1400000, "w": 8000000, "h": 2500000,
             "text": "IL COSTO DELLE RICHIESTE PERSE\nRichieste nei commenti: ~60\nValore medio per contatto: €17\nValore perso stimato: €1.000+\n\nLA SOLUZIONE\nOggi → Risposta manuale, richieste perse\nCon automazione → Risposta 24/7, ogni richiesta catturata\n\nCosto: €180/anno → ROI: 450%+",
             "size": 20, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 16 - Prossimi Passi
    {
        "id": "slide_16",
        "elements": [
            {"id": "elem_next_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "CONTINUARE A CRESCERE", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_next_body", "x": 500000, "y": 1000000, "w": 8000000, "h": 3000000,
             "text": "Q1 2026\n□ Nuove creatività per mantenere l'interesse\n□ Test di Gladys Wood nelle campagne\n□ Valutazione automazione commenti\n\nOBIETTIVI\n• Costo/contatto sotto €15\n• Raggiungere 600+ contatti\n• Recuperare lead dai commenti",
             "size": 24, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 17 - Section 05
    {
        "id": "slide_17",
        "elements": [
            {"id": "elem_s05_num", "x": 500000, "y": 1500000, "w": 3000000, "h": 1500000,
             "text": "05", "size": 120, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_s05_title", "x": 3500000, "y": 2000000, "w": 5000000, "h": 800000,
             "text": "Bonus: Il Percorso", "size": 48, "bold": True, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 18 - Growth Chart
    {
        "id": "slide_18",
        "elements": [
            {"id": "elem_grow_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "DAL 2022 AD OGGI", "size": 36, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_grow_sub", "x": 500000, "y": 900000, "w": 8000000, "h": 400000,
             "text": "4 ANNI DI CRESCITA", "size": 24, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_grow_bars", "x": 500000, "y": 1500000, "w": 8000000, "h": 2000000,
             "text": "2022    51\n2023    112\n2024    203\n2025    561",
             "size": 36, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_grow_note", "x": 500000, "y": 3800000, "w": 8000000, "h": 500000,
             "text": "+1.000% dal 2022 al 2025",
             "size": 24, "bold": True, "color": CYAN, "align": "START"},
        ]
    },
    # Slide 19 - Efficienza
    {
        "id": "slide_19",
        "elements": [
            {"id": "elem_eff_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "CONTATTI PER OGNI €1.000 INVESTITI", "size": 32, "bold": True, "color": CYAN, "align": "START"},
            {"id": "elem_eff_table", "x": 500000, "y": 1000000, "w": 8000000, "h": 2000000,
             "text": "2022    ~10\n2023    16\n2024    31\n2025    60",
             "size": 36, "bold": True, "color": WHITE, "align": "START"},
            {"id": "elem_eff_note", "x": 500000, "y": 3500000, "w": 8000000, "h": 500000,
             "text": "Con lo stesso budget del 2022, oggi 6 volte più contatti.",
             "size": 20, "bold": False, "color": GRAY, "align": "START"},
        ]
    },
    # Slide 20 - Summary
    {
        "id": "slide_20",
        "elements": [
            {"id": "elem_sum_title", "x": 500000, "y": 300000, "w": 8000000, "h": 600000,
             "text": "2025: L'ANNO DEI RECORD", "size": 36, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_sum_body", "x": 500000, "y": 1000000, "w": 8000000, "h": 3000000,
             "text": "561      Contatti generati\n2.1M     Visualizzazioni\n463K     Persone raggiunte\n€17      Costo medio per contatto\n-48%     Riduzione costi vs 2024\n+176%    Crescita contatti vs 2024",
             "size": 28, "bold": False, "color": WHITE, "align": "START"},
        ]
    },
    # Slide 21 - Closing
    {
        "id": "slide_21",
        "elements": [
            {"id": "elem_close_title", "x": 500000, "y": 1800000, "w": 8000000, "h": 800000,
             "text": "GRAZIE!", "size": 72, "bold": True, "color": CYAN, "align": "CENTER"},
            {"id": "elem_close_sub", "x": 500000, "y": 3500000, "w": 8000000, "h": 500000,
             "text": "MADE BY STRATEGA 2025", "size": 18, "bold": False, "color": GRAY, "align": "CENTER"},
        ]
    },
]

def main():
    print("Connecting to Google Slides API...")
    service = get_service()

    requests = []

    # First, delete all existing slides except the first one, then recreate
    print("Getting current presentation...")
    presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
    existing_slides = presentation.get('slides', [])

    # Delete existing slides (except first)
    for slide in existing_slides[1:]:
        requests.append({
            "deleteObject": {"objectId": slide['objectId']}
        })

    # Delete elements from first slide
    if existing_slides:
        first_slide = existing_slides[0]
        for element in first_slide.get('pageElements', []):
            requests.append({
                "deleteObject": {"objectId": element['objectId']}
            })

    # Set first slide background to black
    requests.append(set_background_black("p"))

    # Create new slides (skip first, it already exists)
    for i, slide_def in enumerate(SLIDES[1:], start=2):
        slide_id = slide_def["id"]
        requests.append(create_slide(slide_id))
        requests.append(set_background_black(slide_id))

    print(f"Created {len(SLIDES)} slide structures...")

    # Add content to all slides
    for slide_def in SLIDES:
        page_id = slide_def["id"]
        for elem in slide_def.get("elements", []):
            requests.extend(create_text_box(
                page_id=page_id,
                object_id=elem["id"],
                x=elem["x"],
                y=elem["y"],
                width=elem["w"],
                height=elem["h"],
                text=elem["text"],
                font_size=elem["size"],
                bold=elem["bold"],
                color=elem["color"],
                alignment=elem["align"]
            ))

    print(f"Total requests: {len(requests)}")

    # Execute batch update
    print("Executing batch update...")
    body = {"requests": requests}
    response = service.presentations().batchUpdate(
        presentationId=PRESENTATION_ID,
        body=body
    ).execute()

    print(f"Done! Updated {len(response.get('replies', []))} elements")
    print(f"\nView presentation: https://docs.google.com/presentation/d/{PRESENTATION_ID}/edit")

if __name__ == "__main__":
    main()
