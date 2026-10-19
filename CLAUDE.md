# Mapa Pomysłów - instrukcja codziennej aktualizacji

Repozytorium jest PUBLICZNE. Strona: https://karolstudiojowisz.github.io/Mapapomyslow/
Prywatna wersja strony (pełna, z nazwą klienta) to artefakt Claude: https://claude.ai/artifact/UJdkACrVP3wpQb8oghqEDG

## Codzienny przebieg

1. Gmail: `from:notifications@mail.ideabrowser.com` z ostatnich 2 dni. Pomiń maile od `jordan@` (promocje).
   Sprawdź ostatnią datę w `archiwum.md` i przetwórz każdy brakujący dzień po kolei.
2. Dla każdego dnia napisz notatkę w formacie archiwum (wzoruj się na ostatnich dniach w `archiwum.md`):
   - `📅 GOOD MORNING - D miesiąca RRRR`
   - `💡` idea dnia z liczbami, potem `🌍 Trend:` / `🌍 Hidden Niche:` / `🛠️ Taktyka dnia:` / `🛠️ Narzędzie dnia:` / `🃏 Founder Playbook:` jeśli są w mailu, potem `📎 Dodatkowo:` (wstęp, sponsorzy pomijani)
   - `---`, potem `🔍 Moja diagnoza:` - konkretnie pod projekty Karola: Quote Builder (kalkulator wycen dla freelancerów wideo), Video Audit (płatna diagnoza wideo marki), ARTMAKESENSESTUDIO (jego studio wideo), główny klient Bites (studio reklamy food), Cosmic Cowboy (kanał z muzyką generatywną i animacją). Nigdy ogólnikowo.
3. Oceń bloki:
   - pomysły (💡 i 🌍 Hidden Niche) -> `scan`: `cat` (wideo, food, mark, local, ai, handel, hobby, zycie, zdrowie, fin, przem), `c` = [co wie, co widzi, co może sprzedać] po 0-2, `note` = jedno zdanie "co z tego dla Karola"
   - trendy, playbooki, taktyki, narzędzia -> `lessons`: `pat` (SBB, PRICE, LEAD, EMO, DIST, AIVIS, HUMAN, RET, OPS, NICHE, FIN, CULT, TECH), `rel` 0-2
   - każdy blok z `scan` dostaje też `tags` (dla kreatora "Twoja orbita"): `ind` branże (wideo, foto, grafika, muzyka, pisanie, moda, rekodzielo, wnetrza, beauty, fitness, zdrowie, coaching, edukacja, dzieci, zwierzeta, gastro, ecom, sklep, nieruch, turystyka, dom, moto, rolnictwo, marketing, it, finanse, prawo, hr, logistyka), `skl` umiejętności (kamera, pisanie, uczenie, sprzedaz, organizacja, programowanie, projektowanie, social, rece, liczby), `form` (freelancer, firma, etat, tworca, start), `goal` (dochod, klienci, produkt, firma0), `aud` komu się sprzedaje (b2b, b2c, tworcy, lokal)
   - bloków 📎 nie oceniaj
4. Pobierz prywatne pliki artefaktu (Artifact read, path `archiwum.md` i `oceny.json`) do katalogu roboczego poza repozytorium.
5. `python3 narzedzia/dodaj_dzien.py notatka.md oceny_dnia.json --prywatne <prywatne archiwum.md> --prywatne-oceny <prywatne oceny.json>`
6. Commit i push do `main` (GitHub Pages odświeży się sam).
7. Opublikuj artefakt ponownie z `url` powyżej, z plikami `archiwum.md` i `oceny.json` z prywatnych kopii (index.html bez zmian, pobierz go z artefaktu).

## Zasady treści (obowiązkowe)

- Żadnych informacji osobistych: zdrowie, ADHD, prokrastynacja, horoskop, Human Design, opór przed sprzedażą, cele osobiste. Skrypt odrzuci notatkę z takimi słowami.
- Żadnych długich myślników ani podwójnych łączników. Używaj zwykłego łącznika albo przecinka.
- Pisz po polsku. Nazwę klienta Bites skrypt sam zamienia na "Studio F" w wersji publicznej.
