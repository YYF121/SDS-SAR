import argparse
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

from src.models.placeholder_model import PlaceholderDespeckler
from src.utils.image_io import read_grayscale, save_uint8


def parse_args():
    parser = argparse.ArgumentParser(description="Test script for SDS-SAR despeckling.")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory of input SAR intensity images.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save despeckled results.")
    parser.add_argument("--checkpoint", type=str, default=None, help="Path to pretrained checkpoint.")
    parser.add_argument("--device", type=str, default="cuda", help="Device used by the official model.")
    return parser.parse_args()


def main():
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    image_paths = []
    for suffix in ["*.png", "*.jpg", "*.jpeg", "*.tif", "*.tiff"]:
        image_paths.extend(input_dir.glob(suffix))

    if len(image_paths) == 0:
        raise FileNotFoundError(f"No images found in {input_dir}")

    # Placeholder interface. Replace it with the official SDS-SAR model when released.
    model = PlaceholderDespeckler(checkpoint=args.checkpoint, device=args.device)

    for image_path in tqdm(image_paths, desc="Testing"):
        image = read_grayscale(image_path)
        result = model(image)
        save_uint8(output_dir / image_path.with_suffix(".png").name, result)

    print(f"Done. Results saved to: {output_dir}")


if __name__ == "__main__":
    main()
