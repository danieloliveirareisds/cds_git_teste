def get_operation():
    op = input('Operação: ')

def gether_data():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    
    op = get_operation()

    return n1, n2, op


def main():
    n1, n2, op = gether_data()
    
    print(eval(n1+op+n2))

    return None


if __name__ == "__main__":
    main()