from fastapi import FastAPI, Request, Response
from transformers import AutoModelForCausalLM, AutoTokenizer 

app= FastAPI()

# tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-zephyr-3b")
# model = AutoModelForCausalLM.from_pretrained("stabilityai/stablelm-zephyr-3b", device_map="auto")

@app.get("/")
def home():
    return{"chat", "bot"}

@app.get("/ask")
def ask(prompt):
    res = requests.post('http//ollama:11434/api/generate',
                        json ={"prompt": prompt, 
                        "stream": False,
                        "model": "llama3"})
    return Response(co)
# @app.post("/generat")
# def generate(request, input_data):
#     prompt = [{'role': 'user', 'content': input_data}]
#     inputs = tokenizer.appyl_chat_template(prompt, add_genration_promp=False,
#                                          return_tensor="pt")
#     prompt_length = inputs[0].shape[0]
#     tokens = model.generate(inputs.to(model.device), max_new_tokens=1024, temprature=0.8, do_sample= True)
#     response = tokenizer.decode(tokens[0][prompt_length:], skip_special_tokens=True)

#     return response