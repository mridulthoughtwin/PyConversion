
def handle_uploaded_file(f):
    with open('name.txt', 'rb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)