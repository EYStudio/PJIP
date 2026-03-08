import os
from pathlib import Path
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt
from PySide6.QtWidgets import QWidget


def get_cached_wallpaper():
    """Get Windows cached wallpaper"""
    themes_dir = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Themes"
    cached_file = themes_dir / "TranscodedWallpaper"
    if cached_file.exists():
        return cached_file
    cached_dir = themes_dir / "CachedFiles"
    if cached_dir.exists():
        files = list(cached_dir.glob("*"))
        if files:
            return max(files, key=lambda f: f.stat().st_mtime)
    return None

class WallpaperBlurBackground:
    def __init__(self, widget: QWidget, enable_blured_background: bool, blur_radius=20):
        self.widget = widget
        self.enable_blured_background = enable_blured_background
        wallpaper_path = get_cached_wallpaper()
        if not wallpaper_path:
            raise FileNotFoundError("Can not find wallpaper")

        img = Image.open(wallpaper_path).convert("RGB")
        img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

        self._blurred_pixmap = QPixmap.fromImage(ImageQt(img))
        self._scaled_pixmap = None
        self.update_background()

    @staticmethod
    def _crop_center(pixmap: QPixmap, target_ratio):
        w, h = pixmap.width(), pixmap.height()
        ratio = w / h
        if ratio > target_ratio:
            new_w = int(h * target_ratio)
            x = (w - new_w) // 2
            return pixmap.copy(x, 0, new_w, h)
        else:
            new_h = int(w / target_ratio)
            y = (h - new_h) // 2
            return pixmap.copy(0, y, w, new_h)

    def update_background(self):
        if not self.enable_blured_background:
            return
        size = self.widget.size()
        if size.width() <= 0 or size.height() <= 0:
            return
        target_ratio = size.width() / size.height()
        cropped = self._crop_center(self._blurred_pixmap, target_ratio)
        self._scaled_pixmap = cropped.scaled(
            size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        # self.widget.update()

    def paint_event(self):
        if not self.enable_blured_background:
            return
        painter = QPainter(self.widget)
        painter.drawPixmap(0, 0, self._scaled_pixmap)
