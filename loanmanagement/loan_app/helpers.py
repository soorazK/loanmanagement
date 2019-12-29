from django.conf import settings
from django.http import HttpResponse
from django.utils.text import slugify
from django.template.loader import get_template
from io import BytesIO
from math import ceil
from xhtml2pdf import pisa

import os
import pandas as pd
import random
import string



class LoanCalculator:
    def __init__(self, loan_amount, interest_rate, loan_period_yrs, num_payments_per_year, start_date):
        self.loan_amount = round(float(loan_amount), 2)
        self.interest_rate = round(float(interest_rate), 2)
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

        for i in range(1, self.number_of_payments + 1):
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

        return df.to_dict('records')


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


def unique_key_generator(instance):
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), dest=result, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path.replace("%20", " ")
