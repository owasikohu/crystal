#include <X11/Xlib.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    Display *dpy;
    XWindowAttributes attr;
    
    if(!(dpy = XOpenDisplay(0x0))) return 1;


}
