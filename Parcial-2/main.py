import backup
import restore

def print_menu():
  print(f'¿Qué quieres hacer? (Escoge una opción)')
  print(f'1. Hacer backup de una carpeta')
  print(f'2. Restaurar un backup')
  print(f'0. Salir')

def is_float(element):
  if element is None:
    return False
  try:
    float(element)
    return True
  except ValueError:
    return False

if __name__ == '__main__':
  print_menu()

  while True:
    option = input(': ')
    if not option:
      continue

    if not is_float(option):
      print('Opción no válida')
      print()

    elif int(option) == 1:
      backup.do_backup()
      print()
      print_menu()

    elif int(option) == 2:
      restore.do_restore()
      print()
      print_menu()

    elif int(option) == 0:
      break

    else:
      print()