from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl, QSize, QRectF, QRect, QSizeF
from PySide2.QtGui import QImage, QPainter, QBrush, QPen, QPixmap, QColor
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtCore import Qt
from PySide2.QtMultimediaWidgets import QVideoWidget, QGraphicsVideoItem

import opentimelineio as otio
from PySide2.QtWidgets import QWidget, QStackedLayout, QLabel, QGraphicsScene, QGraphicsView, QGraphicsTextItem, \
    QGraphicsRectItem

class ThumbnailViewer(QWidget):

    def __init__(self, *args, **kwargs):

        super(ThumbnailViewer, self).__init__(*args, **kwargs)
       
        self.image_viewer = QLabel("Thumbnail Viewer")
        self.layout= QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.image_viewer)    
        self.setLayout(self.layout)
       

    def update_thumbnail(self,clip):
        if isinstance(clip, otio.schema.Clip):
                path = clip.media_reference.target_url
                path = QUrl(path)
                print (path) 
                # if path.startswith('file://'):
                if path.isLocalFile():
                    path = path.path()
                    path = path[1:]
                    print (path)
                
                pixmap = QPixmap(path)
                pixmap = pixmap.scaled(648,1152,QtCore.Qt.KeepAspectRatio)
                self.image_viewer.setPixmap(pixmap)

    def next_thumbnail(self):
        pass

    def previous_thumbnail(self):
        pass


