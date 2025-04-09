import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
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

# print(llm.invoke('Привіт'))

# messages = [
#     SystemMessage(content='Ти ввічливий чат бот.'
#                   'Давай короткі та чіткі відповіді.')
#     HumanMessage(content='Привіт, я Алла.'),
#     AIMessage(content='Привіт. Чим можу допомогти?'),
#     HumanMessage(content='Яка столиця Франції?'),
#     AIMessage(content='Столиця Франції - Париж.'),
#     HumanMessage(content='Яка мене звати?'),
# ]

messages = [
    SystemMessage(content='Ти чат бот, який дає відповіді.'
                  'Давай короткі відповіді і додай цікаві факти.'),
    HumanMessage(content='Привіт, я Алла.'),
    AIMessage(content='Привіт. Чим можу допомогти?'),
    HumanMessage(content='Яка столиця Франції?'),
    AIMessage(content='Столиця Франції - Париж.'),
    HumanMessage(content='Яка мене звати?'),
]

trimmer = trim_messages(
    strategy='last', #залишати останні повідомлення
    token_counter=len,
    max_tokens=5, #залишати максимум 3 повідомлення
    start_on='human', #історія завжди почин з
    end_on='human', #історія завжди закінч
    include_system=True #SystemMessage не чіпати
)

while True:
    user_input = input("Ви: ")

    if user_input == '':
        break

    #створити human message
    human_message = HumanMessage(content=user_input)

    messages.append(human_message)

    messages = trimmer.invoke(messages)

    response = llm.invoke(messages)

    messages.append(response)

    print(f'AI: {response.content}')

    print(messages)

response = llm.invoke(messages)
print(response)
