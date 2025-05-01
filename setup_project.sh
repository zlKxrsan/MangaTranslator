#!/bin/bash

# Projektstruktur anlegen
mkdir -p backend/models
mkdir -p backend/routes
mkdir -p backend/templates
mkdir -p backend/static
mkdir -p tests

# Python-Dateien erstellen
touch backend/app.py
touch backend/models/__init__.py
touch backend/models/ocr_model.py
touch backend/models/translation_model.py
touch backend/models/image_processing.py
touch backend/models/utils.py
touch backend/routes/__init__.py
touch backend/routes/ocr_route.py
touch backend/routes/translate_route.py
touch backend/routes/image_route.py
touch backend/templates/index.html
touch backend/static/styles.css
touch config.py
touch requirements.txt
touch Dockerfile
touch .gitignore
touch README.md

# Test-Dateien erstellen
touch tests/__init__.py
touch tests/test_ocr.py
touch tests/test_translation.py
touch tests/test_routes.py
touch tests/test_frontend.py
touch tests/test_integration.py

echo "Project structure created successfully!"

