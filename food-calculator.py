class FoodCalculator:
    def __init__(self):
        self.food_calories = {
            "apple": 52,
            "banana": 89,
            "orange": 47,
            "grapes": 67,
            "cheese": 402,
            "bread": 79,
            # İhtiyaç duyulan diğer yiyecekleri buraya ekleyebilirsiniz
        }

    def calculate_calories(self, food):
        food = food.lower()
        if food in self.food_calories:
            return self.food_calories[food]
        else:
            return "Yiyecek bulunamadı!"

if __name__ == "__main__":
    calculator = FoodCalculator()
    user_input = input("Lütfen yiyeceğin adını girin: ")
    calories = calculator.calculate_calories(user_input)
    print(f"{user_input.capitalize()} {calories} kalori içerir.")
