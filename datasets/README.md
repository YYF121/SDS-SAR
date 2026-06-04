# Dataset

This folder contains instructions for preparing the SDS-SAR datasets.

## Dataset Status

The full datasets will be released after cleaning and license checking.

## Recommended Layout

```text
datasets/
├── SDS-SAR-Train/
│   ├── Sentinel-1/
│   ├── TerraSAR-X/
│   ├── RADARSAT-2/
│   └── GF-3/
├── SDS-SAR-Test/
│   ├── synthetic/
│   └── real/
└── SDS-SAR-Demo/
    ├── input/
    └── output/
```

## Demo Data

Put several SAR intensity images into:

```text
datasets/SDS-SAR-Demo/input/
```

Supported formats in the provided demo script:

- `.png`
- `.jpg`
- `.jpeg`
- `.tif`
- `.tiff`

Then run:

```bash
python scripts/test.py \
  --input_dir datasets/SDS-SAR-Demo/input \
  --output_dir datasets/SDS-SAR-Demo/output \
  --checkpoint checkpoints/sds_sar.pth
```

## Notes

- The method is designed for SAR intensity images.
- Input images are converted to single-channel grayscale images in the demo script.
- For training, normalize SAR intensity images consistently with the official implementation.
