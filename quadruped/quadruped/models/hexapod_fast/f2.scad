% scale(1000) import("f2.stl");

// Sketch PureShapes 25
multmatrix([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, -1.0, -12.5], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 25.000000;
translate([0, 0, -thickness]) {
  translate([-24.400000, -11.000000, 0]) {
    rotate([0, 0, 0.0]) {
      cube([3.400000, 37.000000, thickness]);
    }
  }
  translate([-24.400000, 19.000000, 0]) {
    rotate([0, 0, 0.0]) {
      cube([48.800000, 7.000000, thickness]);
    }
  }
  translate([24.400000, 26.000000, 0]) {
    rotate([0, 0, 180.0]) {
      cube([3.400000, 37.000000, thickness]);
    }
  }
}
}
