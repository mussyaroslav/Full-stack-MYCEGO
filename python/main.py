import os
from PIL import Image

def find_image_folders(root_folder):
    """Ищет все подпапки в указанной папке."""
    folders = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if dirpath != root_folder and any(f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')) for f in filenames):
            folders.append(dirpath)
    return folders

def collect_images(folders):
    """Собирает изображения из всех указанных папок."""
    images = []
    for folder in folders:
        for file_name in os.listdir(folder):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
                file_path = os.path.join(folder, file_name)
                img = Image.open(file_path)
                images.append(img)
    return images

def save_to_tiff(images, output_path):
    """Сохраняет изображения в один TIFF файл."""
    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:], compression="tiff_deflate")
    else:
        print("Нет изображений для сохранения.")

def main():
    # Определяем путь к корневой папке 'img', которая находится на уровень выше
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_folder = os.path.abspath(os.path.join(script_dir, '..', 'img'))
    output_path = os.path.join(script_dir, 'Result.tif')  # Имя выходного файла

    # Находим все подпапки с изображениями
    image_folders = find_image_folders(root_folder)

    # Собираем изображения из всех найденных папок
    images = collect_images(image_folders)

    # Сохраняем изображения в один TIFF файл
    save_to_tiff(images, output_path)
    print(f'Сохранено {len(images)} изображений в {output_path}')

if __name__ == '__main__':
    main()
