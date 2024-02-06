# Class4-Statistics-Week15
## Seaborn kütüphanesi içerisinde bulunan titanic datasını kullanarak,
```
# pip install seaborn
# seaborn kutuphanesini ustteki kod ile yukluyoruz
import seaborn as sns
titanic= sns.load_dataset('titanic')
df = titanic.copy()
print(df.head())
#kodlar araciligi ile titanic datasini yukluyoruz
```

### Değişkenlerin veri türlerini yazınız
- Nicel verileri describe methodu ile inceleyiniz ve verileri ortalaması, standart sapması ve çeyrekliklerine bakarak aykırılık olup olmadığını ve normal dağılıp dağılmadığı konusunda yorumda bulunun.
- Nitel verilerin dtypelarıını kategorik yapın. Sıralanabilecek kategorik değişkenlerin sıralı olarak belirleyiniz. Sıralanmış kategorik verilerin sıralaması doğru değilse sıralamayı uygun hale getirin.
- sex ve class değişkenlerini Label Encoder  veya Dummies yöntemiyle sayısal verierle dönüştürünüz.
- age ve fare değişkenlerinin normalliklerini inceleyiniz

## Hipotez Testleri:
```
H0 hipotezi Titanik kazasında insanlarin sosyo ekonomik siniflari hayatta kalma oranlarına herhangi bir etkisi yoktur
H1 hipotezi Titanik kazasında insanlarin sosyo ekonomik siniflari hayatta kalma oranlarına herhangi bir etkisi vardır.
```
Hipotez test asamalarinin tamamini yukarda önerilen hipotez icin uygulayınız ve sonucu yorumlayiniz.
