from openai import OpenAI

def get_bio_openai(brand, model, year):
    client = OpenAI(api_key = "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",)

    prompt = f"mostrar descricao do carro {brand} {model} {year}, com no maximo 250 caracteres, incluindo especificacoes tecnicas"

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": prompt}
    ],
    max_tokens=1000
    )
    return response.choices[0].message.content
