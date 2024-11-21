from openai import OpenAI
import os
from dotenv import load_dotenv
import yaml

#TODO: code clean up
def get_response_openai(input_text, settings):
    """
    Function to get response from OpenAI API.
    :param input_text: string, input of the user text
    :return: string, output of the content
    """
    model_engine = settings["model_engine"]
    client = OpenAI(api_key=os.environ.get('OPENAI_API'))
    sys_prompt = settings["system_prompt"]
    # print(sys_prompt)
    messages = [
        {"role": "system", "content": f"{sys_prompt}"},
        {"role": "user", "content": f"{input_text}"}
    ]
    completion = client.chat.completions.create(model=model_engine,
    messages=messages)
    # print(completion)
    message = completion.choices[0].message.content
    return message


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]


def get_settings(yaml_file):
    """
    Function to load settings, e.g., prompts from yaml file.
    """
    with open(yaml_file, "r") as f:
        settings = yaml.load(f, Loader=yaml.SafeLoader)
    return settings


def main():
    load_dotenv()
    yaml_file = "./prompts.yaml"
    input_text = "What are you guys going to do this weekend?"
    settings = get_settings(yaml_file)
    reply = get_response_openai(input_text, settings)
    print(reply)


if __name__ == '__main__':
    main()
