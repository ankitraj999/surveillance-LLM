# -*- coding: utf-8 -*-
"""openai-api-module.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A76Vd74TjO8XewgNVnfL_wmmzTZGB62t
"""

#@title Open AI Module

# install from PyPI
#!pip install openai

#@title Configure Open API key
from openai import OpenAI
#from google.colab import userdata
import os
#save openai access key in notebook secret by name =openAIsecretKey  and provide acess to the notebook
#open_api_secret_name = 'openAIsecretKey'  # @param {type: "string"}

try:
  OPEN_API_KEY=os.environ.get('OPEN_API_KEY')
  client=OpenAI(api_key=OPEN_API_KEY)
# except userdata.SecretNotFoundError as e:
#    print(f'Secret not found\n\nThis expects you to create a secret named {open_api_secret_name} in Colab')
#    raise e
# except userdata.NotebookAccessError as e:
#   print(f'You need to grant this notebook access to the {open_api_secret_name} secret in order for the notebook to access openai on your behalf.')
#   raise e
except Exception as e:
  # unknown error
  print(f"There was an unknown error.")
  raise e


#@title Open AI Model Prompt Creation
model="gpt-3.5-turbo"
descriptionQuery="image of a ghostly woman with a veil and glowing eyes"
def openaiInference(model,descriptionQuery):
  completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "you are a security observer. An image was clicked by suvelliance camer you get the {description} from the image create an announcement raising security threat if you find something life threatening , otherwise just brief the description without raising any threat alarm."
    },
    {"role": "user", "content":f"{descriptionQuery}"}
    ]
    )

  return completion.choices[0].message.content.split("\n")

result = openaiInference(model,descriptionQuery)

print(" ".join(result))
