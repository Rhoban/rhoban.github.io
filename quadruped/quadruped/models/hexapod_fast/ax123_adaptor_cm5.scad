% scale(1000) import("ax123_adaptor_cm5.stl");

// Sketch PureShapes 32
multmatrix([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, -1.0, -16.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 32.000000;
translate([0, 0, -thickness]) {
  translate([50.500000, 34.500000, 0]) {
    rotate([0, 0, 180.0]) {
      cube([101.000000, 69.000000, thickness]);
    }
  }
}
}
