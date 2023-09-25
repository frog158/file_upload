def process(file, update_fields=[]):
    """
    Общая функция для обработки файла и установки флага 'processed' в True.

    Args:
        file (File): Экземпляр модели File, который будет обработан.
        update_fields (list): Список полей, которые нужно обновить. По умолчанию ["processed"].

    Общая функция `process` используется для обработки файлов разных форматов (jpeg, png, webp, txt).
    Она устанавливает флаг 'processed' в True и сохраняет объект модели.

    Args:
        file (File): Экземпляр модели File, который будет обработан.
        update_fields (list): Список полей, которые нужно обновить. По умолчанию ["processed"].
    """
    file.processed = True
    file.save(update_fields=["processed", *update_fields])


def process_jpeg(file):
    """
    Обработка файла формата JPEG.

    Args:
        file (File): Экземпляр модели File формата JPEG.

    Функция `process_jpeg` выполняет обработку файла формата JPEG и
    устанавливает флаг 'processed' в True.
    """
    # Выполнить обработку формата JPEG.
    process(file)


def process_png(file):
    """
    Обработка файла формата PNG.

    Args:
        file (File): Экземпляр модели File формата PNG.

    Функция `process_png` выполняет обработку файла формата PNG и
    устанавливает флаг 'processed' в True.
    """
    # Выполнить обработку формата PNG.
    process(file)


def process_webp(file):
    """
    Обработка файла формата WebP.

    Args:
        file (File): Экземпляр модели File формата WebP.

    Функция `process_webp` выполняет обработку файла формата WebP
    и устанавливает флаг 'processed' в True.
    """
    # Выполнить обработку формата WebP.
    process(file)


def process_txt(file):
    """
    Обработка текстового файла.

    Args:
        file (File): Экземпляр модели File текстового файла.

    Функция `process_txt` выполняет обработку текстового файла и
    устанавливает флаг 'processed' в True.
    """
    # Выполнить обработку текстового файла.
    process(file)
