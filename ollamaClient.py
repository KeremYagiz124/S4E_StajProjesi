# ollamaClient.py
import requests

def generate_code(prompt: str):
    system_prompt = (
        "Sen bir Python kod üreticisisin. "
        "Kullanıcının isteğine göre önce bir başlık üret, sonra sadece Python kod bloğu döndür. "
        "Başlığı `Title: ...` şeklinde başlat. Kod bloğunu ```python ile başlat ve ``` ile bitir."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"{system_prompt}\n\nKullanıcı: {prompt}",
            "stream": False
        }
    )

    output = response.json()["response"]

    # Ayır: title ve code
    lines = output.splitlines()
    title = next((l.replace("Title:", "").strip() for l in lines if l.startswith("Title:")), "No title")
    code_lines = []
    recording = False
    for line in lines:
        if line.strip().startswith("```python"):
            recording = True
            continue
        elif line.strip().startswith("```") and recording:
            break
        if recording:
            code_lines.append(line)

    code = "\n".join(code_lines)
    return title, code
