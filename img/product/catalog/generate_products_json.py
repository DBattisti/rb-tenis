import os
import json

# Configuration
IMAGE_FOLDER = '.'  # Current directory
OUTPUT_JSON = 'products.json'  # Output JSON file in current directory
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

def scan_images(folder):
    images = []
    for filename in os.listdir(folder):
        ext = os.path.splitext(filename)[1].lower()
        if ext in SUPPORTED_EXTENSIONS:
            images.append(filename)
    images.sort()
    return images

def build_products(images):
    return [
        {
            'image': f"img/product/catalog/{filename}",
            'name': os.path.splitext(filename)[0][3:].replace('_', ' ')
        }
        for filename in images
    ]

def main():
    images = scan_images(IMAGE_FOLDER)
    products = build_products(images)
    data = {'products': products}
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Wrote {len(products)} products to {OUTPUT_JSON}')

if __name__ == '__main__':
    main()

