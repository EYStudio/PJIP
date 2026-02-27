import os
from pathlib import Path
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt

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


# noinspection PyAttributeOutsideInit
# noinspection PyPep8Naming
class WallpaperBlurMixin:
    def init_wallpaper_background(self, blur_radius=20):
        wallpaper_path = get_cached_wallpaper()
        if not wallpaper_path:
            raise FileNotFoundError("Can not find wallpaper")

        img = Image.open(wallpaper_path).convert("RGB")
        img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

        self._blurred_pixmap = QPixmap.fromImage(ImageQt(img))
        self._scaled_pixmap = None
        self.update_background()

    def _crop_center(self, pixmap, target_ratio):
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
        size = self.size()
        if size.width() <= 0 or size.height() <= 0:
            return
        target_ratio = size.width() / size.height()
        cropped = self._crop_center(self._blurred_pixmap, target_ratio)
        self._scaled_pixmap = cropped.scaled(
            size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.update()

    def paintEvent(self, event):
        if hasattr(self, "_scaled_pixmap") and self._scaled_pixmap:
            painter = QPainter(self) # type: ignore
            painter.drawPixmap(0, 0, self._scaled_pixmap)
        super().paintEvent(event) # type: ignore

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event) # type: ignore