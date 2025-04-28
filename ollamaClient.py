import requests

def generate_code(prompt: str):
    system_prompt = (
        "Sen bir Python kod üreticisisin. "
        "Kullanıcının isteğine göre önce bir başlık üret, sonra sadece Python kod bloğu döndür. "
        "Başlığı `Title: ...` şeklinde başlat. "
        "Kod bloğu şu yapıda olmalı:\n\n"
        "from s4e.config import *\n"
        "from s4e.task import Task\n\n"
        "class Job(Task):\n"
        "    def run(self):\n"
        "        # Kullanıcının istediği işlem burada yapılacak\n\n"
        "    def calculate_score(self):\n"
        "        # 0-10 arası bir skor hesaplanacak, mantıklı bir skor döndür.\n\n"
        "Kod bloğunu ```python ile başlat ve ``` ile bitir."
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

    lines = output.splitlines()
    title = next((l.replace("Title:", "").strip() for l in lines if l.startswith("Title:")), "No title")

    code_lines = []
    recording = False
    for line in lines:
        if line.strip() == "```python":
            recording = True
            continue
        elif line.strip() == "```" and recording:
            break
        if recording:
            code_lines.append(line)

    code = "\n".join(code_lines)
    return title, code
