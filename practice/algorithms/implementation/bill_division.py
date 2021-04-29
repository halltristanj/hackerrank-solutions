def bon_appetit(bill, k, b):
    """
    bill: array
    k: no eat
    b: amount charged
    """
    bill.pop(k)
    adjusted_charge = sum(bill) // 2
    if b == adjusted_charge:
        print("Bon Appetit")
    else:
        print(b - adjusted_charge)
