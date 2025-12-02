def line_pairs_generator():
    """Генератор, який читає text100.txt і повертає по 3 пари для кожного рядка."""

    f = open("text100.txt", "r", encoding="utf-8")  # відкриваємо файл

    line_number = 0
    for line in f:
        line_number += 1

        words = line.strip().split()  # ділити рядок на слова
        pairs = {}  # словник пар для цього рядка

        # ---- Рахуємо пари всередині кожного слова ----
        for w in words:
            w = w.lower()
            clean = ""

            # залишаємо лише букви
            for ch in w:
                if ch.isalpha():
                    clean += ch

            # рахуємо пари в середині слова
            for i in range(len(clean) - 1):
                pair = clean[i] + clean[i + 1]

                if pair not in pairs:
                    pairs[pair] = 1
                else:
                    pairs[pair] += 1

        # ---- Вибираємо 3 найбільш часті пари ----
        top3 = sorted(pairs.items(), key=lambda x: x[1], reverse=True)[:3]

        # перетворюємо назад у словник
        top3_dict = {p: c for p, c in top3}

        # повертаємо номер рядка та 3 пари
        yield line_number, top3_dict

    f.close()



# --------------- ОСНОВНА ЧАСТИНА -----------------

for num, top_pairs in line_pairs_generator():
   print("Рядок", num, "---", top_pairs)

