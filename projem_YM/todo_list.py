print("------------------------------------")
import os

DOSYA_ADI = "gorevler.txt"

def gorevleri_kaydet(tasks):
    """Mevcut görevleri dosyaya kaydeder."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        for task in tasks:
            dosya.write(task + "\n")
    print("\nGörevler başarıyla kaydedildi!")

def main():
    tasks = []

    while True:
        print("\nYapılacaklar Listesi")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Tüm Görevleri Sil")
        print("4. Çıkış")
        print("5. Görevleri Kaydet")
        print("6. Görevi Düzenle")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            task = input("Görev girin: ")
            tasks.append(task)
            print(f"'{task}' eklendi.")
        elif secim == "2":
            if tasks:
                print("\nYapılacaklar:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("\nListe boş.")
        elif secim == "3":
            if tasks:
                tasks.clear()
                print("\nTüm görevler silindi!")
            else:
                print("\nZaten görev yok.")
        elif secim == "4":
            print("Çıkılıyor...")
            break
        elif secim == "5":
            if tasks:
                gorevleri_kaydet(tasks)
            else:
                print("\nKaydedilecek görev yok.")
        elif secim == "6":
            if tasks:
                print("\nDüzenlemek istediğiniz görevin numarasını girin:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                
                try:
                    index = int(input("Görev numarası: ")) - 1
                    if 0 <= index < len(tasks):
                        yeni_gorev = input("Yeni görev metnini girin: ")
                        tasks[index] = yeni_gorev
                        print("\nGörev başarıyla güncellendi!")
                    else:
                        print("\nGeçersiz görev numarası!")
                except ValueError:
                    print("\nLütfen geçerli bir sayı girin!")
            else:
                print("\nDüzenlenecek görev yok.")
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
