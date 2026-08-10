registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()

# Check whether the student can access the online exam
if registered == "No":
    print("Access Denied: Registration Incomplete.")
elif fee_paid == "No" or identity_verified == "No":
    print("Access Denied: Verification Pending.")
elif system_check == "No":
    print("Access Denied: System Check Failed.")
else:
    print("Access Granted.")
