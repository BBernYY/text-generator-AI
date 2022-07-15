from transformers import pipeline
from settings import model, generate

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-'+model['params'])
res = generator(**generate)

open("output.txt", "w").write(res[0]['generated_text'])