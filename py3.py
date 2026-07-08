principal=int(input("Enter loan amount(principal :)"))
annual_rate_percent=int(input("enter annual interest rate(in%% : )"))
year=int(input("enter loan tenure(in years): "))

monthly_rate=annual_rate_percent/(12*100)
months=year*12
emi=principal*monthly_rate*pow(1+monthly_rate,months)/(pow(1+monthly_rate,months))
total_payment=emi*months;
total_interest=total_payment-principal;

print("\nMonthly EMI:RS",emi)
print("\Total Interest:RS",total_interest)
print("\nTotal payment(principal+Interest):RS",total_payment)