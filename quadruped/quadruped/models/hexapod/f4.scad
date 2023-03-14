% scale(1000) import("f4.stl");

// Sketch PureShapes 29
multmatrix([[-1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 14.5], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) {
thickness = 29.000000;
translate([0, 0, -thickness]) {
  translate([-24.000000, 38.000000, 0]) {
    rotate([0, 0, 0.0]) {
      cube([48.000000, 15.700000, thickness]);
    }
  }
  translate([24.000000, 53.700000, 0]) {
    rotate([0, 0, 180.0]) {
      cube([3.000000, 64.700000, thickness]);
    }
  }
  translate([-24.000000, -11.000000, 0]) {
    rotate([0, 0, 0.0]) {
      cube([3.000000, 64.700000, thickness]);
    }
  }
}
}
