% scale(1000) import("f3.stl");

// Sketch PureShapes 25
multmatrix([[0.0, 0.0, -1.0, -12.5], [-1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 25.000000;
translate([0, 0, -thickness]) {
  translate([0.000000, 19.000000, 0]) {
    rotate([0, 0, 180.0]) {
      cube([4.300000, 38.000000, thickness]);
    }
  }
}
}
