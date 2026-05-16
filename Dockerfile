# Используем официальный образ Python 3.10 (легковесный)
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем библиотеки Python
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры Chromium для Playwright
RUN playwright install chromium

# Копируем весь код проекта внутрь контейнера
COPY . .

# Команда, которая будет выполнена при запуске контейнера
CMD ["pytest", "-v"]

FROM python:3.10-slim

# Установка Java и Allure
RUN apt-get update && \
    apt-get install -y default-jre wget && \
    wget -q -O allure.tgz https://github.com/allure-framework/allure2/releases/download/2.33.0/allure-2.33.0.tgz && \
    tar -zxvf allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.33.0/bin/allure /usr/local/bin/allure && \
    rm allure.tgz

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium

COPY . .

# Создаём папку для результатов Allure
RUN mkdir -p allure-results