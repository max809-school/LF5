def get_float_input(prompt_text):
    """Fordert den Benutzer kontinuierlich zur Eingabe auf, bis eine gültige Gleitkommazahl eingegeben wird."""
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def perform_trade_calculation():
    """
    Sammelt Eingaben und berechnet den Bruttoverkaufspreis basierend auf dem
    Handelskalkulationsschema.
    """
    print("--- Bitte geben Sie die Eingabewerte an ---")

    # --- Eingaben ---
    gross_quantity = get_float_input("Bruttomenge: ")
    quantity_deductions = get_float_input("Mengenabzüge: ")
    price_per_unit = get_float_input("* Preis je Einheit: ")
    supplier_discount_percent = get_float_input("- Liefererrabatt (v. H. in %): ")
    supplier_cash_discount_percent = get_float_input("- Liefererskonto (v. H. in %): ")
    acquisition_costs = get_float_input("+ Bezugskosten: ")
    overhead_surcharge_percent = get_float_input(
        "+ Handlungskostenzuschlagssatz (v. H. in %): "
    )
    profit_margin_percent = get_float_input("+ Gewinnzuschlag (v. H. in %): ")
    customer_cash_discount_percent = get_float_input("+ Kundenskonto (i. H. in %): ")
    customer_discount_percent = get_float_input("+ Kunderabatt (i. H. in %): ")
    vat_percent = get_float_input("+ Mehrwertsteuer (MWST-Satz in %): ")

    print("\n--- Berechnungsergebnisse ---")

    # Schritt 1: Nettomenge und Einkaufspreis berechnen
    net_quantity = gross_quantity - quantity_deductions
    purchase_price = net_quantity * price_per_unit
    print(f"{'Bruttomenge':<35} {gross_quantity:>12.2f}")
    print(f"{'- Mengenabzüge':<35} {quantity_deductions:>12.2f}")
    print(f"{'= Nettomenge':<35} {net_quantity:>12.2f}")
    print(f"{'* Preis je Einheit':<35} {price_per_unit:>12.2f}")
    print(f"{'= Einkaufspreis':<35} {purchase_price:>12.2f}")

    # Schritt 2: Liefererrabatt anwenden (von Hundert)
    supplier_discount_value = purchase_price * (supplier_discount_percent / 100)
    target_purchase_price = purchase_price - supplier_discount_value
    print(
        f"- Liefererrabatt ({supplier_discount_percent:.2f}%) {'':<20} {supplier_discount_value:>12.2f}"
    )
    print(f"{'= Zieleinkaufspreis':<35} {target_purchase_price:>12.2f}")

    # Schritt 3: Liefererskonto anwenden (von Hundert)
    supplier_cash_discount_value = target_purchase_price * (
        supplier_cash_discount_percent / 100
    )
    cash_purchase_price = target_purchase_price - supplier_cash_discount_value
    print(
        f"- Liefererskonto ({supplier_cash_discount_percent:.2f}%) {'':<20} {supplier_cash_discount_value:>12.2f}"
    )
    print(f"{'= Bareinkaufspreis':<35} {cash_purchase_price:>12.2f}")

    # Schritt 4: Bezugskosten hinzufügen
    cost_price = cash_purchase_price + acquisition_costs
    print(f"{'+ Bezugskosten':<35} {acquisition_costs:>12.2f}")
    print(f"{'= Einstandspreis (Bezugspreis)':<35} {cost_price:>12.2f}")

    # Schritt 5: Handlungskostenzuschlag hinzufügen (von Hundert)
    overhead_surcharge_value = cost_price * (overhead_surcharge_percent / 100)
    prime_cost = cost_price + overhead_surcharge_value
    print(
        f"+ Handlungskosten ({overhead_surcharge_percent:.2f}%) {'':<18} {overhead_surcharge_value:>12.2f}"
    )
    print(f"{'= Selbstkosten':<35} {prime_cost:>12.2f}")

    # Schritt 6: Gewinnzuschlag hinzufügen (von Hundert)
    profit_margin_value = prime_cost * (profit_margin_percent / 100)
    cash_selling_price = prime_cost + profit_margin_value
    print(
        f"+ Gewinnzuschlag ({profit_margin_percent:.2f}%) {'':<19} {profit_margin_value:>12.2f}"
    )
    print(f"{'= Barverkaufspreis':<35} {cash_selling_price:>12.2f}")

    # Schritt 7: Zielverkaufspreis berechnen (in Hundert)
    # Barverkaufspreis = Zielverkaufspreis * (1 - Kundenskonto)
    target_selling_price = cash_selling_price / (
        1 - (customer_cash_discount_percent / 100)
    )
    customer_cash_discount_value = target_selling_price - cash_selling_price
    print(
        f"+ Kundenskonto ({customer_cash_discount_percent:.2f}%) {'':<21} {customer_cash_discount_value:>12.2f}"
    )
    print(f"{'= Zielverkaufspreis':<35} {target_selling_price:>12.2f}")

    # Schritt 8: Nettoverkaufspreis berechnen (in Hundert)
    # Zielverkaufspreis = Nettoverkaufspreis * (1 - Kunderabatt)
    net_selling_price = target_selling_price / (1 - (customer_discount_percent / 100))
    customer_discount_value = net_selling_price - target_selling_price
    print(
        f"+ Kunderabatt ({customer_discount_percent:.2f}%) {'':<22} {customer_discount_value:>12.2f}"
    )
    print(f"{'= Nettoverkaufspreis':<35} {net_selling_price:>12.2f}")

    # Schritt 9: Mehrwertsteuer hinzufügen
    vat_value = net_selling_price * (vat_percent / 100)
    gross_selling_price = net_selling_price + vat_value
    print(f"+ Mehrwertsteuer ({vat_percent:.2f}%) {'':<19} {vat_value:>12.2f}")
    print("-" * 48)
    print(f"{'= Bruttoverkaufspreis':<35} {gross_selling_price:>12.2f}")
    print("=" * 48)


if __name__ == "__main__":
    try:
        perform_trade_calculation()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Division durch 0 ist nicht erlaubt")
