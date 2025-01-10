class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Пустой словарь для товаров и их цен

    def add(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def delete(self, item_name):
        """Удаляет товар из ассортимента по названию."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Получает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def set_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __repr__(self):
        """Возвращает строковое представление магазина и его ассортимента."""
        return f"Магазин '{self.name}' по адресу '{self.address}' имеет следующие товары: {self.items}"