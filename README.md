# Yapay Zekâ Destekli Kod Üretici Uygulaması

Bu proje, bir kullanıcıdan alınan prompt (istek) ile yapay zekâ destekli Python kodu üreten bir web uygulamasıdır. Uygulama, kullanıcıya Python kodu üretir ve bu kodun kısa ve anlamlı bir başlığını döndürür.

## Proje Hakkında
Bu proje, Ollama kullanarak, kullanıcının girdiği bir prompt'a dayalı olarak Python kodu üretir. Üretilen kod, bir API aracılığıyla Flask web sunucusuna gönderilir ve web arayüzünde kullanıcıya gösterilir.

## Teknolojiler
- **Flask**: Python web framework'ü.
- **Ollama** (veya benzeri bir LLM API'si): Yapay zekâ destekli model.

## Kurulum ve Çalıştırma
### 1. Gereksinimler
- **Python 3.10 veya üzeri**: Python bağımlılıklarını çalıştırabilmek için gereklidir.

### 2. Adımlar
- Terminalden app.py dosyasını çalıştırmak yeterli.

#### a) Uygulamanın Çalıştırılması (Yerel Ortamda)
1. **Gerekli Python paketlerini yükleyin**:
   ```bash
   pip install -r requirements.txt
