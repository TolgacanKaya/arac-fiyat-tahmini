import joblib
import pandas as pd

# Modeli yükle
model = joblib.load('fiyat_tahmin_modeli.pkl')

# Kullanıcıdan veri al
def veri_al():
    marka = input("Marka (örnek: Maruti): ")
    model_adi = input("Model Adı (örnek: Swift): ")
    km = float(input("Kilometre (örnek: 35000): "))
    motor = float(input("Motor Hacmi (cc, örnek: 1197): "))
    guc = float(input("Güç (bhp, örnek: 82): "))
    yakit = input("Yakıt Tipi (örnek: Petrol): ")
    vites = input("Vites Tipi (örnek: Manual): ")
    sahip = input("Sahip Sayısı (örnek: First Owner): ")
    koltuk = int(input("Koltuk Sayısı (örnek: 5): "))
    yas = int(input("Araç Yaşı (örnek: 5): "))
    
    veri = {
        'Unnamed: 0': [0],  # Eğer bu index gibi kullanılıyorsa 0 verelim
        'Location': ['Mumbai'],  # Örnek bir değer koyabiliriz
        'Kilometers_Driven': [km],
        'Engine': [motor],
        'Power': [guc],
        'Mileage': [20],  
        'Fuel_Type': [yakit],
        'Transmission': [vites],
        'Owner_Type': [sahip],
        'Seats': [koltuk],
        'Age': [yas]
    }
    
    return pd.DataFrame(veri)

df_yeni = veri_al()
tahmin = model.predict(df_yeni)
print(f"\n💰 Tahmini Araç Fiyatı: {tahmin[0]:.2f} Lakh INR")