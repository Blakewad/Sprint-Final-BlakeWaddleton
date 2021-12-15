# QAP 5 Project Data Files and Reports
# Author: Blake Waddleton
# Date: December 15, 2021

allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
digit_set = set("1234567890")
import datetime

# Data File Called OSICD
f = open("OSICD.dat", "r")
PolNum = int(f.readline())
BasicPremium = float(f.readline())
CarDis = float(f.readline())
ExtLiaCov = float(f.readline())
GlassCov = float(f.readline())
LoanCarCov = float(f.readline())  # PER CAR
HST_RATE = float(f.readline())  # MULTIPLY BY SUB TOTAL FOR TAXES
ProcFee = float(f.readline())  # ADD TO POLICY TOTAL ALL DIVIDED BY 12 FOR MONTHLY PAYMENT

f.close()

# Validations and inputs
while True:
    while True:
        Cus_fName = input("Enter Customer's First Name: ")
        if Cus_fName == "":
            print("Must Enter First Name")
        elif not set(Cus_fName).issubset(allowed_char):
            print("Invalid Entry, Please Use A-Z,- or '")
        else:
            break

    while True:
        Cus_lName = input("Enter Customer's Last Name: ")
        if Cus_lName == "":
            print("Must Enter Last Name")
        elif not set(Cus_lName).issubset(allowed_char):
            print("Invalid Entry, Please Use A-Z,- or '")
        else:
            break

    while True:
        StreetAddress = input("Enter Street Address: ")
        if StreetAddress == "":
            print("Please Enter a Street Address")
        else:
            break

    while True:
        City = input("City: ")
        if City == "":
            print("Customer Name is Cannot be Blank. Please Re-enter")
        else:
            break

    while True:
        Province = input("Enter Province Code (XX): ").upper()
        if len(Province) != 2:
            print("Must use 2 character code")
        elif Province != "AB" and Province != "BC" and Province != "MB" and Province != "NB" and Province != "NL" \
                and Province != "NT" and Province != "NS" and Province != "NU" and Province != "ON" and Province != "PE" \
                and Province != "QC" and Province != "SK" and Province != "YT":
            print("Please use Valid Code")
        else:
            break

    while True:
        pos_code_alpha_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        digit_set = set("1234567890")
        PostalCode = input("Enter Postal Code (A1A1A1): ")
        if PostalCode == "":
            print("Please Enter Postal Code")
        elif len(PostalCode) != 6:
            print("Postal Code Must be 6 Characters")
        elif set(PostalCode[0]).issubset(pos_code_alpha_set) == False or set(PostalCode[1]).issubset(
                digit_set) == False or set(
                PostalCode[2]).issubset(pos_code_alpha_set) == False or set(PostalCode[3]).issubset(
            digit_set) == False or set(
            PostalCode[4]).issubset(pos_code_alpha_set) == False or set(PostalCode[5]).issubset(digit_set) == False:
            print("Must be in specified format")
        else:
            break

    while True:
        digit_set = set("1234567890")
        Phone_num = input("Enter Phone Number (1234567890): ")
        if len(Phone_num) != 10:
            print("Please Enter 10 Digit Phone Number")
        elif set(Phone_num).issubset(digit_set) is False:
            print("Please Use Digits 0-9 Only")
        else:
            break

    while True:
        PolicyDate = input("Enter the Policy Date (YYYY-MM-DD): ")
        try:
            PolicyDate = datetime.datetime.strptime(PolicyDate, "%Y-%m-%d")
        except:
            print("Please use specified format")
        else:
            if PolicyDate > datetime.datetime.now():
                print("Policy Date can not Exceed Current Date")
            else:
                break

    # Dates and Time
    first_pay_due_date = PolicyDate + datetime.timedelta(days=30)
    first_pay_due_date_dis = datetime.datetime.strftime(first_pay_due_date, "%d-%b-%y")
    full_pay_due_date = PolicyDate + datetime.timedelta(days=30)
    full_pay_due_date_dis = datetime.datetime.strftime(full_pay_due_date, "%d-%b-%y")

    # Calculations and Workings
    InsPrem = BasicPremium
    NumCarsIns = int(input("Please enter number of cars being insured: "))
    if NumCarsIns > 1:
        InsPrem += (BasicPremium - (CarDis * BasicPremium)) * (NumCarsIns - 1)

    ExtraLiabilityCost = 0
    ExtraLiability = input("Would you like Extra Liability up to $1,000,000 (Y or N): ")
    if ExtraLiability.upper() == "Y":
        ExtraLiabilityCost += ExtLiaCov

    GlassCoverageCost = 0
    GlassCoverage = input("Would you like optional glass coverage (Y or N): ")
    if GlassCoverage.upper() == "Y":
        GlassCoverageCost += GlassCov

    LoanerCarCost = 0
    LoanerCar = input("Would you like a loaner car (Y or N): ")
    if LoanerCar.upper() == "Y":
        LoanerCarCost += LoanCarCov

    InsPremium = BasicPremium

    TotalExtraCost = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost + NumCarsIns
    TotalInsPremium = InsPremium + TotalExtraCost
    HST = TotalInsPremium * HST_RATE
    TotalCost = TotalInsPremium + HST
    MonthlyPayment = (TotalCost + ProcFee) / 12

    PaymentTypeCost = 0
    PaymentType = input("Would you like to pay in full or monthly (F or M): ") # Payment Displayed by Total Cost or Monthly Payment
    if PaymentType.upper() == 'F':
        PaymentTypeCost = TotalCost
    else:
        PaymentTypeCost = MonthlyPayment


    # Receipt for One Stop Insurance Company
    print()
    print("      One Stop Insurance Company")
    print("     ============================    ")
    print()
    print("Client Name and Address:")
    print('Sold To: ')
    print(' ' * 4, Cus_fName, Cus_lName)
    print(' ' * 4, StreetAddress)
    print(' ' * 4, City, Province, PostalCode)
    print()
    print("Phone Number:", Phone_num)
    print()
    print()
    print("Number of Cars Insured:          {}".format(NumCarsIns))
    print()
    print("Extra Liability (Y or N):        {}".format(ExtraLiability))
    print("Extra Liability Cost:            ${:,.2f}".format(ExtraLiabilityCost))
    print()
    print("Glass Coverage (Y or N):         {}".format(GlassCoverage))
    print("Glass Coverage Cost:             ${:,.2f}".format(GlassCoverageCost))
    print()
    print("Loaner Car (Y or N):             {}".format(LoanerCar))
    print("Loaner Car Cost:                 ${:,.2f}".format(LoanerCarCost))
    print()
    print("Payment Type (F or M):           {}".format(PaymentType))
    print("Basic Insurance Premium:         ${:,.2f}".format(InsPremium))
    print("Total Extra Costs:               ${:,.2f}".format(TotalExtraCost))
    print("Total Insurance Premium:         ${:,.2f}".format(TotalInsPremium))
    print("Hst Rate:                        ${:,.2f}".format(HST))
    print("Total Cost:                      ${:,.2f}".format(TotalCost))

    print("Full or Monthly Payment:         ${:,.2f}".format(PaymentTypeCost))
    print()
    print("--------------------------------------")
    print()
    print("Issued: {}".format(PolicyDate))
    print()

    PolNum += 1

    f = open('OSICD.dat', "w")
    f.write("{}\n".format(str(PolNum)))
    f.write("{}\n".format(str(BasicPremium)))
    f.write("{}\n".format(str(CarDis)))
    f.write("{}\n".format(str(ExtLiaCov)))
    f.write("{}\n".format(str(GlassCov)))
    f.write("{}\n".format(str(LoanCarCov)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(ProcFee)))
    f.close()

    f = open('Policies.dat', "a")
    f.write("{},".format(str(PolNum)))
    f.write("{},".format(str(PolicyDate)))
    f.write("{},".format(str(Cus_fName + Cus_lName)))
    f.write("{},".format(str(StreetAddress)))
    f.write("{},".format(str(City)))
    f.write("{},".format(str(Province)))
    f.write("{},".format(str(PostalCode)))
    f.write("{},".format(str(Phone_num)))
    f.write("{},".format(str(NumCarsIns)))
    f.write("{},".format(str(ExtraLiability)))
    f.write("{},".format(str(GlassCoverage)))
    f.write("{},".format(str(LoanerCar)))
    f.write("{},".format(str(PaymentType)))
    f.write("{},".format(str(InsPremium)))
    f.write("{},".format(str(TotalExtraCost)))
    f.write("{},".format(str(TotalInsPremium)))
    f.write("{},".format(str(HST_RATE)))
    f.write("{},".format(str(TotalCost)))
    f.write("{}\n".format(str(MonthlyPayment)))
    print("Policy processed and saved.")
    f.close()

    while True:
        Continue = input("Do you want to make another Entry?  (Y) or (N) ").upper()
        if Continue == "Y":
            print()
            break
        elif Continue == "N":
            print()
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")
    if Continue == "N":
        print()
        break

#  First Report, Detailed report
print('1234567890123456789012345678901234567890123456789012345678901234567890')
print()
print('ONE STOP INSURANCE COMPANY')
print('POLICY LISTING AS OF {}'.format(first_pay_due_date))
print()
print('POLICY CUSTOMER                      INSURANCE     EXTRA     TOTAL')
print('NUMBER NAME                           PREMIUM      COSTS     PREMIUM')
print('======================================================================')

CusCount = 0

# Data File Called Policies
f = open("Policies.dat", "r")

for PoliciesDataLine in f:
    PoliciesLine = PoliciesDataLine.split(",")

    PolNum = int(PoliciesLine[0].strip())
    PolicyDate = PoliciesLine[1].strip()
    CusName = PoliciesLine[2].strip()
    StreetAddress = PoliciesLine[3].strip()
    City = PoliciesLine[4].strip()
    Province = PoliciesLine[5].strip()
    PostalCode = PoliciesLine[6].strip()
    Phone_num = PoliciesLine[7].strip()
    NumCarsIns = PoliciesLine[8].strip()
    ExtraLiability = PoliciesLine[9].strip()
    GlassCoverage = PoliciesLine[10].strip()
    LoanerCar = PoliciesLine[11].strip()
    PaymentType = PoliciesLine[12].strip()
    InsPremium = float(PoliciesLine[13].strip())
    TotalExtraCost = float(PoliciesLine[14].strip())
    TotalInsPremium = float(PoliciesLine[15].strip())
    HST_RATE = float(PoliciesLine[16].strip())
    TotalCost = float(PoliciesLine[17].strip())
    MonthlyPayment = float(PoliciesLine[18].strip())

    CusCount += 1
    PolNum += 1
    TotalPolicies = NumCarsIns

    print('{}   {} {}                ${:,.2f}      ${:,.2f}   ${:,.2f}'.format(PolNum, Cus_fName, Cus_lName,
                                                                                           InsPremium, TotalExtraCost,
                                                                                           TotalInsPremium))

print('======================================================================')
print('Total policies: {}'.format(TotalPolicies))
print()
print()
print()

f.close()

# Second Report, Exception Report
print('ONE STOP INSURANCE COMPANY')
print('MONTHLY PAYMENT LISTING AS OF {}'.format(first_pay_due_date))
print()
print('POLICY    CUSTOMER          TOTAL               TOTAL     MONTHLY')
print('NUMBER    NAME              PREMIUM    HST      COST      PAYMENT')
print('=====================================================================')

CusCount = 0
f = open("Policies.dat", "r")

for PoliciesDataLine in f:
    PoliciesLine = PoliciesDataLine.split(",")

    PolNum = int(PoliciesLine[0].strip())
    PolicyDate = PoliciesLine[1].strip()
    CusName = PoliciesLine[2].strip()
    StreetAddress = PoliciesLine[3].strip()
    City = PoliciesLine[4].strip()
    Province = PoliciesLine[5].strip()
    PostalCode = PoliciesLine[6].strip()
    Phone_num = PoliciesLine[7].strip()
    NumCarsIns = PoliciesLine[8].strip()
    ExtraLiability = PoliciesLine[9].strip()
    GlassCoverage = PoliciesLine[10].strip()
    LoanerCar = PoliciesLine[11].strip()
    PaymentType = PoliciesLine[12].strip()
    InsPremium = float(PoliciesLine[13].strip())
    TotalExtraCost = float(PoliciesLine[14].strip())
    TotalInsPremium = float(PoliciesLine[15].strip())
    HST_RATE = float(PoliciesLine[16].strip())
    TotalCost = float(PoliciesLine[17].strip())
    MonthlyPayment = float(PoliciesLine[18].strip())
    CusCount += 1
    PolNum += 1
    TotalPolicies = NumCarsIns
    print('{}   {} {}      ${:,.2f}  ${:,.2f} ${:,.2f}  ${:,.2f} '.format(PolNum, Cus_fName, Cus_lName,
                                                                                   TotalInsPremium, HST_RATE, TotalCost,
                                                                                   MonthlyPayment))
print('=====================================================================')
print('Total policies: {}'.format(TotalPolicies))
f.close()
