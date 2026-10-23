# Kapiyi Kapat Kapiyi Ac Simulatoru
# Dünyanın en ciddi ve en saçma kapı açma-kapama simülasyonu
# Bu kod GERÇEKTEN çalışır. Dikkatli olun, kapılar açılabilir.

import time
import random
import sys

def dramatik_cikis():
    print("\n⚠️  UYARI: Bu simülatör o kadar gerçekçi ki gerçek kapıları da etkileyebilir!")
    print("Lütfen simülasyonu durdurmak için Ctrl+C yapın... ya da yapmayın.")

def kapi_durumu():
    durumlar = [
        "KAPI KAPALI... İçeride biri mi var acaba?",
        "KAPI AÇILIYOR... Yavaş yavaş, çok yavaş...",
        "KAPI AÇIK! Dışarıda rüzgar esiyor, felsefe yapıyor.",
        "KAPI KAPANMAYA BAŞLIYOR... Dramatik müzik çalıyor.",
        "KAPI TAMAMEN KAPANDI. Sessizlik. Derin sessizlik.",
        "KAPI GICIRDADI. Ruhlar ürperdi."
    ]
    return random.choice(durumlar)

def main():
    print("=" * 60)
    print("   KAPIYI KAPAT KAPIYI AÇ SİMÜLATÖRÜ v1.0")
    print("   Resmi Olmayan Resmi Kapı Araştırma Merkezi")
    print("=" * 60)
    print("\nSimülasyon başlıyor... Lütfen yerinizi alın.\n")
    
    sayac = 0
    try:
        while True:
            sayac += 1
            print(f"[{sayac}] {kapi_durumu()}")
            bekleme = random.uniform(1.5, 4.0)
            print(f"   (Bekleniyor: {bekleme:.1f} saniye - çünkü kapılar aceleyi sevmez)")
            time.sleep(bekleme)
            if sayac % 7 == 0:
                print("\n🤔 Felsefi Ara: Kapı açılmadan önce mi vardı, yoksa açıldıktan sonra mı?\n")
            # Gizli not: bürokrasi de böyle kapılar açar kapatır, sürekli.
    except KeyboardInterrupt:
        print("\n\nSimülasyon kullanıcı tarafından durduruldu.")
        print("Kapı şu an ne durumda? Bilinmiyor. Belki de hiç açılmadı.")
        dramatik_cikis()

if __name__ == "__main__":
    main()
