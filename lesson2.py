import warnings

import dotenv
import os

from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

warnings.filterwarnings('ignore') #ігнорувати ворнінги
dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mistral-7B-Instruct-v0.3',
    temperature = 0.3
)

# response = llm('How are you?')
# print(response)
#
#
# response = llm.invoke('[INST]How are you?[/INST]')
# print(response)

# Prompt
# інструкція
# контекст
# дані користувача
# формат відповіді

# аналіз тональності
#
# визначити чи є тональність тексту позитивною,
# негативною чи нейтральною

# prompt = PromptTemplate.from_template ("""
# Ти класифікатор текстів. Твоя задача віднести текст до одного з класів: позитивний, негативний, нейтральний.
# Відповідь має бути одним словом з трьох.
#
# Приклад 1:
# Користувач: Чудове відео, мені неймовірно сподобалося
# Модель: позитивний
#
# Приклад 2:
# Користувач: дарма витратив час на це
# Модель: негативний
#
# Приклад 3:
# Користувач: непогано, на один вечір підійде
# Модель: нейтральний
#
# Користувач: {user_data}
# Модель:
# """)
# # response = llm.invoke(prompt)
# # print(response)
# #
# data = input("Введіть свій коментар: ")
# # формуємо промпт для конкретного повідомленя
# user_prompt = prompt.format(user_data=data)
#
# response = llm.invoke(user_prompt)
# print(f"Результат: {response}")

# Завдання 1
# Напишіть промпт для генерації коду функції для
# вирішення певної задачі.
# Вхідні параметри – мова програмування, опис задачі
# Реалізуйте двома способами:
#  Zero-shot
#  Few-shot

# prompt = PromptTemplate.from_template("""
# [INST]Ти програміст. Твоя задача полягає в написанні простих функцій.[/INST]
#
# [INST]Умова: {user_task}
# Мова програмування: {user_mova}
#
# Виконання:
# [/INST]
# """)
# user_task = input("Введіть, яка функція вам необхідна: ")
# user_mova = input("Введіть мову програмування: ")
#
# result = prompt.format(user_task = user_task, user_mova = user_mova)
#
# response = llm.invoke(result)
# print(f"Результат: {response}")
import random
def gener_numb():
    numb = random.randint(1, 10)
    return numb

prompt = PromptTemplate.from_template("""
[INST]Ти програміст. Твоя задача полягає в написанні простих функцій. В результаті має бути лише код.

Приклад 1:
Умова: функція генерації чисел
Мова програмування: Python
Виконання:
``` python
import random
def gener_numb():
    numb = random.randint(1, 10)
    return numb
```
##
    
Приклад 2:
Умова: середнє арифметичне списку чисел
Мова програмування: Python
Виконання:
``` python
def average_list(numbers):
    sum_numbers = sum(numbers)
    avg = sum_numbers / len(numbers)
    return avg
```
[/INST] 

[INST]Умова: {user_task} 
Мова програмування: {user_mova}

Виконання:
```{user_mova}
```
[/INST]
""")
user_task = input("Введіть, яка функція вам необхідна: ")
user_mova = input("Введіть мову програмування: ")

result = prompt.format(user_task = user_task, user_mova = user_mova)

response = llm.invoke(result)
print(f"Результат: {response}")