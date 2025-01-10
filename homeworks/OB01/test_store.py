from store import Store

stores = {
    '1':Store("5-ка", "Улица Ленина, 666"),
    '2':Store("Перекрёсток", "Улица Ленина, 1"),
    '3':Store("Магнит", "пос. Пролетарка, 123")
}
for k in stores.keys():
    st = stores[k]
    st.add("яблоки", 0.5)
    st.add("бананы", 0.75)
    st.add("шоколад", 1)
    st.add("водка", 3.62)
    print(st)

# Получаем цену товара
print("Цена яблок:", stores['1'].get_price("яблоки"))
# Обновляем цену товара с проверкой ошибок ввода
stores['1'].set_price("яблоки", 1)
stores['1'].set_price("яблоко", 2)
print("Обновленная цена яблок:", stores['1'].get_price("яблоки"))
# Удаляем и добаляем товары с
stores['2'].delete('шоколад')
stores['3'].delete('Водка')
stores['3'].delete('водка')
stores['3'].add('мороженое',0.4)
# Проверяем текущий ассортимент
for k in stores.keys():
    print(stores[k])
