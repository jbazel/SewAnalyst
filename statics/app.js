

// write a simple tween object
var tween = KUTE.fromTo('#rectangle',  // target shape
   { path: '#rectangle' }, // from shape
   { path: '#star' }, // to shape
   { // options
      easing: 'easingCubicInOut',
      yoyo: true, repeat: 1, duration: 2500}
 ).start();
