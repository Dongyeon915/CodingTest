def swap02(a,b):
  a, b = b, a
  # 튜플로 리턴값이 여러개가 된다.
  return a, b
if __name__ == '__main__':
    a = 50
    b = 30

print(f"a: {a}, b: {b}")

a, b = swap02(a, b)
print(f"a: {a}, b: {b}")

# Tuple
person01 = ("동연", 3, True, False)

lists = [1, 2, 3]
person02 = ("동연", lists, 3, True, False)
print(person02[1][2])

# 튜플은 대부분든 모든 값을 저장할수있다.
a, b, c = (10, 30, [1, 2, 3])
print(f"{a} {b} {c}")

# 튜플은 들어있는 값의 파악이 어려워 key를 넣은 사전이 있다.{}
test_dict = {"name": "동연", "age": 30}
print(test_dict["name"])

user_name, user_age = test_dict.keys()
print(f"{user_name}, {user_age}")