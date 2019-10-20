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


    def val_pesel(self, num: int) -> bool:  #spróbować zsumowaną liczbę weryfikować przez modulo 10 (%10)
        temp_num = str(num)

        temp_list = [int(i) for i in temp_num] #list of num each digit
        multiple_by = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1] #pattern
        result = [temp_list * multiple_by for temp_list, multiple_by in zip(temp_list, multiple_by)] # multiple 2 lists

        temp_num_2 = str(sum(result)) #return sum of the list 'result' and convert to string
        temp_list_2 = [int(i) for i in temp_num_2] #create list with digits from temp_num_2 number

        if temp_list_2[-1] == 0: #prawidłowy
            return 'D'
        else:
            return 'N' #Nieprawidłowy

h = Homework()
h.val_pesel(44051401458)
# print(h.prime_num(3))