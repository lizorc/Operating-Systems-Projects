import os
import math
import datetime
import json
from initials import MAX_CHUNK_SIZE, INPUT_PATH, OUTPUT_PATH

input_path = INPUT_PATH
output_path = OUTPUT_PATH

def do_backup():
  while True:
    path = input(f'Carpeta para backup: ')
    if not path:
      print('No se ha introducido ninguna ruta')
    elif not os.path.exists(path):
      print('La ruta no existe')
    else:
      break

  output_path = input(f'Carpeta de salida de backup ({OUTPUT_PATH}): ')
  if not output_path:
    output_path = OUTPUT_PATH
  if not os.path.exists(output_path):
    os.makedirs(output_path)
  backup_folder_into(path, output_path)

def backup_folder_into(input_path, output_path):
  files_list = get_folder_info(input_path)
  folder_total_size = sum([size for _, size in files_list])

  actual_time = datetime.datetime.now()
  filename = actual_time.strftime("%Y%m%d_%H%M%S")

  total_size = 0
  actual_chunk = 0
  output_file = get_filepart(output_path, filename, actual_chunk)
  for f, size in files_list:
    with open(f, 'rb') as input_file:
      if total_size + size <= MAX_CHUNK_SIZE:
        output_file.write(input_file.read())
        total_size += size
      else:
        output_file.write(input_file.read(MAX_CHUNK_SIZE - total_size))
        gap = size - (MAX_CHUNK_SIZE - total_size)
        output_file.close()

        total_size = 0
        actual_chunk += 1
        output_file = get_filepart(output_path, filename, actual_chunk)
        output_file.write(input_file.read())
        total_size += gap

  print(f'---------------------------------------------')
  print(f'| Backup completado para {input_path} en {output_path}')
  print(f'---------------------------------------------')
  backup_data = {
    'created_at': actual_time.strftime("%Y-%m-%d %H:%M:%S"),
    'input_path': os.path.abspath(input_path),
    'output_path': os.path.abspath(output_path),
    'filename': filename,
    'chunks': actual_chunk + 1,
    'files': files_list,
    'total_size': folder_total_size
  }

  data = []
  if os.path.exists('data.json'):
    with open('data.json', 'r') as file:
      data = json.load(file)

  data.append(backup_data)

  json_data = json.dumps(data)
  with open('data.json', 'w') as file:
    file.write(json_data)

  # print('----REPORT----')
  # print(f'Created at: {actual_time.strftime("%Y-%m-%d %H:%M:%S")}')
  # print(f'Input path: {input_path}')
  # print(f'Output path: {output_path}')
  # print(f'Filename: {filename}')
  # print(f'Chunks: {actual_chunk + 1}')
  # print('Total size: {0:.3f} GB'.format(folder_total_size / 1024 / 1024 / 1024))

def get_folder_info(folder_path):
  files_list = []
  for root, _, files in os.walk(folder_path):
    for filename in files:
      path = os.path.join(root, filename)
      abs_path = os.path.abspath(path)
      size = os.path.getsize(path)
      files_list.append((abs_path, size))
  return files_list

def get_filepart(folder, name, num):
  return open(f'{folder}/{name}_{num}', 'xb')