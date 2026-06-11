from optics_spec_checker import LensSpecification, LensDesign, check_lens_design


def test_lens_design_passes_all_requirements():
    spec = LensSpecification(
        target_efl=50.0,
        efl_tolerance=2.0,
        max_f_number=4.5,
        min_field_angle=26.5,
        max_distortion=2.0,
    )

    design = LensDesign(
        efl=50.0,
        f_number=4.0,
        field_angle=27.0,
        distortion=1.0,
    )

    results = check_lens_design(spec, design)

    assert results["Effective Focal Length"]["pass"] is True
    assert results["F-number"]["pass"] is True
    assert results["Field Angle"]["pass"] is True
    assert results["Distortion"]["pass"] is True


def test_lens_design_fails_distortion_requirement():
    spec = LensSpecification(
        target_efl=50.0,
        efl_tolerance=2.0,
        max_f_number=4.5,
        min_field_angle=26.5,
        max_distortion=2.0,
    )

    design = LensDesign(
        efl=50.0,
        f_number=4.0,
        field_angle=27.0,
        distortion=3.5,
    )

    results = check_lens_design(spec, design)

    assert results["Distortion"]["pass"] is False