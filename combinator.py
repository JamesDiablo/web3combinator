import itertools

def get_combinations(address):

    temp_address = address.replace('0x', '', 1)
    temp_address_list = list(temp_address)
    only_letter_list = []

    for i in range(len(temp_address_list)):
        if temp_address_list[i].isdigit() == False:
            only_letter_list.append(temp_address_list[i])
            temp_address_list[i] = ''

    temp_address_list = tuple(temp_address_list)
    only_letter_list = ''.join(only_letter_list)
    letter_register = list(map(''.join, itertools.product(*zip(only_letter_list.upper(), only_letter_list.lower()))))

    ready_address = []
    for i in letter_register:
        string_letter_register = list(i)
        temp = temp_address_list
        temp = list(temp)
        
        for j in string_letter_register:
            
            for index, x in enumerate(temp):
                if x == '':
                    temp[index] = j
                    break

        ready_address.append('0x' + ''.join(temp))

    print(f'Готово! Все возможные комбинации сохранены в файл {address.lower()}.txt')

    with open(f"{address.lower()}.txt", "w") as file:
        print(*ready_address, file=file, sep="\n")


def main():
    address = str(input('     WELCOME\n------------------\nВведите адрес вашего кошелька: '))
    get_combinations(address)

if __name__ == "__main__":
    main()