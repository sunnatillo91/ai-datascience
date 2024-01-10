# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 20:46:28 2024

@author: Sunnatillo
"""

# AMALIYOT
# 1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini
#  qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def toliq_ism_info(ism, familiya, tyil, tjoy, manzil, email, tel=''):
    """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon 
    raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
    if tel:
        toliq_ism = f"{ism.title()} {familiya.title()} {tyil}-yilda {tjoy.title()}da tug'ilgan \
            yoshi {2024-tyil} da. Email: {email}, manzili {manzil.title()}, telefon raqami {tel}"
    else:
        toliq_ism = f"{ism.title()} {familiya.title()} {tyil}-yilda {tjoy.title()}da tug'ilgan \
            yoshi {2024-tyil} da. Email: {email}, manzili {manzil.title()}, telefon raqami noma'lum"
    return toliq_ism
talaba = toliq_ism_info('orif', 'shamsiyev', 1986, "nurota", 'navoiy', "orif@gmail.com", 939507999)
print(talaba)
# 2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni 
# shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


# 3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# 4. Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va 
# yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

# 5. Berilgan oraliqdagi [tub sonlar](https://uz.wikipedia.org/wiki/Tub_sonlar_ro%CA%BByxati) ro'yxatini 
# qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
# musbat sonlar)
# 6. Foydalanuvchidan son qabul qilib, shu son miqdoricha [Fibonachchi ketma-ketligidagi]
# (https://medium.com/@qudratxoja.musayev/fibonachchi-sonlari-va-u-haqida-qiziqarli-faktlar-47000a80264d) sonlar ro'yxatni qaytaruvchi funksiya yozing.  **Ta’rif**: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  `1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...`

# JAVOBLAR
