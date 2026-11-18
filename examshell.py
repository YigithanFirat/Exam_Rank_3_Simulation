import json
import os
import sys
import random
import grader
import time
import threading

# 3 Saat = 3 * 60 * 60 = 10800 saniye
EXAM_DURATION = 10800 

def load_pool():
    with open('pool.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    pool = load_pool()
    current_level = 1
    total_score = 0
    current_question = None
    
    # Sınavın başlangıç zamanını kaydet
    start_time = time.time()
    
    # Arka planda süreyi kontrol eden fonksiyon
    def time_checker():
        while True:
            elapsed = time.time() - start_time
            if elapsed >= EXAM_DURATION:
                # Kullanıcı input'ta bekliyor olsa bile programı anında kapatır
                print("\n\n⏳ SINAV SÜRESİ DOLDU (3 Saat)! Sistem otomatik olarak kapatılıyor...")
                print(f"Toplam Puanın: {total_score}/100\n")
                os._exit(0)
            time.sleep(1) # Her 1 saniyede bir kontrol et

    # Zamanlayıcıyı ayrı bir thread (iş parçacığı) olarak başlat
    # daemon=True olması, program normal yollarla kapanırsa bu thread'in de ölmesini sağlar
    timer_thread = threading.Thread(target=time_checker, daemon=True)
    timer_thread.start()

    # rendu klasörünü oluştur
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
            # Kalan süreyi hesapla
            elapsed = time.time() - start_time
            remaining = max(0, EXAM_DURATION - elapsed)
            
            # Saniyeyi Saat:Dakika:Saniye formatına çevir
            hours, remainder = divmod(remaining, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

            print("\n--- DURUM ---")
            print(f"Kalan Süre: {time_str}")
            print(f"Seviye: {current_level} / 6")
            print(f"Puan: {total_score} / 100")
            if current_question:
                print(f"Aktif Görev: {current_question['name']}")
            print("Çalışma Dizini: ./rendu/\n")
            
        elif cmd == "subject":
            if current_level > 6:
                print("\nSınavı zaten tamamladın! 'finish' yazarak çıkabilirsin.\n")
                continue
                
            # Eğer o level için henüz soru atanmadıysa, rastgele bir soru seç
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
                # Puanı ekle ve seviye atla
                points = pool["levels"][str(current_level)]["points"]
                total_score += points
                current_level += 1
                current_question = None # Yeni seviye için soruyu sıfırla
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
