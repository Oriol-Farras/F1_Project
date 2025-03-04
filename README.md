# F1_Project

Aquest és un projecte desenvolupat amb Django que proporciona informació sobre la Fórmula 1.

## 📌 Requisits

Abans d'executar el projecte, assegura't de tenir instal·lats els següents programes:

- Python 3.x  
- Docker   
- Git 

## 🚀 Instal·lació i execució

Segueix aquests passos per posar en marxa el projecte:

### 1️⃣ Clonar el repositori
```bash
git clone https://github.com/usuari/F1_Project.git
cd F1_Project
```

### 2️⃣ Crear i activar un entorn virtual (opcional però recomanat)
```bash
python -m venv venv
source venv/bin/activate  # Per a Linux i Mac
venv\Scripts\activate     # Per a Windows
```

### 3️⃣ Instal·lar les dependències
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar les migracions
```bash
python manage.py migrate
```

### 5️⃣ Executar el servidor de desenvolupament
```bash
python manage.py runserver
```

El projecte estarà disponible a `http://127.0.0.1:8000/`.

---

## 🐳 Executar amb Docker (Opcional)

Si prefereixes utilitzar Docker, assegura't de tenir Docker i Docker Compose instal·lats i executa:

```bash
docker-compose up --build
```

Això iniciarà el servei en un contenidor.

---

## 👥 Integrants del projecte

- **Oriol Farràs Sans**


---


