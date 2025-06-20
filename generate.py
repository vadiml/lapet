import pandas as pd
import numpy as np
import huggingface_hub
from lapet import ModelHandler, Llama2ModelHandler, Llama3ModelHandler,Llama31ModelHandler, Phi4ModelHandler, GemmaModelHandler, LiteLLMModelHandler

config = {
    'batch_size': 5,
    'max_length': 1500,
    'max_new_tokens': 500,
    'temperature': 0.6,
    'top_p': 0.9,
    'dataset': 'https://huggingface.co/datasets/talkmap/telecom-conversation-corpus/resolve/main/telecom_200k.csv',
    'samples': 5,
    'models': {
        'meta-llama/Llama-2-7b-chat-hf': Llama2ModelHandler,
        'meta-llama/Meta-Llama-3-8B-Instruct': Llama3ModelHandler,
        'meta-llama/Llama-3.1-8B-Instruct': Llama31ModelHandler,
        'meta-llama/Llama-3.2-3B-Instruct': Llama31ModelHandler,
        'microsoft/Phi-3-mini-4k-instruct': ModelHandler,
        'microsoft/Phi-3.5-mini-instruct': Phi4ModelHandler,
        'microsoft/phi-4-mini-instruct': Phi4ModelHandler,
        'HuggingFaceH4/zephyr-7b-beta': ModelHandler,
        'google/gemma-7b': ModelHandler,
        'google/gemma-3-1b-it': GemmaModelHandler,
        'google/gemma-3-4b-it': GemmaModelHandler,
        # 'ollama_chat/llama3.1:8b': LiteLLMModelHandler,
        # 'ollama_chat/phi3:14b': LiteLLMModelHandler,
        # 'ollama_chat/phi4-mini:latest': LiteLLMModelHandler,
        # 'ollama_chat/gemma3:12b': LiteLLMModelHandler,
        # 'together_ai/meta-llama/Llama-4-Scout-17B-16E-Instruct': LiteLLMModelHandler,
        # 'together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo-Free': LiteLLMModelHandler,
    },
    'system_prompt': "You are a helpful AI assistant that generates answers to questions. You will be provided with transcripts of conversations between customers and service agents. Your task is to follow the instruction and output a response from each conversation in a valid JSON format. Focus on provided concise outputs that could be useful for follow-up actions and ensure that your outputs are directly relevant to the discussed topics. This prompt is meant to ensure that you understand the essence of the customer's concerns and can articulate it succinctly in a structured format that is easy for both human and machine processing. Continue with this approach for the upcoming conversations.",
    'prompts': [
        {'name': 'intent-sentence','prompt': 'In a sentence, describe the customer\'s goal of the conversation. Format the output in JSON using the following format: { "intent-sentence": "<OUTPUT>" } where <OUTPUT> is the sentence. Be concise.'},
        {'name': 'intent-label','prompt': 'Create a two two four word label for the customer\'s goal where the first word is a verb and the second word is a noun. Format the output in JSON using the following format: { "intent-label": "<OUTPUT>" } where "<OUTPUT> is the label. Be concise.'},
        {'name': 'customer-sentiment','prompt': 'What is the customer\'s sentiment? Pick one: Positive, Neutral, Negative.  Format the output in JSON using the following format: { "customer-sentiment": "<OUTPUT>" } where <OUTPUT> is the sentiment. Be concise.'},
        {'name': 'agent-empathy','prompt': 'What was the agent\'s level of empathy? Pick one: Poor, Average, High.  Format the output in JSON using the following format: { "agent-empathy": "<OUTPUT>" } where <OUTPUT> is the agent\'s empathy. Be concise.'},
        {'name': 'outcome','prompt': 'Did the customer achieve their goal? Yes or no.  Format the output in JSON using the following format: { "outcome": "<OUTPUT>"  } where <OUTPUT> is the answer to the question. Be concise.'},
        {'name': 'summary','prompt': 'In a sentence, write a summary of the conversation in a paragraph format including a description of the customer\'s goal, the actions that the agent took to help the customer meet their goal, and whether the customer was able to achieve their goal.  Format the output in JSON using the following format: { "summary": "<OUTPUT>" } where <OUTPUT> is the summary. Be concise.'}
    ]
}

# huggingface_hub.login()
# retrieve token from HF_TOKEN environment variable
handler = ModelHandler(config)
responses = handler.process_dataset()
responses.to_csv('eval_data.csv', index=False)

