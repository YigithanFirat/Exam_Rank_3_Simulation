import os
import sys
import json
import subprocess
import ast
import time

COOLDOWN_FILE = ".cooldown.json"
COOLDOWN_DURATION = 120


def get_remaining_cooldown():
    """Eğer bir bekleme süresi varsa, kalan süreyi saniye cinsinden döndürür."""
    if os.path.exists(COOLDOWN_FILE):
        try:
            with open(COOLDOWN_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                last_fail_time = data.get("last_fail_time", 0)
                elapsed = time.time() - last_fail_time
                
                if elapsed < COOLDOWN_DURATION:
                    return int(COOLDOWN_DURATION - elapsed)
        except Exception:
            pass
    return 0


def apply_cooldown():
    """Başarısızlık durumunda şu anki zamanı ceza dosyasına yazar."""
    with open(COOLDOWN_FILE, "w", encoding="utf-8") as f:
        json.dump({"last_fail_time": time.time()}, f)


def clear_cooldown():
    """Başarılı olunduğunda veya ceza bittiğinde dosyayı temizler."""
    if os.path.exists(COOLDOWN_FILE):
        os.remove(COOLDOWN_FILE)


def grade_question(question_data):
    remaining_time = get_remaining_cooldown()
    if remaining_time > 0:
        minutes, seconds = divmod(remaining_time, 60)
        return False, f"⏳ MOULINETTE MEŞGUL: Önceki başarsız denemeden dolayı beklemen gerekiyor.\nKalan süre: {minutes} dakika {seconds} saniye."

    filename = question_data["filename"]
    func_name = question_data["name"]
    tests = question_data["tests"]
    filepath = os.path.join("rendu", filename)
    if not os.path.exists(filepath):
        apply_cooldown()
        return False, f"Hata: {filename} dosyası './rendu/' dizininde "
    "bulunamadı!"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source_code = f.read()
            tree = ast.parse(source_code, filename=filepath)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                        apply_cooldown()
                        return False, "❌ MOULINETTE BAŞARISIZ: Yasaklı fonksiyon (sorted) kullanımı tespit edildi!"
                    elif isinstance(node.func, ast.Attribute) and node.func.attr == "sort":
                        apply_cooldown() # Ceza uygula
                        return False, "❌ MOULINETTE BAŞARISIZ: Yasaklı metod (.sort) kullanımı tespit edildi!"
    except SyntaxError:
        apply_cooldown() # Ceza uygula
        return False, "❌ MOULINETTE BAŞARISIZ: Yazdığın kodda sözdizimi (Syntax) hatası var!"
    except Exception as e:
        apply_cooldown() # Ceza uygula
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
        args = json.loads(test["input"]) 
        expected = eval(test["expected"]) 
        
        result = {func_name}(*args)
        
        if result != expected:
            print(f"Test {{i}} BAŞARISIZ! Girdi: {{args}} | Beklenen: {{expected}} | Senin Sonucun: {{result}}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Test {{i}} sırasında çökme yaşandı (Exception): {{e}}")
        sys.exit(1)

print("SUCCESS")
"""
    with open("_runner.py", "w", encoding="utf-8") as f:
        f.write(runner_code)
        
    python_cmd = sys.executable 
    process = subprocess.run([python_cmd, "_runner.py"], capture_output=True, text=True)
    
    if os.path.exists("_runner.py"):
        os.remove("_runner.py")

    # 4. Sonuçları değerlendir
    if process.returncode == 0 and "SUCCESS" in process.stdout:
        clear_cooldown() # Başarılı teslim! Cezayı kaldır.
        return True, "✅ Mükemmel! Moulinette kodunu onayladı."
    else:
        apply_cooldown() # Testlerden biri patladı, ceza uygula.
        return False, f"❌ MOULINETTE BAŞARISIZ:\n{process.stdout.strip()}"
