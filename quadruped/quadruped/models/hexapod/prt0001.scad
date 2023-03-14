% scale(1000) import("prt0001.stl");

// Sketch PureShapes 32.4
multmatrix([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 16.400000000000002], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 32.400000;
translate([0, 0, -thickness]) {
  translate([16.000000, 11.500000, 0]) {
    rotate([0, 0, -180.0]) {
      cube([32.000000, 50.000000, thickness]);
    }
  }
}
}
