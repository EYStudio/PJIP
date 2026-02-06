from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QByteArray, Qt


def svg_to_pixmap(svg_text: str, size: int = 256) -> QPixmap:
    """Render SVG text into a QPixmap with transparent background."""
    renderer = QSvgRenderer(QByteArray(svg_text.encode("utf-8")))

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)
    renderer.render(painter)
    # renderer.render(painter, pixmap.rect())
    painter.end()

    return pixmap


def svg_to_icon(svg_text: str, size: int = 256) -> QIcon:
    """Convert SVG text directly into a QIcon."""
    pixmap = svg_to_pixmap(svg_text, size)
    return QIcon(pixmap)
