import math


class Calculator:

    @staticmethod
    def calculate_volume_credits(perf, play):
        volume_credits = max(perf['audience'] - 30, 0)
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        return volume_credits

    @staticmethod
    def calculate_amount(perf, plays):
        play = get_play(perf, plays)
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')
        return this_amount

    def get_customer_invoice(invoice):
        return invoice["customer"]

    def get_total_amount(invoice, plays):
        total_amount = 0
        for perf in invoice['performances']:
            amount_per_performance = Calculator.calculate_amount(perf, plays)
            total_amount += amount_per_performance
        return total_amount

    def get_volume_credits(invoice, plays):
        volume_credits = 0
        for perf in invoice['performances']:
            play = get_play(perf, plays)
            volume_credits += Calculator.calculate_volume_credits(perf, play)
        return volume_credits


class PerfData():
    def __init__(self, name):
        self.name = name


def statement(invoice, plays):
    total_amount = 0
    result = f'Statement for {Calculator.get_customer_invoice(invoice)}\n'

    for perf in invoice['performances']:
        amount_per_performance = Calculator.calculate_amount(perf, plays)
        result += f' {get_play(perf, plays)["name"]}: {format_as_dollars(amount_per_performance)} ({perf["audience"]} seats)\n'

    total_amount = Calculator.get_total_amount(invoice, plays)

    result += f'Amount owed is {format_as_dollars(total_amount)}\n'
    result += f'You earned {Calculator.get_volume_credits(invoice, plays)} credits\n'
    return result




def statement_html(invoice, plays):
    return "abc"

def get_play(perf, plays):
    return plays[perf['playID']]

def format_as_dollars(amount):
    return f"${(amount / 100):0,.2f}"