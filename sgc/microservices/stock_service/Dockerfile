# ✅ Utilise une image Python légère
FROM python:3.12-slim

# ✅ Crée un répertoire de travail dans le conteneur
WORKDIR /app

# ✅ Copie tout le contenu du service dans l'image
COPY . .

# ✅ Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Ouvre le port par défaut de Django/Gunicorn
EXPOSE 8000

# ✅ Lance le serveur Django via Gunicorn
CMD ["gunicorn", "stock_app.wsgi:application", "--bind", "0.0.0.0:8000"]
