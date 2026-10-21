import hashlib
file_name = input("enter file name : ")
with open(file_name , "rb")as file:
  data = file.read()

hash_value = hashlib.sha256(data).hexdigest()
print("SHA_256 : " , hash_value)

original_hash + input("enter original hash : ")
