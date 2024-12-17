from pdf2image import convert_from_path
import os

# Function to convert PDF to images
def pdf_to_images(pdf_path, output_dir, dpi=300):
    
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=r"C:\Users\Sanjal PC\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin")
    image_paths = []

    # Save each page as an image
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"pages_{i + 1}.png") 
        image.save(image_path, "PNG")
        print(f"Saved image: pages_{i + 1}.png successfully")  
        image_paths.append(image_path)

    return image_paths


if __name__ == "__main__":
    pdf_path = r"C:\Users\Sanjal PC\OneDrive\Desktop\Bank cheques.pdf"  
    output_dir = r"C:\Users\Sanjal PC\OneDrive\Desktop\output_images"  
    images = pdf_to_images(pdf_path, output_dir)

    print(f"\nPDF converted to images and saved in folder: {output_dir}")
    print("Saved pages:")
    for image in images:
        print(image)
