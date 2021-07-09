print('How many kilometers did you run');
km = input();
miles = float(km)/1.60934;
rounded_miles = round(miles, 2);
print('Your {} km, is {} miles'.format(km, rounded_miles));