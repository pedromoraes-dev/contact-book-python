from contact_book import ContactBook
agenda = ContactBook()

while True:
    
    print('''
          -Agenda de Contatos-
          
          1 - Adicionar contato
          2 - Listar contato(s)
          3 - Buscar contato
          4 - Remover contato
          5 - Sair
          ''')
    
    choice = input('Escolha uma das opções acima: ')
    if not choice.isdigit():
        print('Digite apenas números.')
        continue
    choice = int(choice)
    
    if choice == 1:
        name = input('Digite o nome: ')
        phone = input('Digite o número: ')
        email = input('Digite o email: ')
        agenda.add_contact(name, phone, email)
        
    elif choice == 2:
        agenda.list_contact()
        
    elif choice == 3:
        name = input('Digite o nome do contato que deseja buscar: ')
        agenda.search_contact(name)
        
    elif choice == 4:
        name = input('Digite o nome do contato que deseja remover: ')
        agenda.remove_contact(name)
        
    elif choice == 5: 
        print('Fechando a agenda...')
        break
    
    else:
        print('Opção inválida.')
        