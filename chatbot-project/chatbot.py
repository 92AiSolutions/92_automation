
---

### 2. **`chatbot-project/`**

#### **`chatbot.py`**
```python
from fastapi import FastAPI
import openai

openai.api_key = 'your-api-key'

app = FastAPI()

@app.post("/chat/")
async def chat(query: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    return {"response": response.choices[0].text.strip()}

