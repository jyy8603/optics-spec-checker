"""
Optics Spec Checker

A simple Python tool for checking optical lens design specifications.
This tool checks whether a lens design satisfies basic optical requirements
such as effective focal length, F-number, field angle, and distortion.
"""

from dataclasses import dataclass


@dataclass
class LensSpecification:
    target_efl: float
    efl_tolerance: float
    max_f_number: float
    min_field_angle: float
    max_distortion: float


@dataclass
class LensDesign:
    efl: float
    f_number: float
    field_angle: float
    distortion: float


def check_lens_design(spec: LensSpecification, design: LensDesign) -> dict:
    results = {}

    efl_min = spec.target_efl - spec.efl_tolerance
    efl_max = spec.target_efl + spec.efl_tolerance

    results["Effective Focal Length"] = {
        "value": design.efl,
        "requirement": f"{efl_min:.2f} mm ~ {efl_max:.2f} mm",
        "pass": efl_min <= design.efl <= efl_max,
    }

    results["F-number"] = {
        "value": design.f_number,
        "requirement": f"<= {spec.max_f_number:.2f}",
        "pass": design.f_number <= spec.max_f_number,
    }

    results["Field Angle"] = {
        "value": design.field_angle,
        "requirement": f">= {spec.min_field_angle:.2f} deg",
        "pass": design.field_angle >= spec.min_field_angle,
    }

    results["Distortion"] = {
        "value": design.distortion,
        "requirement": f"<= {spec.max_distortion:.2f} %",
        "pass": design.distortion <= spec.max_distortion,
    }

    return results


def print_report(results: dict) -> None:
    print("\nLens Specification Check Result")
    print("-" * 40)

    overall_pass = True

    for item, result in results.items():
        status = "PASS" if result["pass"] else "FAIL"
        print(f"{item}: {result['value']} | Requirement: {result['requirement']} | {status}")

        if not result["pass"]:
            overall_pass = False

    print("-" * 40)
    print("Overall Result:", "PASS" if overall_pass else "FAIL")


if __name__ == "__main__":
    specification = LensSpecification(
        target_efl=50.0,
        efl_tolerance=2.0,
        max_f_number=4.5,
        min_field_angle=26.5,
        max_distortion=2.0,
    )

    design = LensDesign(
        efl=49.3,
        f_number=4.2,
        field_angle=27.0,
        distortion=1.5,
    )

    check_results = check_lens_design(specification, design)
    print_report(check_results)
