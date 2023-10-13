# 1) Нахождение элемента
# def m_elemnt(nums):
#     n = len(nums)
#     m = {}
#
#     for num in nums:
#         if num in m:
#             m[num] += 1
#         else:
#             m[num] = 1
#     for num, freq in m.items():
#         if freq > n / 2:
#             return num
#     return 0
#
# masiv = input("Укажите числа через пробел: ").split()
# masiv = [int(num) for num in masiv]
#
# result = m_elemnt(masiv)
# print(f"Самый повторяющийся элемент: {result}")

# 2) Двоичная система
# bi_num = "10101"
# g_num = 0
# length = len(bi_num)
#
# for i in range(length):
#     if bi_num[i] == "1":
#         power = length - 1 - i
#         result = 1
#         for l in range(power):
#             result *= 2
#         g_num += result
#
# print(g_num)

# 3) Преобразователь 32-Бит
# def num_32b(s):
#     s = s.strip()
#     if not s:
#         return 0
#     g = -1 if s[0] == '-' else 1
#     s = s[s[0] == '-':]
#
#     result = 0
#     for char in s:
#         if '0' <= char <= '9':
#             result = result * 10 + ord(char) - ord('0')
#         else:
#             break
#     return max(min(result * g, 2 ** 31 - 1), -2 ** 31)
#
# u_input = input("Укажите число: ")
# result = num_32b(u_input)
# print("Результат: ", result)

# 4) Удаление из масива
# def clear(nums):
#     unique_nums = list(set(nums))
#
#     if len(unique_nums) % 2 != 0:
#         unique_nums[-1], unique_nums[-2] = unique_nums[-2], unique_nums[-1]
#     result = []
#
#     for i in range(0, len(unique_nums), 2):
#         if i + 1 < len(unique_nums):
#             result.append(unique_nums[i + 1])
#             result.append(unique_nums[i])
#         else:
#             result.append(unique_nums[i])
#     return result
#
# u_input = input("Укажите числа через пробел: ")
# a_nums = [int(num) for num in u_input.split()]
#
# result = clear(a_nums)
# print("Результат:", result)

# 5) Игра пристолов
# import random
#
# n = random.randint(1, 3)
# m_serii = n * 5
# watched_ep = set()
#
# for _ in range(m_serii):
#     season = random.randint(1, n)
#     episode = random.randint(1, 5)
#     watched_ep.add((season, episode))
#
# missing_ep = [(s, e) for s in range(1, n + 1) for e in range(1, 6) if (s, e) not in watched_ep]
#
# k = len(missing_ep)
# print("Количество утерянных серий:", k)
#
# missing_ep.sort(key=lambda x: (x[0], x[1]))
# cseason = None
#
# print(f"\nСписок сезонов и серий (Утерянные серии выделены скобками):")
#
# for s in range(1, n + 1):
#     episodes_in_season = [e for e in range(1, 6) if (s, e) not in watched_ep]
#     episode_str = " ".join([f"({e})" if e in episodes_in_season else str(e) for e in range(1, 6)])
#     print(f"Сезон {s}: {episode_str}")
#
# print(f"\n!!!Подсчет серий прошел успешно!!!")