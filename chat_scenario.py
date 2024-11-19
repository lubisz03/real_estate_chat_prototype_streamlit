chat_scenario = [
    {"role": "ai", "content": "Cześć! Jestem Twoim asystentem do wyszukiwania mieszkań. Powiedz mi, czego szukasz!"},
    {"role": "user", "content": "Szukam mieszkania dwupokojowego w przystępnej cenie."},
    {"role": "ai", "content": "Świetnie! Czy preferujesz konkretną lokalizację, np. blisko centrum czy w spokojnej okolicy?"},
    {"role": "user", "content": "Najlepiej w spokojnej okolicy."},
    {"role": "ai", "content": "A co z wyposażeniem? Chcesz mieszkanie umeblowane czy do własnej aranżacji?"},
    {"role": "user", "content": "Umeblowane, gotowe do zamieszkania."},
    {
        "role": "ai",
        "content": "Mam dla Ciebie dwie propozycje:",
        "offer": [
            {
                "title": "**1. Mieszkanie na obrzeżach miasta**",
                "description": "2 pokoje, 50m², umeblowane, 2000 PLN/miesiąc",
                "image": "./assets/house1.webp",
                "url": "https://example.com/zdjecia1"
            },
            {
                "title": "**2. Ciche mieszkanie przy parku**",
                "description": "2 pokoje, 45m², umeblowane, 2200 PLN/miesiąc",
                "image": "./assets/house2.webp",
                "url": "https://example.com/zdjecia2"
            }
        ]
    },
    {"role": "user", "content": "Chyba nie, wolałbym coś bliżej centrum."},
    {
        "role": "ai",
        "content": "Rozumiem! Sprawdź tę opcję bliżej centrum miasta:",
        "offer": [{
            "title": "**Mieszkanie w centrum**",
            "description": "2 pokoje, 48m², umeblowane, 2500 PLN/miesiąc",
            "image": "./assets/house3.webp",
            "url": "https://example.com/zdjecia3"
        }]
    },
    {"role": "user", "content": "To wygląda super, biorę!"},
    {"role": "ai", "content": "Cieszę się, że udało się znaleźć idealne mieszkanie! Jeśli będziesz potrzebować więcej pomocy, daj znać. Powodzenia z przeprowadzką!"}
]
