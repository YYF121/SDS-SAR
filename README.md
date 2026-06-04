# Self-supervised Despeckling Based Solely on SAR Intensity Images: A General Strategy

Official repository for **Self-supervised Despeckling Based Solely on SAR Intensity Images: A General Strategy**.

SDS-SAR provides a general self-supervised despeckling strategy for SAR intensity images. It is designed to train despeckling networks using only speckled SAR intensity images, without requiring speckle-free references, multi-temporal stacks, SLC data, or additional modality assumptions.

> The code, pretrained models, and dataset links will be progressively released.

<p align="center">
  <img src="assets/framework.png" width="90%">
</p>

## News

- **2026.01**: Paper published in *ISPRS Journal of Photogrammetry and Remote Sensing*.
- **2026.XX**: Initial repository framework released.

## Paper

**Self-supervised despeckling based solely on SAR intensity images: A general strategy**  
Liang Chen, Yifei Yin, Hao Shi, Jingfei He, Wei Li  
*ISPRS Journal of Photogrammetry and Remote Sensing*, vol. 231, pp. 854--873, 2026.  
DOI: [10.1016/j.isprsjprs.2025.11.025](https://doi.org/10.1016/j.isprsjprs.2025.11.025)

## Highlights

- A self-supervised despeckling strategy based solely on SAR intensity images.
- A theoretical criterion for training without speckle-free SAR references.
- Random-Aware sub-SAMpler with Projection correLation Estimation (**RA-SAMPLE**) for constructing mutually independent training pairs.
- A multi-feature loss combining despeckling, regularization, and perceptual terms.
- Applicable to diverse SAR intensity images and multiplicative coherent imaging noise.

## Repository Structure

```text
SDS-SAR/
├── assets/                  # Figures used in README
│   └── framework.png         # Put the framework figure here
├── checkpoints/              # Pretrained models, not tracked by git
├── configs/                  # Training and testing configs
│   └── sds_sar_test.yaml
├── datasets/                 # Dataset links and demo data
│   ├── README.md
│   └── SDS-SAR-Demo/
│       ├── input/
│       └── output/
├── scripts/                  # Entry scripts
│   ├── test.py
│   └── prepare_demo_dataset.py
├── src/                      # Core implementation
│   ├── models/
│   │   └── placeholder_model.py
│   └── utils/
│       └── image_io.py
├── CITATION.cff
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/YYF121/SDS-SAR.git
cd SDS-SAR

conda create -n sds-sar python=3.9 -y
conda activate sds-sar

pip install -r requirements.txt
```

## Quick Test

After placing SAR intensity images in `datasets/SDS-SAR-Demo/input/`, run:

```bash
python scripts/test.py \
  --input_dir datasets/SDS-SAR-Demo/input \
  --output_dir datasets/SDS-SAR-Demo/output \
  --checkpoint checkpoints/sds_sar.pth
```

The current script provides a clean testing interface and a fallback placeholder filter. Replace `src/models/placeholder_model.py` with the released SDS-SAR network when the model code is ready.

## Dataset

The SDS-SAR dataset will be released through one or more public links.

Recommended dataset layout:

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

Please see [`datasets/README.md`](datasets/README.md) for details.

## TODO

- [ ] Release training code.
- [ ] Release testing code with official network.
- [ ] Release pretrained checkpoints.
- [ ] Release dataset download links.
- [ ] Add quantitative evaluation scripts.
- [ ] Add visual examples.

## Citation

If this work is useful for your research, please cite:

```bibtex
@article{chen2026sds_sar,
  title   = {Self-supervised despeckling based solely on SAR intensity images: A general strategy},
  author  = {Chen, Liang and Yin, Yifei and Shi, Hao and He, Jingfei and Li, Wei},
  journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
  volume  = {231},
  pages   = {854--873},
  year    = {2026},
  doi     = {10.1016/j.isprsjprs.2025.11.025}
}
```

## Contact

For questions, please contact:

- Yifei Yin: 513843129@qq.com

## Acknowledgement

This repository is built for the SDS-SAR paper. We thank the SAR image despeckling and self-supervised learning communities for their valuable research foundations.

## License

This project is released for academic research. Please refer to the LICENSE file for details.
