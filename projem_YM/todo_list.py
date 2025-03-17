print("------------------------------")
def main():
    tasks = []

    while True:
        print("\nYapılacaklar Listesi")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Tüm Görevleri Sil")
        print("4. Çıkış")

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
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "_main_":
    main()