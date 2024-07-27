import pulp

# Створення задачі лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішень
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція - максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Вивід результатів
print(f"Статус розв'язку: {pulp.LpStatus[model.status]}")
print(f"Кількість виробленого лимонаду: {lemonade.varValue} одиниць")
print(f"Кількість виробленого фруктового соку: {fruit_juice.varValue} одиниць")
