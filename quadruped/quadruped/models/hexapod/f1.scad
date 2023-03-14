% scale(1000) import("f1.stl");

// Sketch PureShapes 25
multmatrix([[-1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 27.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 25.000000;
translate([0, 0, -thickness]) {
  translate([24.000000, 23.000000, 0]) {
    rotate([0, 0, 180.0]) {
      cube([48.000000, 6.000000, thickness]);
    }
  }
}
}
