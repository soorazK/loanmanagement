import pandas as pd
from math import ceil

class LoanCalculator:
    def __init__(self, loan_amount, interest_rate, loan_period_yrs, num_payments_per_year, start_date):
        self.loan_amount = round(float(loan_amount), 2)
        self.interest_rate = round(float(int(interest_rate)), 2)
        self.loan_period_yrs = round(float(loan_period_yrs), 2)
        self.num_payments_per_year = round(float(num_payments_per_year), 2)
        self.start_date = start_date
        self.number_of_payments = ceil(self.loan_period_yrs * self.num_payments_per_year)
        self.monthly_interest_rate = self.interest_rate / 100 / 12
        self.payment_per_period = 0 if self.number_of_payments == 0 else self.calculate_pmt()

    def calculate_pmt(self):
        pmt = self.loan_amount * self.monthly_interest_rate / (1 - (1 + self.monthly_interest_rate) ** (-self.number_of_payments))

        return round(pmt, 2)

    def generate_table(self):
        df = pd.DataFrame(columns=[
            "payment_no",
            "payment_date",
            "payment",
            "principal",
            "interest",
            "extra_payments",
            "balance"
        ])

        for i in range(1, self.number_of_payments +1):
            if i == 1:
                interest = round(self.loan_amount * self.monthly_interest_rate, 2)
                new_row = {'payment_no': i, 'payment_date': "some_date", 'payment': self.payment_per_period,
                           'principal': self.payment_per_period - interest, 'interest': interest,
                           'extra_payments': interest,
                           'balance': self.loan_amount - self.payment_per_period
                           }

                df = df.append(new_row, ignore_index=True)
            else:

                prev_balance = df.loc[i-2]['balance']
                if i >= self.number_of_payments or prev_balance <= 0:
                    break

                prev_extra_payments = df.loc[i-2]['extra_payments']
                interest = prev_balance * self.monthly_interest_rate
                payment = self.payment_per_period if self.monthly_interest_rate + interest < prev_balance else prev_balance + interest
                principal = payment - interest
                extra_payments = prev_extra_payments + interest
                new_balance = prev_balance - principal - extra_payments
                new_row = {
                    'payment_no': i, 'payment_date': "some_date", 'payment': payment,
                    'principal': principal, 'interest': interest, 'extra_payments': extra_payments,
                    'balance': new_balance
                }

                df = df.append(new_row, ignore_index=True)

        return df.to_json(orient='records')

# obj= LoanCalculator(4356000, 2, 20.3, 12, 'x')
# obj.generate_table()
