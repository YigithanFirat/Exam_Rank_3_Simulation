# 42 Exam Rank 03 Simulator 💻🎓

[English](#english) | [Türkçe](#türkçe)

---

<a id="english"></a>
## 🇬🇧 English

### About The Project
This project is a custom-built, CLI-based simulator that mimics the real **42 School's `examshell`** environment. It is specifically designed for the **Exam Rank 03 (Python)** module. The simulator provides a complete exam experience with an automated grading system (Moulinette), dynamic subject assignment, and a leveling system.

### Project Structure
To run this project, extract the code blocks below into their respective files in the same directory:
1. `pool.json` (Database)
2. `examshell.py` (Main CLI)
3. `grader.py` (Test Engine)

---

<a id="türkçe"></a>
## 🇹🇷 Türkçe

### Proje Hakkında
Bu proje, gerçek **42 Okulları'nın `examshell`** ortamını taklit eden, tamamen Python ile yazılmış CLI (Komut Satırı Arayüzü) tabanlı bir simülatördür. **Exam Rank 03 (Python)** modülü için özel olarak tasarlanmıştır.

### Proje Yapısı
Bu projeyi çalıştırmak için aşağıdaki kod bloklarını aynı dizin (klasör) içerisinde kendi isimleriyle oluşturmalısınız:
1. `pool.json` (Soru veritabanı)
2. `examshell.py` (Ana sınav ekranı)
3. `grader.py` (Moulinette test motoru)

---
<br>

## 📂 1. Dosya: `pool.json`
Bu dosya soruları, puanları ve gizli test senaryolarını barındırır. Yeni soruları buraya ekleyebilirsiniz.

```json
{
  "levels": {
    "1": {
      "points": 16,
      "questions": [
        {
          "name": "py_bracket_validator",
          "filename": "py_bracket_validator.py",
          "subject": "Bir dize alan ve içerisindeki parantezlerin (), [], {} doğru şekilde açılıp kapandığını doğrulayan bir fonksiyon yazın. Doğruysa True, yanlışsa False döndürsün.",
          "tests": [
            {"input": "[\"()[]{}\"]", "expected": "True"},
            {"input": "[\"([)]\"]", "expected": "False"},
            {"input": "[\"{[()]}\"]", "expected": "True"}
          ]
        },
        {
          "name": "py_cryptic_sorter",
          "filename": "py_cryptic_sorter.py",
          "subject": "Verilen bir sayı listesini özel bir mantığa göre sıralayan bir fonksiyon yazın. (Örn: Önce çift sayılar, sonra tek sayılar kendi içlerinde artan şekilde).",
          "tests": [
            {"input": "[[3, 1, 2, 4]]", "expected": "[2, 4, 1, 3]"}
          ]
        }
      ]
    },
    "2": {
      "points": 16,
      "questions": [
        {
          "name": "py_echo_validator",
          "filename": "py_echo_validator.py",
          "subject": "Verilen bir dizenin belirli bir deseni tekrar edip etmediğini kontrol eden bir fonksiyon yazın.",
          "tests": [
            {"input": "[\"ababab\"]", "expected": "True"},
            {"input": "[\"hello\"]", "expected": "False"}
          ]
        },
        {
          "name": "py_mirror_matrix",
          "filename": "py_mirror_matrix.py",
          "subject": "2 boyutlu bir matrisi (listelerin listesi) dikey eksende yansıtan (ters çeviren) bir fonksiyon yazın.",
          "tests": [
            {"input": "[[[1, 2], [3, 4]]]", "expected": "[[2, 1], [4, 3]]"}
          ]
        }
      ]
    },
    "3": {
      "points": 16,
      "questions": [
        {
          "name": "py_hidenp",
          "filename": "py_hidenp.py",
          "subject": "İlk dizenin, ikinci dizenin içinde (karakter sırasını bozmadan) gizlenip gizlenmediğini kontrol eden bir fonksiyon yazın. Gizlenmişse True, aksi halde False döndürün.",
          "tests": [
            {"input": "[\"fgex.;\", \"tyf34gdgf;'ektufjhgdgex.;.;;vj\"]", "expected": "True"},
            {"input": "[\"abc\", \"btarc\"]", "expected": "False"}
          ]
        },
        {
          "name": "py_inter",
          "filename": "py_inter.py",
          "subject": "İki dize alan ve her ikisinde de bulunan karakterleri, ilk dizede göründükleri sırayla (tekrarsız olarak) döndüren bir fonksiyon yazın.",
          "tests": [
            {"input": "[\"padinton\", \"paqefwtdjetyiytjneytjoeyjntoeynt\"]", "expected": "\"padinto\""}
          ]
        },
        {
          "name": "py_number_base_converter",
          "filename": "py_number_base_converter.py",
          "subject": "10'luk tabandaki bir tam sayıyı, verilen herhangi bir tabana (2 ile 16 arası) dönüştüren bir fonksiyon yazın.",
          "tests": [
            {"input": "[255, 16]", "expected": "\"FF\""},
            {"input": "[10, 2]", "expected": "\"1010\""}
          ]
        },
        {
          "name": "py_pattern_tracker",
          "filename": "py_pattern_tracker.py",
          "subject": "Bir dize içerisindeki tekrar eden en uzun alt deseni bulan bir fonksiyon yazın.",
          "tests": [
            {"input": "[\"aabaabaaba\"]", "expected": "\"aab\""}
          ]
        }
      ]
    },
    "4": {
      "points": 16,
      "questions": [
        {
          "name": "py_anagram",
          "filename": "py_anagram.py",
          "subject": "İki dizenin birbirinin anagramı (harflerinin yer değiştirmiş hali) olup olmadığını kontrol eden bir fonksiyon yazın. Boşlukları ve büyük/küçük harfi göz ardı edin.",
          "tests": [
            {"input": "[\"Listen\", \"Silent\"]", "expected": "True"},
            {"input": "[\"Hello\", \"World\"]", "expected": "False"}
          ]
        },
        {
          "name": "py_shadow_merge",
          "filename": "py_shadow_merge.py",
          "subject": "İki sözlüğü (dictionary) birleştiren bir fonksiyon yazın. Aynı anahtarlar çakışırsa, ikinci sözlüğün değeri ilkini gölgelesin (ezsin). (NOT: Eğer liste birleştirmek istiyorsanız, input formatını listelere uygun hale getirin).",
          "tests": [
            {"input": "[{\"a\": 1, \"b\": 2}, {\"b\": 3, \"c\": 4}]", "expected": "{\"a\": 1, \"b\": 3, \"c\": 4}"}
          ]
        },
        {
          "name": "py_string_permutation_checker",
          "filename": "py_string_permutation_checker.py",
          "subject": "Bir dizenin, başka bir dizenin permütasyonu olup olmadığını kontrol eden bir fonksiyon yazın.",
          "tests": [
            {"input": "[\"abc\", \"bca\"]", "expected": "True"}
          ]
        }
      ]
    },
    "5": {
      "points": 16,
      "questions": [
        {
          "name": "py_string_sculptor",
          "filename": "py_string_sculptor.py",
          "subject": "Yalnızca alfabetik karakterlerin büyük/küçük harf durumunu değiştirerek bir dizeyi dönüştüren bir fonksiyon yazın. Alfabetik olmayanlar indeks sayısını etkilemez. İlk harf küçük, ikincisi büyük olmalıdır vb.",
          "tests": [
            {"input": "[\"hello\"]", "expected": "\"hElLo\""},
            {"input": "[\"abc123def\"]", "expected": "\"aBc123DeF\""}
          ]
        },
        {
          "name": "py_twist_sequence",
          "filename": "py_twist_sequence.py",
          "subject": "Bir sayı listesini k pozisyon kadar sağa döndüren (son k elemanı başa alan) bir fonksiyon yazın.",
          "tests": [
            {"input": "[[1,2,3,4,5], 2]", "expected": "[4,5,1,2,3]"},
            {"input": "[[1,2,3], 5]", "expected": "[2,3,1]"}
          ]
        }
      ]
    },
    "6": {
      "points": 20,
      "questions": [
        {
          "name": "py_whisper_cipher",
          "filename": "py_whisper_cipher.py",
          "subject": "Bir dizedeki harfleri belirli bir miktarda kaydırarak Sezar şifrelemesi oluşturan bir fonksiyon yazın. Negatif kaydırma desteklenmelidir.",
          "tests": [
            {"input": "[\"hello\", 3]", "expected": "\"khoor\""},
            {"input": "[\"abc\", -3]", "expected": "\"xyz\""}
          ]
        }
      ]
    }
  }
}
```

---
<br>

## 📂 2. Dosya: `examshell.py`
Bu dosya simülatörün ana iskeletidir. Terminalde bunu çalıştıracaksınız (`python examshell.py`).

```python
import json
import os
import sys
import random
import grader

def load_pool():
    with open('pool.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    pool = load_pool()
    current_level = 1
    total_score = 0
    current_question = None
    
    if not os.path.exists("rendu"):
        os.makedirs("rendu")

    print("========================================")
    print("      42 EXAM RANK 03 SIMULATOR         ")
    print("========================================")
    print("Komutlar: subject, status, grademe, finish\n")

    while True:
        try:
            cmd = input("examshell> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nSınavdan çıkılıyor...")
            break

        if cmd == "status":
            print(f"\n--- DURUM ---")
            print(f"Seviye: {current_level} / 6")
            print(f"Puan: {total_score} / 100")
            if current_question:
                print(f"Aktif Görev: {current_question['name']}")
            print("Çalışma Dizini: ./rendu/\n")
            
        elif cmd == "subject":
            if current_level > 6:
                print("\nSınavı zaten tamamladın! 'finish' yazarak çıkabilirsin.\n")
                continue
                
            if current_question is None:
                level_data = pool["levels"][str(current_level)]
                current_question = random.choice(level_data["questions"])
            
            print(f"\n================ GÖREV ================")
            print(f"Soru: {current_question['name']}")
            print(f"Dosya Adı: {current_question['filename']}")
            print(f"Görev Metni:\n{current_question['subject']}")
            print("=======================================\n")

        elif cmd == "grademe":
            if current_question is None:
                print("\nÖnce 'subject' komutuyla bir görev almalısın!\n")
                continue
                
            print("\n⏳ Moulinette kodu derliyor ve test ediyor...\n")
            success, message = grader.grade_question(current_question)
            print(message)
            
            if success:
                points = pool["levels"][str(current_level)]["points"]
                total_score += points
                current_level += 1
                current_question = None 
                print(f"\n🎉 TEBRİKLER! Seviye atladın. Yeni Puan: {total_score}")
                
                if current_level > 6:
                    print("\n🏆 BÜTÜN SEVİYELERİ GEÇTİN! 100 TAM PUAN! Sınav bitti.")
            print("")

        elif cmd == "finish":
            print("Sınavdan çıkmak istediğine emin misin? (y/n)")
            ans = input("> ").strip().lower()
            if ans == 'y':
                print(f"Sınav sonlandırıldı. Toplam Puan: {total_score}/100")
                sys.exit(0)
                
        elif cmd == "":
            continue
            
        else:
            print("Bilinmeyen komut. Komutlar: subject, status, grademe, finish")

if __name__ == "__main__":
    main()
```

---
<br>

## 📂 3. Dosya: `grader.py`
Bu dosya arka planda yazdığınız kodları, veritabanındaki test case'ler ile karşılaştıran Moulinette motorudur. (Doğrudan çalıştırmanıza gerek yoktur, `examshell.py` bu dosyayı kullanır).

```python
import os
import sys
import json
import subprocess

def grade_question(question_data):
    filename = question_data["filename"]
    func_name = question_data["name"]
    tests = question_data["tests"]
    filepath = os.path.join("rendu", filename)

    if not os.path.exists(filepath):
        return False, f"Hata: {filename} dosyası './rendu/' dizininde bulunamadı!"

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

    if process.returncode == 0 and "SUCCESS" in process.stdout:
        return True, "✅ Mükemmel! Moulinette kodunu onayladı."
    else:
        return False, f"❌ MOULINETTE BAŞARISIZ:\n{process.stdout.strip()}"
```
