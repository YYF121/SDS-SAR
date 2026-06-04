import cv2
import numpy as np


class PlaceholderDespeckler:
    """A lightweight placeholder with the same call interface as the future SDS-SAR model.

    This class only applies a simple median filter so that the repository can be tested
    before the official trained model is released.
    """

    def __init__(self, checkpoint=None, device="cuda"):
        self.checkpoint = checkpoint
        self.device = device

    def __call__(self, image: np.ndarray) -> np.ndarray:
        if image.ndim != 2:
            raise ValueError("Expected a single-channel SAR intensity image.")
        image = image.astype(np.float32)
        filtered = cv2.medianBlur((image * 255.0).clip(0, 255).astype(np.uint8), 3)
        return filtered.astype(np.float32) / 255.0
