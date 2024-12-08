# Wolfenstein-3D-Clone
Wolfenstein 3D using OpenGL

Wolfeinstein 3D clone written in Python using Pygame, ModernGL, Numpy, PyTMX, PyGLM

You can create your own level in the Tiled editor, see more details here:
https://youtu.be/yJXuvK_eLrQ?si=ShmzXXb1uSqtDC4u

![wolfenstein](/screenshot/0.jpg)


![wolfenstein](/screenshot/1.jpg)

## Common Issues and Solutions

### Rendering Issues on Windows 11

Some users have reported rendering issues on Windows 11 where only walls are rendered and other elements are missing. This issue may be related to specific hardware configurations or OpenGL settings. Here are some steps to troubleshoot and resolve the issue:

1. **Update Graphics Drivers**: Ensure that your graphics drivers are up to date. Visit the manufacturer's website (e.g., Intel, Nvidia) to download and install the latest drivers.

2. **Check Python and Library Versions**: Make sure you are using compatible versions of Python and the required libraries. The recommended versions are:
   - Python 3.10 or 3.11
   - moderngl 5.8.2
   - numpy 1.26.1
   - pygame 2.5.2
   - PyGLM 2.7.0

3. **Run in Compatibility Mode**: Try running the application in compatibility mode for an earlier version of Windows. Right-click on the executable, go to Properties, and select the Compatibility tab.

4. **Adjust OpenGL Settings**: Some users have found that adjusting OpenGL settings can help. You can try changing the context profile or disabling certain features in the code.

5. **Debugging Information**: If the issue persists, provide detailed debugging information, including console output and screenshots, to help diagnose the problem.

By following these steps, you may be able to resolve the rendering issues and enjoy the game on Windows 11.
