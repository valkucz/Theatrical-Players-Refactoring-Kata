using System;
using System.Collections.Generic;
using System.Globalization;

namespace TheatricalPlayersRefactoringKata
{
    public class StatementPrinter
    {
        const int TRAGEDY_BASE_PRICE = 40000;
        private const int COMEDY_BASE_PRICE = 30000;
        public string Print(Invoice invoice, Dictionary<string, Play> plays)
        {
            var totalAmount = 0;
            var volumeCredits = 0;
            var result = string.Format("Statement for {0}\n", invoice.Customer);
            CultureInfo cultureInfo = new CultureInfo("en-US");

            foreach(var perf in invoice.Performances)
            {
                volumeCredits += ComputePrice(plays, perf, cultureInfo, ref result, ref totalAmount);
            }
            result += String.Format(cultureInfo, "Amount owed is {0:C}\n", Convert.ToDecimal(totalAmount / 100));
            result += String.Format("You earned {0} credits\n", volumeCredits);
            return result;
        }

        private static int ComputePrice(Dictionary<string, Play> plays, Performance perf, CultureInfo cultureInfo,
            ref string result, ref int totalAmount)
        {
            var volumeCredits = 0;
            var play = plays[perf.PlayID];
            var price = 0;
            switch (play.Type) 
            {
                case "tragedy":
                    if (perf.Audience > 30) {
                        price += 1000 * (perf.Audience - 30) + TRAGEDY_BASE_PRICE;
                    }
                    break;
                case "comedy":
                    if (perf.Audience > 20) {
                        price += 10000 + 500 * (perf.Audience - 20) + COMEDY_BASE_PRICE;
                    }
                    price += 300 * perf.Audience;
                    break;
                default:
                    throw new Exception("unknown type: " + play.Type);
            }
            // add volume credits
            volumeCredits = Math.Max(perf.Audience - 30, 0);
            // add extra credit for every ten comedy attendees
            if ("comedy" == play.Type) volumeCredits += (int)Math.Floor((decimal)perf.Audience / 5);

            // print line for this order
            result += String.Format(cultureInfo, "  {0}: {1:C} ({2} seats)\n", play.Name, Convert.ToDecimal(price / 100), perf.Audience);
            totalAmount += price;
            return volumeCredits;
        }
    }
}
