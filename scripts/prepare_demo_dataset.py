from pathlib import Path
import argparse
import numpy as np
from src.utils.image_io import save_uint8


def parse_args():
    parser = argparse.ArgumentParser(description="Create several toy SAR-like demo images.")
    parser.add_argument("--output_dir", type=str, default="datasets/SDS-SAR-Demo/input")
    parser.add_argument("--num_images", type=int, default=3)
    parser.add_argument("--size", type=int, default=256)
    return parser.parse_args()


def main():
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(2026)
    for idx in range(args.num_images):
        base = np.zeros((args.size, args.size), dtype=np.float32)
        yy, xx = np.mgrid[:args.size, :args.size]

        # Simple bright structures.
        base += np.exp(-((xx - args.size * 0.45) ** 2 + (yy - args.size * 0.45) ** 2) / (2 * (args.size * 0.08) ** 2))
        base += 0.7 * np.exp(-((xx - args.size * 0.65) ** 2 + (yy - args.size * 0.60) ** 2) / (2 * (args.size * 0.05) ** 2))
        base += 0.15

        # Multiplicative speckle-like noise.
        speckle = rng.gamma(shape=1.0, scale=1.0, size=base.shape).astype(np.float32)
        noisy = base * speckle
        noisy = noisy / (noisy.max() + 1e-8)

        save_uint8(output_dir / f"demo_{idx + 1:02d}.png", noisy)

    print(f"Demo images saved to: {output_dir}")


if __name__ == "__main__":
    main()
