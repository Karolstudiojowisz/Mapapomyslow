"""Dopisuje jeden dzień IdeaBrowser do archiwum i ocen.

Użycie:
  python3 narzedzia/dodaj_dzien.py notatka.md oceny_dnia.json [--prywatne sciezka/archiwum_prywatne.md --prywatne-oceny sciezka/oceny_prywatne.json]

notatka.md       jedna notatka dnia, zaczyna się od linii "📅 GOOD MORNING - D miesiąca RRRR"
oceny_dnia.json  {"scan": {"0": {"cat": "wideo", "c": [2,1,1], "note": "..."}},
                  "lessons": {"1": {"pat": "LEAD", "rel": 2}},
                  "tags": {"0": {"ind": ["wideo"], "skl": ["kamera"], "form": ["freelancer"], "goal": ["klienci"]}}}
                 klucze to numery bloków w notatce (0 = pierwszy blok 💡, potem 🌍/🛠️/🃏/📎 w kolejności).

Wersja publiczna (archiwum.md i oceny.json w repozytorium) dostaje "Studio F" zamiast nazwy klienta.
Opcjonalnie te same dane trafiają do prywatnych kopii bez zamiany nazwy.
"""
import json, re, sys, argparse

MIES = {"czerwca": 6, "lipca": 7, "sierpnia": 8, "września": 9, "października": 10,
        "listopada": 11, "grudnia": 12, "stycznia": 1, "lutego": 2, "marca": 3,
        "kwietnia": 4, "maja": 5}
CATS = {"wideo", "food", "mark", "local", "ai", "handel", "hobby", "zycie", "zdrowie", "fin", "przem"}
PATS = {"SBB", "PRICE", "LEAD", "EMO", "DIST", "AIVIS", "HUMAN", "RET", "OPS", "NICHE", "FIN", "CULT", "TECH"}
MARKS = ("💡", "🌍", "🛠️", "🛠", "🃏", "📎")
BLOCKED = ["ADHD", "prokrastyn", "Merkur", "horoskop", "Human Design", "—", "--"]


def data_z_notatki(txt):
    first = txt.strip().split("\n", 1)[0]
    m = re.search(r"(\d{1,2}) (\S+) (\d{4})", first)
    if not first.startswith("📅") or not m or m.group(2) not in MIES:
        sys.exit("Pierwsza linia musi wyglądać tak: 📅 GOOD MORNING - 20 października 2026")
    return "%s-%02d-%02d" % (m.group(3), MIES[m.group(2)], int(m.group(1)))


def liczba_blokow(txt):
    body = txt.split("🔍 Moja diagnoza")[0]
    return sum(1 for ln in body.split("\n") if ln.startswith(MARKS))


def dopisz(archiwum, oceny, txt, dzien, data):
    a = open(archiwum, encoding="utf-8").read()
    if re.search(r"^📅[^\n]*\b%d %s %s" % (int(data[8:]), [k for k, v in MIES.items() if v == int(data[5:7])][0], data[:4]), a, re.M):
        print("Ten dzień już jest w", archiwum, "- pomijam")
        return False
    with open(archiwum, "a", encoding="utf-8") as f:
        f.write("\n\n---\n\n" + txt.strip() + "\n")
    o = json.load(open(oceny, encoding="utf-8"))
    for i, v in dzien.get("scan", {}).items():
        o["scan"]["%s#%s" % (data, i)] = v
    for i, v in dzien.get("lessons", {}).items():
        o["lessons"]["%s#%s" % (data, i)] = v
    o.setdefault("tags", {})
    for i, v in dzien.get("tags", {}).items():
        o["tags"]["%s#%s" % (data, i)] = v
    json.dump(o, open(oceny, "w", encoding="utf-8"), ensure_ascii=False)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("notatka"); ap.add_argument("oceny_dnia")
    ap.add_argument("--prywatne"); ap.add_argument("--prywatne-oceny")
    a = ap.parse_args()
    txt = open(a.notatka, encoding="utf-8").read()
    dzien = json.load(open(a.oceny_dnia, encoding="utf-8"))
    data = data_z_notatki(txt)
    n = liczba_blokow(txt)
    for part in ("scan", "lessons"):
        for i, v in dzien.get(part, {}).items():
            if not i.isdigit() or int(i) >= n:
                sys.exit(f"Zły numer bloku {i} w {part} (notatka ma {n} bloków)")
            if part == "scan" and (v.get("cat") not in CATS or len(v.get("c", [])) != 3):
                sys.exit(f"Zła ocena w bloku {i}: {v}")
            if part == "lessons" and v.get("pat") not in PATS:
                sys.exit(f"Zły wzorzec w bloku {i}: {v}")
    check = "\n".join(l for l in txt.split("\n") if l.strip() != "---") + json.dumps(dzien, ensure_ascii=False)
    bad = [w for w in BLOCKED if w.lower() in check.lower()]
    if bad:
        sys.exit("Notatka zawiera niedozwolone treści: " + ", ".join(bad))
    if "🔍 Moja diagnoza" not in txt:
        sys.exit("Brak sekcji 🔍 Moja diagnoza")
    pub_txt = txt.replace("Bites", "Studio F")
    pub_dzien = json.loads(json.dumps(dzien, ensure_ascii=False).replace("Bites", "Studio F"))
    dopisz("archiwum.md", "oceny.json", pub_txt, pub_dzien, data)
    if a.prywatne and a.prywatne_oceny:
        dopisz(a.prywatne, a.prywatne_oceny, txt, dzien, data)
    print("OK", data, "bloków:", n)


if __name__ == "__main__":
    main()
