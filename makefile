.PHONY: format lint

# Форматирование кода
format:
	black .
	isort .

# Проверка стиля и линтинг
lint:
	flake8 .
