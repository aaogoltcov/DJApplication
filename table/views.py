import csv
import os

from django.shortcuts import render

from app.settings import BASE_DIR
from table.models import File, Header


def set_path(file):
    try:
        if File.objects.values('file')[0]['file'] == os.path.join(BASE_DIR, file):
            return 'Такой файл уже существует!'
    except IndexError:
        File(file=os.path.join(BASE_DIR, file), name=file).save()


def get_path():
    try:
        return File.objects.values('file')[0]['file']
    except IndexError:
        return 'Такого файла не существует!'


CSV_FILENAME = 'phones.csv'


def table_view_new(request):
    set_path(CSV_FILENAME)
    file_path = get_path()
    template = 'table_new.html'
    with open(file_path, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)
        print(Header.objects.order_by('order').values('name', 'width').all())
        context = {
            'columns': Header.objects.order_by('order').values('name', 'width').all(),
            'table': table, 
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
