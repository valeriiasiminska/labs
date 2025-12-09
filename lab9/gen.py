def line_pairs_generator():
    """Генератор: читає файл пострічково, шукає пари букв і повертає 3 найчастіші."""

    f = open("text100.txt", "r", encoding="utf-8")  # Відкриваємо файл для читання

    line_number = 0  # Лічильник рядків

    # Цикл, який читає файл рядок за рядком
    for line in f:
        line_number = line_number + 1  # Збільшуємо номер рядка

        # 1. Підготовка рядка: прибираємо пробіли, ділимо на слова
        line = line.strip()
        words = line.split()

        # 2. Тут будемо зберігати всі пари букв для цього рядка
        pairs = {}

        # 3. Обходимо кожне слово
        for w in words:

            # Приводимо до нижнього регістру
            w = w.lower()

            # Очищення слова: беремо тільки букви
            clean_word = ""
            for ch in w:
                if ch.isalpha():
                    clean_word = clean_word + ch

            # 4. Якщо слово менше 2 букв — пропускаємо (пари не існує)
            if len(clean_word) < 2:
                continue

            # 5. Знаходимо всі пари сусідніх букв у слові
            for i in range(len(clean_word) - 1):
                pair = clean_word[i] + clean_word[i + 1]

                # Якщо пара зустрілась вперше
                if pair not in pairs:
                    pairs[pair] = 1
                else:
                    pairs[pair] = pairs[pair] + 1

        # 6. Перетворюємо словник у список для сортування
        pairs_list = list(pairs.items())

        # 7. Сортуємо пари за кількістю входжень (від більшого до меншого)
        pairs_list.sort(key=lambda x: x[1], reverse=True)

        # 8. Беремо тільки перші 3 пари
        top3 = pairs_list[:3]

        # 9. Перетворюємо назад у словник, бо так зручніше повертати
        top3_dict = {}
        for p, c in top3:
            top3_dict[p] = c

        # 10. Повертаємо номер рядка і словник із трьома парами
        yield line_number, top3_dict

    f.close()  # Закриваємо файл
