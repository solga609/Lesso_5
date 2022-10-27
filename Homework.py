
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва



import random

txt = ("абв")
print("Слово, которое необходимо удалить из текста: ", txt)
num_word = (int(input("Количество слов в текте: ")))
list_word = []
print("Любой текст: ")
for x in range(num_word):
    random_txt = random.sample(txt, 3)
    list_word.append(" ".join(random_txt))
    print("Текст без абв: ")
    list_word2 = list(filter(lambda x: txt not in x, list_word))
    print(" ".join(list_word2))
