#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it


PROVINCIAL_TAX = .05
FEDERAL_TAX = .025


def bill_of_sale(purchase, provincial_sales_tax, federal_sales_tax, total_sales_tax, total_price):
    with open("sales_receipt.txt", "w") as output_file:
        output_file.write("Amount of purchase: {0:.2f}".format(purchase))
        output_file.write("\nProvincial tax: {0:.2f}".format(provincial_sales_tax))
        output_file.write("\nFederal tax: {0:.2f}".format(federal_sales_tax))
        output_file.write("\nTotal tax: {0:.2f}".format(total_sales_tax))
        output_file.write("\nTotal sale: {0:.2f}".format(total_price))


def calculate_bill(purchase):
    provincial_sales_tax = purchase * PROVINCIAL_TAX
    federal_sales_tax = purchase * FEDERAL_TAX
    total_sales_tax = provincial_sales_tax + federal_sales_tax
    total_price = purchase + total_sales_tax
    bill_of_sale(purchase, provincial_sales_tax, federal_sales_tax, total_sales_tax, total_price)


calculate_bill(17.89)
