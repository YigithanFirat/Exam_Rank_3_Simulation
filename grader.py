import os
import sys
import json
import subprocess

def grade_question(question_data):
    filename = question_data["filename"]
    func_name = question_data["name"]
    tests = question_data["tests"]
    filepath = os.path.join("rendu", filename)

    # 1. Dosya var mı kontrolü
    if not os.path.exists(filepath):
        return False, f"Hata: {filename} dosyası './rendu/' dizininde bulunamadı!"

    # 2. Testleri çalıştıracak geçici bir betik (runner) oluşturuyoruz
    # Bu betik, kullanıcının kodunu import edip test case'leri deneyecek.
    runner_code = f"""
import sys
import json
sys.path.insert(0, './rendu')

try:
    from {filename[:-3]} import {func_name}
except ImportError:
    print("HATA: {func_name} fonksiyonu {filename} içinde bulunamadı veya import edilemedi!")
    sys.exit(1)
except Exception as e:
    print(f"HATA (Sözdizimi/Çalıştırma): {{e}}")
    sys.exit(1)

tests = {json.dumps(tests)}

for i, test in enumerate(tests, 1):
    try:
        # JSON'dan string olarak gelen listeyi gerçek Python listesine çevir
        args = json.loads(test["input"]) 
        expected = eval(test["expected"]) # Beklenen sonucu Python objesine çevir
        
        # Kullanıcının fonksiyonunu parametrelerle çalıştır
        result = {func_name}(*args)
        
        if result != expected:
            print(f"Test {{i}} BAŞARISIZ! Girdi: {{args}} | Beklenen: {{expected}} | Senin Sonucun: {{result}}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Test {{i}} sırasında çökme yaşandı (Exception): {{e}}")
        sys.exit(1)

print("SUCCESS")
"""
    # Geçici runner dosyasını yaz
    with open("_runner.py", "w", encoding="utf-8") as f:
        f.write(runner_code)
        
    # Alt süreç (subprocess) olarak runner'ı çalıştır
    # (İşletim sistemine göre python veya python3 komutu gerekebilir)
    python_cmd = sys.executable 
    process = subprocess.run([python_cmd, "_runner.py"], capture_output=True, text=True)
    
    # İşimiz bitince geçici dosyayı sil
    if os.path.exists("_runner.py"):
        os.remove("_runner.py")

    # 3. Sonuçları değerlendir
    if process.returncode == 0 and "SUCCESS" in process.stdout:
        return True, "✅ Mükemmel! Moulinette kodunu onayladı."
    else:
        return False, f"❌ MOULINETTE BAŞARISIZ:\n{process.stdout.strip()}"
    