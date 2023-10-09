import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = get_play(perf, plays)
        amount_per_performance = calculate_amount(perf, plays)

        volume_credits = calculate_volume_credits(perf, play, volume_credits)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(amount_per_performance / 100)} ({perf["audience"]} seats)\n'

    for perf in invoice['performances']:
        amount_per_performance = calculate_amount(perf, plays)
        total_amount += amount_per_performance

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


def get_play(perf, plays):
    return plays[perf['playID']]


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


def calculate_volume_credits(perf, play, volume_credits):
    # add volume credits
    volume_credits += max(perf['audience'] - 30, 0)
    # add extra credit for every ten comedy attendees
    if "comedy" == play["type"]:
        volume_credits += math.floor(perf['audience'] / 5)
    return volume_credits


def statement_html(invoice, plays):
    return "abc"
