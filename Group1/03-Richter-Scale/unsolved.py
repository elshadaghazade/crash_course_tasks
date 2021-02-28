# The energy in joules released for a particular Richter scale measurement is given by:
# Energy = 10 ^ (1.5 x richter + 4.8)
# ------------------------------------------
# One ton of exploded TNT yields 4.184x10^9
#  joules. Thus, you can relate the energy released in
# joules to tons of exploded TNT. 

richter_scale_value = input("Please enter a Richter scale value:")
richter = float(richter_scale_value)
tnt_joules = 4.184 * (10 ** 9)

richter_joules = ?
tnt = ?


print("Richter scale value:", richter)
print("Equivalence in joules:", richter_joules)
print("Equivalence in tons of TNT:", tnt)