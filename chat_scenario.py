# chat_scenario = [
#     {"role": "ai", "content": "Cześć! Jestem Twoim asystentem do wyszukiwania mieszkań. Powiedz mi, czego szukasz!"},
#     {"role": "user", "content": "Szukam mieszkania dwupokojowego w przystępnej cenie."},
#     {"role": "ai", "content": "Świetnie! Czy preferujesz konkretną lokalizację, np. blisko centrum czy w spokojnej okolicy?"},
#     {"role": "user", "content": "Najlepiej w spokojnej okolicy."},
#     {"role": "ai", "content": "A co z wyposażeniem? Chcesz mieszkanie umeblowane czy do własnej aranżacji?"},
#     {"role": "user", "content": "Umeblowane, gotowe do zamieszkania."},
#     {
#         "role": "ai",
#         "content": "Mam dla Ciebie dwie propozycje:",
#         "offer": [
#             {
#                 "title": "**1. Mieszkanie na obrzeżach miasta**",
#                 "description": "2 pokoje, 50m², umeblowane, 2000 PLN/miesiąc",
#                 "image": "./assets/house1.webp",
#                 "url": "https://example.com/zdjecia1"
#             },
#             {
#                 "title": "**2. Ciche mieszkanie przy parku**",
#                 "description": "2 pokoje, 45m², umeblowane, 2200 PLN/miesiąc",
#                 "image": "./assets/house2.webp",
#                 "url": "https://example.com/zdjecia2"
#             }
#         ]
#     },
#     {"role": "user", "content": "Chyba nie, wolałbym coś bliżej centrum."},
#     {
#         "role": "ai",
#         "content": "Rozumiem! Sprawdź tę opcję bliżej centrum miasta:",
#         "offer": [{
#             "title": "**Mieszkanie w centrum**",
#             "description": "2 pokoje, 48m², umeblowane, 2500 PLN/miesiąc",
#             "image": "./assets/house3.webp",
#             "url": "https://example.com/zdjecia3"
#         }]
#     },
#     {"role": "user", "content": "To wygląda super, biorę!"},
#     {"role": "ai", "content": "Cieszę się, że udało się znaleźć idealne mieszkanie! Jeśli będziesz potrzebować więcej pomocy, daj znać. Powodzenia z przeprowadzką!"}
# ]
chat_scenario = [
    {"role": "ai", "content": "Cześć! Jestem asystentem pomagającym znaleźć mieszkanie na wynajem idealne do potrzeb każdego! Tobie też pomogę, przedstaw mi proszę tylko swoje wymagania."},
    {"role": "user", "content": "łódź, dwa pokoje, max. 30 minut komunikacją miejską do pł weeia"},
    {"role": "ai", "content": "Jaki jest twój budżet? Mieszkanie spełniające powyższe wymagania w mieście Łódź w podanej lokalizacji zwykle wynająć można w łącznej kwocie od 2000 złotych do 3500 złotych. Powiedz również, czy będziesz wynajmować mieszkanie z kimś?"},
    {"role": "user", "content": "do 2500 zł, będę wynajmować sam"},
    {"role": "ai", "content": "Znalazłem 187 ofert spełniających twoje wymagania. Czy chcesz wyświetlić już przykładowe oferty? A może wolisz podać dodatkowe wymagania i znaleźć lepiej dopasowane mieszkanie?\nPrzykładowe rzeczy, które mają znaczenie przy wynajmie mieszkania to m.in: piętro, balkon lub taras, garaż, wyposażenie kuchni czy łazienki, standard, itp."},
    {"role": "user", "content": "wolę podać dodatkowe kryteria, będzie to: zmywarka, pralka, każde piętro oprócz parteru"},
    {
        "role": "ai",
        "content": "Twoje wymagania spełnia 43 ofert mieszkań. Oto 2 oferty najlepiej dopasowane z nich:",
        "offer": [
            {
                "title": "**1. Mieszkanie dwupokojowe, ul. Radwańska, 30m2, pierwsze piętro**",
                "description": "Koszt wynajmu:\n- miesięcznie ok. 2500 zł (1800zł + 700zł czynsz, opłaty, internet i telewizja)\n- kaucja zwrotna 2500 zł\nLokalizacja:\n- ok. 4 minuty pieszo do Politechnika Łódzka, WEEIA, ul. Prof. Bohdana Stefanowskiego\n- ok. 11 minut pieszo do Nowa Sukcesja, ul. aleje Politechniki\n- ok. 7 minut pieszo do Park im. ks. bp. Michała Klepacza\nWyposażenie:\n- Kuchnia: zmywarka, płyta indukcyjna, zlew, lodówka\n- Łazienka: prysznic, pralka\n- Sypialnia i salon: łóżko dwuosobowe, sofa, telewizor, stół i krzesła\nWarto zwrócić uwagę przed wynajmem:\n- Tylko dla osób niepalących\n- Brak piekarnika w kuchni\n",
                "image": "./assets/img1.webp",
                "url": "https://www.otodom.pl/pl/oferta/przepiekne-2-pokoje-centrum-na-2-6-mcy-lub-rok-ID4pYJh"
            },
            {
                "title": "**2. Mieszkanie dwupokojowe, ul. Uniwersytecka, 47m2, pierwsze piętro**",
                "description": "Koszt wynajmu:\n- miesięcznie ok. 2500 zł (1650zł + 750zł czynsz i opłaty + internet)\n- kaucja zwrotna 2500 zł\nLokalizacja:\n- ok. 29 minut komunikacją miejską do Politechnika Łódzka, WEEIA, ul. Prof. Bohdana Stefanowskiego\n- ok. 26 minut komunikacją miejską do M1 Łódź, ul. Brzezińska\n- ok. 16 minut pieszo do Park Helenów\nWyposażenie:\n- Kuchnia: zmywarka, płyta indukcyjna, zlew, mikrofala, lodówka\n- Łazienka: prysznic, pralka\n- Sypialnia i salon: łóżko dwuosobowe\nWarto zwrócić uwagę przed wynajmem:\n- Tylko dla osób niepalących\n- Brak piekarnika w kuchni\n- Oferta biura nieruchomości (możliwa dodatkowa opłata, brak informacji w ogłoszeniu)\n\nCo sądzisz?",
                "image": "./assets/img2.webp",
                "url": "https://www.otodom.pl/pl/oferta/sloneczne-rozkladowe-mieszkanie-ul-uniwersytecka-ID4tuiI"
            }
        ]
    },
    {"role": "user", "content": "dodaj do wymagań piekarnik w mieszkaniu"},
    {"role": "ai", "content": "Czy dodatkowo oprócz tego możesz zwiększyć budżet do 2600 zł łącznie? Dzięki temu, pokażę dodatkowo dwie kolejne oferty świetnie dopasowane do twoich potrzeb!"},
    {"role": "user", "content": "tak, zwiększ budżet do 2600 zł"},
    {
        "role": "ai",
        "content": "Oto dwie kolejne propozycje spełniające twoje wymagania:",
        "offer": [
            {
                "title": "**3. Mieszkanie dwupokojowe, ul. Ogrodowa, 38m2, drugie piętro**",
                "description": "Koszt wynajmu:\n- miesięcznie ok. 2600 zł (1800zł + 700zł czynsz i opłaty + prąd + internet)\n- kaucja zwrotna 3000 zł\nLokalizacja:\n- ok. 23 minuty komunikacją miejską do Politechnika Łódzka, WEEIA, ul. Prof. Bohdana Stefanowskiego\n- ok. 6 minut pieszo do Manufaktura, ul. Drewnowska\n- ok. 4 minut pieszo do Park Staromiejski\nWyposażenie:\n- Kuchnia: piekarnik, zmywarka, płyta elektryczna, zlew, lodówka, czajnik\n- Łazienka: prysznic, pralka\n- Sypialnia i salon: łóżko dwuosobowe, szafa, kanapa, stół i krzesła\nWarto zwrócić uwagę przed wynajmem:\n- Tylko dla osób niepalących\n- Oferta biura nieruchomości (możliwa dodatkowa opłata, brak informacji w ogłoszeniu)\n",
                "image": "./assets/img3.webp",
                "url": "https://www.otodom.pl/pl/oferta/przepiekne-2-pokoje-centrum-na-2-6-mcy-lub-rok-ID4pYJh"
            },
            {
                "title": "**4. Mieszkanie dwupokojowe, ul. Mahatmy Gandhiego, 45m2, drugie piętro**",
                "description": "Koszt wynajmu:\n- miesięcznie ok. 2600 zł (1600zł + 880zł czynsz i opłaty + internet)\n- kaucja zwrotna 2480 zł\nLokalizacja:\n- ok. 30 minut komunikacją miejską do Politechnika Łódzka, WEEIA, ul. Prof. Bohdana Stefanowskiego\n- ok. 15 minut pieszo do Manufaktura, ul. Drewnowska\n- ok. 10 minut pieszo do Miejski Skwer na Lutomierskiej\nWyposażenie:\n- Kuchnia: piekarnik, zmywarka, kuchnia gazowa, zlew, lodówka, czajnik\n- Łazienka: wanno-prysznic, pralka\n- Sypialnia i salon: łóżko dwuosobowe, szafa, kanapa, kanapa, stół i krzesła, telewizor\nWarto zwrócić uwagę przed wynajmem:\n- Bardzo krótki opis oferty, braki dokładanych informacji w wynajmie\n",
                "image": "./assets/img4.webp",
                "url": "https://www.otodom.pl/pl/oferta/wynajme-45-m2-dwa-pokoje-ID3QzfK"
            }
        ]
    },
    {"role": "user", "content": "oferta nr 3 mi pasuje"},
    {"role": "ai", "content": "To świetnie! Powodzenia w wynajmie! Jeżeli jeszcze będziesz mnie potrzebować, to wiesz gdzie mnie szukać."},
    {"role": "user", "content": "ok"},
]
