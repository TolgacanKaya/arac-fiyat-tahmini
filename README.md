# 🚗 Araba Fiyat Tahmini

Bu projede, geçmiş araba satış verilerine dayanarak bir arabanın fiyatını tahmin eden bir makine öğrenmesi modeli geliştirilmiştir.

## 🔍 Proje Amacı

Kullanıcının girdiği araba bilgilerine göre (model yılı, kilometre, yakıt tipi, vites tipi, motor gücü vb.) fiyat tahmini yapılması hedeflenmiştir.

## 🧰 Kullanılan Teknolojiler

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- scikit-learn
- Jupyter Notebook

## 🗃️ Veri Seti

Veri dosyası: `car_price.csv`

| Sütun Adı           | Açıklama                                         |
| ------------------- | ------------------------------------------------ |
| `Name`              | Aracın marka ve modeli                           |
| `Location`          | Satışın yapıldığı şehir                          |
| `Year`              | Aracın üretim yılı                               |
| `Kilometers_Driven` | Aracın bugüne kadar yaptığı toplam kilometre     |
| `Fuel_Type`         | Yakıt tipi (Benzin, Dizel, LPG, Elektrik)        |
| `Transmission`      | Vites tipi (Manuel/Otomatik)                     |
| `Owner_Type`        | Sahibinin kaçıncı el olduğu (İlk el, 2. el vb.)  |
| `Mileage`           | 1 litre yakıtla kaç km gittiği (km/l veya km/kg) |
| `Engine`            | Motor hacmi (cc)                                 |
| `Power`             | Motor gücü (beygir gücü)                         |
| `Seats`             | Koltuk sayısı                                    |
| `New_Price`         | Aracın sıfır fiyatı (opsiyonel olabilir)         |
| `Price`             | Aracın satış fiyatı (etiket – hedef değişken)    |

## Dosya Yapısı

├── araba_fiyat_tahmini.ipynb # Jupyter Notebook dosyası

├── car_price.csv # Veri seti

├── model.pkl # Eğitilmiş model dosyası (isteğe bağlı)

├── fiyat_tahmin.py # Model dosyasını kullanarak girilen verilere göre fiyat tahmini(Regresyon Modeli kaydedilmiştir.)

├── README.md # Proje açıklamaları

## 📊 Modeller

Aşağıdaki algoritmalar kullanılmış ve karşılaştırılmıştır:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## 📌 Proje Adımları
Veri Ön İşleme:

- Eksik veriler temizlendi.

- Kategorik veriler sayısal değerlere dönüştürüldü.

- Gerekirse outlier (aykırı değer) temizliği yapıldı.

Veri Görselleştirme:

- Hedef değişken olan Price ile diğer sütunlar arasındaki ilişkiler incelendi.

Modelleme:

- Basit doğrusal regresyon

- Karar ağaçları ve Random Forest modelleri

- Model karşılaştırması yapıldı.

- Model Kaydetme ve Kullanma:

- Eğitilen model .pkl dosyası olarak kaydedildi.

- Yeni kullanıcı girdilerine göre fiyat tahmini yapıldı.

Model Kaydetme ve Kullanma
- En iyi model .pkl dosyasına kaydedildi.

- Kullanıcıdan alınan verilerle fiyat tahmini yapılabilir hale getirildi.

## 🧪 Sonuçlar

En yüksek başarıyı Random Forest modeli vermiştir. Tahmin başarısı metriklerle değerlendirilmiştir (RMSE, R² vb.).

## 🚀 Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri yükleyin:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
