import json
import os
import sys
import random
import grader
import time
import threading
import shutil

EXAM_DURATION = 10800


def load_pool():
    with open('pool.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def clean_up():
    """Çıkışta rendu, __pycache__ klasörlerini ve bekleme süresi dosyasını
    temizler."""
    if os.path.exists("rendu"):
        shutil.rmtree("rendu")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    if os.path.exists(".cooldown.json"):
        os.remove(".cooldown.json")


def main():
    pool = load_pool()
    current_level = 1
    total_score = 0
    current_question = None
    start_time = time.time()

    def time_checker():
        while True:
            elapsed = time.time() - start_time
            if elapsed >= EXAM_DURATION:

                print("\n\n⏳ SINAV SÜRESİ DOLDU (3 Saat)! Sistem otomatik "
                      "olarak kapatılıyor...")
                print(f"Toplam Puanın: {total_score}/100\n")
                clean_up()
                os._exit(0)
            time.sleep(1)
    timer_thread = threading.Thread(target=time_checker, daemon=True)
    timer_thread.start()
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
            clean_up()
            break
        if cmd == "status":
            elapsed = time.time() - start_time
            remaining = max(0, EXAM_DURATION - elapsed)
            hours, remainder = divmod(remaining, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{int(hours):02d}:{int(minutes):02d}:"
            f"{int(seconds):02d}"
            print("\n--- DURUM ---")
            print(f"Kalan Süre: {time_str}")
            print(f"Seviye: {current_level} / 6")
            print(f"Puan: {total_score} / 100")
            if current_question:
                print(f"Aktif Görev: {current_question['name']}")
            print("Çalışma Dizini: ./rendu/\n")
        elif cmd == "subject":
            if current_level > 6:
                print("\nSınavı zaten tamamladın! 'finish' yazarak "
                      "çıkabilirsin.\n")
                continue
            if current_question is None:
                level_data = pool["levels"][str(current_level)]
                current_question = random.choice(level_data["questions"])
            print("\n================ GÖREV ================")
            print(f"Soru: {current_question['name']}")
            print(f"Dosya Adı: {current_question['filename']}")
            print(f"Beklenen Şablon:\n{current_question['prototype']}")
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
                print(f"\n🎉 TEBRİKLER! Seviye atladın. Yeni Puan: "
                      f"{total_score}")
                if current_level > 6:
                    print("\n🏆 BÜTÜN SEVİYELERİ GEÇTİN! 100 TAM PUAN! Sınav "
                          "bitti.")
            print("")

        elif cmd == "finish":
            print("Sınavdan çıkmak istediğine emin misin? (y/n)")
            ans = input("> ").strip().lower()
            if ans == 'y':
                print(f"Sınav sonlandırıldı. Toplam Puan: {total_score}/100")
                clean_up()
                sys.exit(0)
        elif cmd == "":
            continue
        else:
            print("Bilinmeyen komut. Komutlar: subject, status, grademe, "
                  "finish")


if __name__ == "__main__":
    main()
