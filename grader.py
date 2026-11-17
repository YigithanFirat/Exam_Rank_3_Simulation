import os
import sys
import json
import subprocess
import ast

def grade_question(question_data):
    filename = question_data["filename"]
    func_name = question_data["name"]
    tests = question_data["tests"]
    filepath = os.path.join("rendu", filename)

    # 1. Dosya var mı kontrolü
    if not os.path.exists(filepath):
        return False, f"Hata: {filename} dosyası './rendu/' dizininde bulunamadı!"

    # 2. Yasaklı Fonksiyon Denetimi (AST ile)
    # Öğrenci list.sort() veya sorted() kullandıysa baştan eliyoruz
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source_code = f.read()
            tree = ast.parse(source_code, filename=filepath)
            
            for node in ast.walk(tree):
                # Fonksiyon çağrısı (Call) düğümlerini kontrol et
                if isinstance(node, ast.Call):
                    # sorted() kontrolü
                    if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                        return False, "❌ MOULINETTE BAŞARISIZ: Yasaklı fonksiyon (sorted) kullanımı tespit edildi!"
                    # list.sort() metod kontrolü
                    elif isinstance(node.func, ast.Attribute) and node.func.attr == "sort":
                        return False, "❌ MOULINETTE BAŞARISIZ: Yasaklı metod (.sort) kullanımı tespit edildi!"
    except SyntaxError:
        return False, "❌ MOULINETTE BAŞARISIZ: Yazdığın kodda sözdizimi (Syntax) hatası var!"
    except Exception as e:
        return False, f"❌ AST Denetim Hatası: {e}"

    # 3. Testleri çalıştıracak geçici bir betik (runner) oluşturuyoruz
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
        
        # Kullanıcının fonksiyonunu parametrelerle çalıştır (*args sayesinde argümanları açıyoruz)
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
    python_cmd = sys.executable 
    process = subprocess.run([python_cmd, "_runner.py"], capture_output=True, text=True)
    
    # İşimiz bitince geçici dosyayı temizle
    if os.path.exists("_runner.py"):
        os.remove("_runner.py")

    # 4. Sonuçları değerlendir
    if process.returncode == 0 and "SUCCESS" in process.stdout:
        return True, "✅ Mükemmel! Moulinette kodunu onayladı."
    else:
        return False, f"❌ MOULINETTE BAŞARISIZ:\n{process.stdout.strip()}"
