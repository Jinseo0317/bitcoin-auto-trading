import pyupbit

f = open("upbit_api.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
balance = upbit.get_balance("KRW")
print(balance)
