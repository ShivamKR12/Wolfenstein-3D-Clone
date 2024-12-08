# Wolfenstein-3D-Clone
Wolfenstein 3D using OpenGL

Wolfeinstein 3D clone written in Python using Pygame, ModernGL, Numpy, PyTMX, PyGLM

You can create your own level in the Tiled editor, see more details here:
https://youtu.be/yJXuvK_eLrQ?si=ShmzXXb1uSqtDC4u

![wolfenstein](/screenshot/0.jpg)


![wolfenstein](/screenshot/1.jpg)

## Tested Configurations

The following configurations have been tested and are known to work:

- **Operating System**: Windows 11
- **Graphics Drivers**: Latest versions for Intel Iris XE and Nvidia RTX A2000
- **Python Version**: 3.9
- **Pygame Version**: 2.5.1
- **ModernGL Version**: 5.8.2
- **PyGLM Version**: 2.7.0
- **Numpy Version**: 1.25.2
- **PyTMX Version**: 3.32

## Known Issues

- **Rendering Issues**: Some users have reported rendering issues on Windows 11. Ensure your graphics drivers are up to date.
- **Compatibility**: Verify that the game is compatible with your system. Some older libraries or dependencies might not work well with the latest operating system.
- **Texture Loading Warnings**: Logs may contain repeated libpng warnings about incorrect sRGB profiles. This suggests a potential issue with how textures are loaded and processed, possibly affecting visual output.
