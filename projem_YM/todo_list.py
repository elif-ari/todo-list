def main():
    tasks = []

    while True:
        print("\nYapılacaklar Listesi")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            task = input("Görev girin: ")
            tasks.append(task)
            print(f"'{task}' eklendi.")
        elif secim == "2":
            print("\nYapılacaklar:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif secim == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()