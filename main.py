def get_discounted_price(q, base_price):
    """Функція для визначення ціни з урахуванням обсягу закупівлі."""
    if q < 50:
        return base_price  # 0% знижки
    elif q < 100:
        return base_price * 0.95  # 5% знижки
    elif q < 150:
        return base_price * 0.90  # 10% знижки
    elif q < 200:
        return base_price * 0.85  # 15% знижки
    else:
        return base_price * 0.80  # 20% знижки


def main():
    # Вхідні параметри
    p_base = 20000  # Базова ціна закупівлі (грн)
    p_sell = 28000  # Ціна реалізації (грн)
    demand = 180  # Прогнозований попит (шт)
    budget = 3500000  # Бюджет (грн)
    s_max = 200  # Місткість складу (шт)
    h_cost = 500  # Витрати на зберігання 1 од. (грн)

    best_q = 0
    max_profit = float('-inf')
    best_stats = {}

    print(
        f"{'Обсяг (Q)':<12} | {'Ціна закуп.':<12} | {'Витрати':<12} | {'Продано':<8} | {'Залишок':<8} | {'Прибуток (грн)':<15}")
    print("-" * 80)

    # Аналізуємо кожен можливий обсяг закупівлі з кроком 10 для наочності таблиці
    # (в реальному алгоритмі крок 1, тут 10 виведено для компактного звіту)
    for q in range(0, s_max + 1, 10):
        # Якщо хочете перевірити кожну одиницю, змініть крок: range(0, s_max + 1)
        if q == 0:
            continue

        c_q = get_discounted_price(q, p_base)
        total_cost = q * c_q

        # Перевірка обмеження бюджету
        if total_cost > budget:
            print(f"{q:<12} | {c_q:<12} | {total_cost:<12} | {'-':<8} | {'-':<8} | {'Перевищено бюджет':<15}")
            continue

        sold = min(q, demand)
        leftover = max(0, q - demand)

        revenue = sold * p_sell
        holding_costs = leftover * h_cost
        profit = revenue - total_cost - holding_costs

        print(f"{q:<12} | {c_q:<12} | {total_cost:<12.0f} | {sold:<8} | {leftover:<8} | {profit:<15.0f}")

        # Пошук оптимуму (шукаємо серед усіх Q, навіть тих, що не в таблиці)

    # Точний пошук з кроком 1
    for q in range(1, s_max + 1):
        c_q = get_discounted_price(q, p_base)
        total_cost = q * c_q
        if total_cost > budget:
            continue

        sold = min(q, demand)
        leftover = max(0, q - demand)
        profit = sold * p_sell - total_cost - leftover * h_cost

        if profit > max_profit:
            max_profit = profit
            best_q = q
            best_stats = {
                'Ціна': c_q, 'Витрати': total_cost, 'Продано': sold, 'Залишок': leftover
            }

    print("-" * 80)
    print("\nОПТИМАЛЬНЕ РІШЕННЯ:")
    print(f"Оптимальний обсяг закупівлі (Q*): {best_q} шт.")
    print(f"Закупівельна ціна зі знижкою: {best_stats['Ціна']} грн")
    print(f"Загальні витрати на закупівлю: {best_stats['Витрати']} грн")
    print(f"Прогнозований продаж: {best_stats['Продано']} шт.")
    print(f"Залишок на складі: {best_stats['Залишок']} шт.")
    print(f"Максимальний прибуток: {max_profit} грн")


if __name__ == "__main__":
    main()