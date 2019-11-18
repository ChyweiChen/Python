# PROGRAM BetterAverageArrayReal:

BankBal = [44.44, 423.33, 545.23, 423.3, 121.6, 32.4, 121.4, 13.8]
total = 0
for a in range(0,len(BankBal)):
# DO
    total = total + BankBal[a]
# ENDFOR;
AveValue = total/len(BankBal)
print(AveValue)
# END.

