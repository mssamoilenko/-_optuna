import dotenv
import os

from langchain_huggingface import HuggingFaceEndpoint

dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mistral-7B-Instruct-v0.3',
    # top_k = 3,#вибрати з трьох наймовірніших слів
    # top_p = 0.6, #вибрати серед слів, сума ймовірностей яких дорівнює 60%
    temperature = 10,
    max_new_tokens = 50  #максимальна довжина відповіді
)

#низька температура  <0.3 -- мала креативність, формальність
#висока температура >0.6 -- креативність, більш живі відповіді але менш надійні
#велика темп >1.2 -- галюцинації

response = llm('How are you?')
print(response)

# інструкції в mistral

response = llm.invoke('[INST]How are you?[/INST]')
print(response)

