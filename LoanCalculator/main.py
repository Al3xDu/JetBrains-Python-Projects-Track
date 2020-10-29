import math
import sys


from utils_printer import print_hi_to_this_project


def calc_diff(principal, interest, periods):
    payment_sum = 0
    for m in range(1, int(periods) + 1):
        param = principal - ((principal * (m - 1)) / periods)
        month_payment = principal / periods + interest * param
        month_payment = math.ceil(month_payment)
        payment_sum += month_payment
        print(f"Month {m}: payment is {month_payment}")

    over_payment = payment_sum - principal
    print("\n")
    print(f"Overpayment = {math.ceil(over_payment)}")


def calc_annuity(principal, interest, periods, payment):
    annuity_type = None

    if principal == 0:
        annuity_type = True
        upper_param = interest * pow(1 + interest, periods)
        bottom_param = pow(1 + interest, periods) - 1
        principal = payment / (upper_param / bottom_param)

    if periods == 0:
        annuity_type = False
        log_value = payment / (payment - interest * principal)
        log_base = 1 + interest
        periods = math.log(log_value, log_base)

    number_of_years = int(int(periods) / 12)
    number_of_months = math.ceil(periods - int(number_of_years * 12))

    if number_of_months == 12:
        number_of_months = 0
        number_of_years += 1

    periods = math.ceil(periods)
    upper_func_param = interest * pow(1 + interest, math.ceil(periods))
    bottom_func_param = pow(1 + interest, math.ceil(periods)) - 1
    annuity = principal * upper_func_param / bottom_func_param
    if payment == 0:
        payment = math.ceil(annuity)

    over_payment = payment * periods - principal

    if number_of_years == 0:
        loan_message = f"It will take {number_of_months} months to repay this loan!"
    elif number_of_months == 0:
        loan_message = f"It will take {number_of_years} years to repay this loan!"
    else:
        loan_message = f"It will take {number_of_years} years and {number_of_months} months to repay this loan!"

    if annuity_type is True:
        print(f"Your loan principal = {int(principal)}!")
    elif annuity_type is False:
        print(loan_message)
    else:
        print(f"Your annuity payment = {payment}!")

    print(f"Overpayment = {math.ceil(over_payment)}")


def main():
    args = sys.argv
    test = []
    calc_type = None
    principal = 0
    payment = 0
    periods = 0
    interest = 0
    for arg in args:
        if "type" in arg:
            calc_type = str(arg[arg.index("=") + 1:])
            test.append(calc_type)
        if "principal" in arg:
            principal = int(arg[arg.index("=") + 1:])
            test.append(principal)
        if "payment" in arg:
            payment = int(arg[arg.index("=") + 1:])
            test.append(payment)
        if "periods" in arg:
            periods = int(arg[arg.index("=") + 1:])
            test.append(periods)
        if "interest" in arg:
            interest = float(arg[arg.index("=") + 1:])
            test.append(interest)

    # Verify args
    if calc_type is None or interest is None:
        print("Incorrect parameters")
        sys.exit()

    if len(test) < 4 or principal < 0 or periods < 0 or payment < 0 or interest < 0:
        print("Incorrect parameters")
        sys.exit()

    if calc_type is not None and calc_type != "diff" and calc_type != "annuity":
        print("Incorrect parameters")
        sys.exit()

    # Actual program calculator
    interest = (interest / 100) / ((12 * 100) / 100)
    if calc_type == "diff":
        calc_diff(principal, interest, periods)
    elif calc_type == "annuity":
        calc_annuity(principal, interest, periods, payment)


# Entrypoint
if __name__ == '__main__':
    print_hi_to_this_project()
    main()
