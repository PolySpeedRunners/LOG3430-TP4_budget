import os

bon_commit = input("Indiquer le hash du dernier commit fonctionnel : ")
mauvais_commit = input("Indiquer le hash du commit non-fonctionnel : ")

os.system(f"git bisect start {mauvais_commit} {bon_commit}")
os.system(f"git bisect run python manage.py test")
os.system(f"git bisect reset")