# PyQt Notepad
Lightweight notepad written in PyQt6. Supports opening, saving, 4 styles, font settings.

![Screenshot](https://github.com/l1mafresh/pyqt-notepad/blob/main/screenshot.png)

## Important
If you are going to run this program on Windows or macOS, remove the line

```
self.setWindowIcon(QtGui.QIcon.fromTheme(u"accessories-text-editor"))
```

it loads the system notepad icon, but this is only for those who have Linux.
