def main():
    sales = get_sales()
    while sales >= 0:
        if sales < 1000:
            sales_bonus = sales * 0.10
        else:
            sales_bonus = sales * 0.15
        print("$", sales_bonus)
        sales = get_sales()


def get_sales():
    sales = float(input("Enter sales: $"))
    return sales


main()
