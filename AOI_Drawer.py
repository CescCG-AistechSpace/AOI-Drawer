import cv2
import numpy as np

class PolygonTool:
    def __init__(self, image_path):
        self.original = cv2.imread(image_path)
        if self.original is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        self.image = self.original.copy()
        self.points = []
        self.opacity = 0.7  # 50% opacity
        self.color = (255, 100, 0)  # Blue color (BGR format)
        
        # Create window
        cv2.namedWindow('Polygon Tool', cv2.WINDOW_AUTOSIZE)
         # Get screen dimensions
        screen = cv2.getWindowImageRect('Polygon Tool')
        screen_width = screen[2]
        screen_height = screen[3]
        
        # Set window size to maximum available space
        cv2.resizeWindow('Polygon Tool', screen_width, screen_height)
        cv2.moveWindow('Polygon Tool', 0, 0)  # Position window at top-left
        cv2.setMouseCallback('Polygon Tool', self.mouse_callback)
        
        print("Instructions:")
        print("- Left click: Add polygon point")
        print("- 'r': Reset image")
        print("- 'q': Quit")
        print("- 'z': Undo last point")
    
    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Add point to polygon
            self.points.append((x, y))
            # Draw point
            cv2.circle(self.image, (x, y), 3, (255, 0, 0), -1)
            # Draw lines between points
            if len(self.points) > 1:
                cv2.line(self.image, self.points[-2], self.points[-1], (255, 0, 0), 2)

                if len(self.points) >= 3:
                    if self.points[0][0]-4 < x < self.points[0][0]+4 and self.points[0][1]-4 < y < self.points[0][1]+4:
                        self.fill_polygon()      
                        self.points = []  # Reset points for next polygon
 
    
    def fill_polygon(self):
        if len(self.points) < 3:
            return
        
        # Create overlay
        overlay = self.image.copy()
        
        # Convert points to numpy array
        pts = np.array(self.points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        
        # Fill polygon on overlay
        cv2.fillPoly(overlay, [pts], self.color)
        
        # Blend with original using opacity
        self.image = cv2.addWeighted(overlay, self.opacity, self.image, 1 - self.opacity, 0)

    def undo_last_point(self):
        if len(self.points) > 0:
            self.points.pop()  # Remove the last point
            self.image = self.original.copy()  # Reset the image
            
            # Redraw all remaining points and lines
            for i, point in enumerate(self.points):
                cv2.circle(self.image, point, 3, (255, 0, 0), -1)
                if i > 0:  # Draw line from previous point
                    cv2.line(self.image, self.points[i-1], point, (255, 0, 0), 2)
    
    def reset(self):
        self.image = self.original.copy()
        self.points = []
    
    def run(self):
        while True:
              # Check if window has been closed
            if cv2.getWindowProperty('Polygon Tool', cv2.WND_PROP_VISIBLE) < 1:
                break

            cv2.imshow('Polygon Tool', self.image)
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.reset()
            elif key == ord('z'): 
                self.undo_last_point()
        
        cv2.destroyAllWindows()

