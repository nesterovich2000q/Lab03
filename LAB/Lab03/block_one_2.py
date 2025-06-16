from collections import Counter
import re

# Читаем текст из input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Разбиваем текст на слова (учитываем только буквы и цифры)
words = re.findall(r'\b\w+\b', text)

# Считаем частоту каждого слова
counter = Counter(words)

# Берём 3 самых частых слова
top_three = counter.most_common(3)

# Формируем результат
result_lines = [f"'{word}' встречается {count} раз(а)" for word, count in top_three]
result_text = "Три самых частых слова:\n" + "\n".join(result_lines)

# Записываем результат в output.txt
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(result_text)

print(result_text)
