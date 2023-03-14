% scale(1000) import("f6.stl");

// Sketch PureShapes 9
multmatrix([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, -1.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 9.000000;
translate([0, 0, -thickness]) {
  translate([3.000000, 12.500000, 0]) {
    rotate([0, 0, -180.0]) {
      cube([41.000000, 25.000000, thickness]);
    }
  }
}
}
