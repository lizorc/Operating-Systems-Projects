import os
import json

def do_restore():
  restore_data = get_restore_info()
  if len(restore_data) == 0:
    print(f'No hay backups para restaurar')
    return

  while True:
    print(f'Escoge un backup para restaurar')
    for (i, d) in enumerate(restore_data):
      print(f'{i}. {d["input_path"]} (creado el {d["created_at"]})')
      last = i
    option = input (': ')
    if not option:
      print('No se ha introducido ninguna opción')
    if int(option) < 0 or int(option) > last:
      print('Opción no válida')
    else:
      break

  while True:
    output_path = input(f'Carpeta para restaurar: ')
    if not output_path:
      print('No se ha introducido ninguna ruta')
    else:
      break

  if not os.path.exists(output_path):
    os.makedirs(output_path)

  restore_to(restore_data[int(option)], output_path)

def restore_to(input_data, output_path):
  output_path = os.path.abspath(output_path) + '/'
  backup_path = os.path.abspath(input_data['output_path']) + '/' + input_data['filename'] + '_'

  actual_chunk = 0
  backup_file = open(backup_path + str(actual_chunk), 'rb')
  backup_size = os.path.getsize(backup_path + str(actual_chunk))
  for f in input_data['files']:
    filename = f[0].replace(input_data['input_path'] + '/', '')
    file_size = f[1]

    if filename.rfind('/') >= 0:
      file_folders = filename[0:filename.rfind('/')]
      if not os.path.exists(output_path + file_folders):
        os.makedirs(output_path + file_folders)

    if backup_size >= file_size:
      with open(output_path + filename, 'xb') as output_file:
        output_file.write(backup_file.read(file_size))
      backup_size -= file_size
    else:
      with open(output_path + filename, 'xb') as output_file:
        output_file.write(backup_file.read())
      file_size -= backup_size
      backup_file.close()

      actual_chunk += 1
      backup_file = open(backup_path + str(actual_chunk), 'rb')
      backup_size = os.path.getsize(backup_path + str(actual_chunk))
      with open(output_path + filename, 'ab') as output_file:
        output_file.write(backup_file.read(file_size))
      backup_size -= file_size

  #print(input_data)
  #print(output_path)

def get_restore_info():
  try:
    with open('data.json', 'r') as file:
      data = json.load(file)
    return data
  except:
    return []