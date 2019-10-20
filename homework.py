'''Define class method to check if number is prime.
Define class method to validate if given PESEL number is valid
'''

class Homework(object):

    def prime_num(self, num):

        if num <= 1:
            return 'Nie'

        for i in range(2, num):
            if num % i == 0:
                return 'Nie'
            if num % i != 0:
                return 'Tak'


    def val_pesel(self, num: int) -> bool:
        temp_num = str(num)

        temp_list = [int(i) for i in temp_num] # list of digits of a given number
        multiple_by = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1] # pattern
        result = [temp_list * multiple_by for temp_list, multiple_by in zip(temp_list, multiple_by)] # multiply 2 lists

        temp_num_2 = sum(result)

        if temp_num_2 % 10 == 0:
            return 'D'  # 'D' means PESEL is valid
        else:
            return 'N'  # 'N' PESEL is incorrect

h = Homework()
h.val_pesel(44051401458)
# print(h.prime_num(3))