import os
import dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages
)

dotenv.load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=os.getenv('GEMINI_API_KEY')
)

# Завдання 1
# Напишіть функцію яка перевіряє складність паролю:
#  кількість символів(>8)
#  наявність хоча б однієї літери\цифри\спеціального
# символу
#  наявність літер в різних регістрах
# Функція повертає тест з описом паролю(що добре, а що
# погано)
# На основі цієї функції створіть агента.

def check_password(user_password: str):
    """
    Функція для перевірки коректності паролю
    :param
    user_password: str
    :return:
    """
    result = ""
    if len(user_password) >= 8:
        result += "кількість символів > 8, це вірно"
    else:
        result += "кількість символів менша за 8, пароль не надійний"

    alfa_flag = False
    digit_flag = False
    spesial_flag = False

    for letter in user_password:
        if letter.isalpha() and not alfa_flag:
            alfa_flag = True
            result += "\nв паролі є літера"
        elif letter.isdigit() and not digit_flag:
            digit_flag = True
            result += "\nв паролі є цифра"
        elif not spesial_flag and not letter.isalpha() and not letter.isdigit():
            spesial_flag = True
            result += "\nв паролі є спеціальні символи"

    if not alfa_flag:
        result +="\nв паролі відсутні літери"
    if not digit_flag:
        result += "\nв паролі відсутні числа"
    if not spesial_flag:
        result += "\nв паролі відсутні символи"

    return result




# def get_weather(city: str, time: str = 'сьогодні'):
#     """
#     Шукає погоду в мевному місті
#     :param
#         city: str, місто для якого треба знайти прогноз погоди
#         time: str, час на який шукати прогноз погоди.
#             може бути година, наприклад 16:30
#             може бути день, наприклад завтра, сьогодні
#     :return:
#         str, опис погоди в місті
#     """
#     print('hello from get_weather')
#     return f"B {city} сонячно {time}"
#
# def product(a: int, b: int):
#     """
#     Повертає добуток двох чисел
#     :param a:
#     :param b:
#     :return:
#     """
#     print('hello from product')
#     return a*b
#
# # створення інструмента пошуку в інтернеті
#
# search = DuckDuckGoSearchRun()
#
# # створення агента
agent = create_react_agent(model=llm, tools=[check_password])

data_input = {
    'messages': [
        SystemMessage(content='Ти чатбот, ти можеш перевірити пароль на надійність та дати детальний звіт. Кожне речення пиши з нового рядка.')

]}

# response = agent.invoke(data_input)
# # print(response)
#
# for mes in response['messages']:
#     mes.pretty_print()

# консоль для спілкування

while True:
    user_input = input('YOU: ')

    if user_input == "":
        break

    human_message = HumanMessage(content=user_input)

    data_input['messages'].append(human_message)

    response = agent.invoke(data_input)

    data_input = response

    last_message = data_input['messages'][-1]

    print(last_message.content)


