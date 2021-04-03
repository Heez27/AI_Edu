from emaillistapp import model

def run_list():
    results = model.findall()
    #index = 1
    #for result in results:
    #    print(f'{index}:{result["first_name"]}')
    #    index = index + 1
    for index, result in enumerate(results):
        print(f'{index+1}:{result["first_name"]} {result["last_name"]}:{result["email"]}')

def run_add(): #insert tuple
    firstname = input('first name: ')
    lastname = input('last name: ')
    email = input('email: ')
    model.insert(firstname, lastname, email)
    run_list()

def run_delete(): #이메일로 튜플 삭제
    email = input('email: ')
    model.deletebyemail(email)
    run_list()

def main():
    while True:
        cmd = input(f'(l)ist, (a)dd, (d)lete, (q)uit > ')

        if cmd == 'q':
            break
        elif cmd == 'l': #리스트를 실행
            run_list()
        elif cmd == 'a':
            run_add()
        elif cmd == 'd':
            run_delete()
        else:
            print('Unknown menu')


        #print(f'execute {cmd}')


if __name__ == '__main__':
    main()