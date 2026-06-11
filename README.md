# optics-spec-checker

A simple Python tool for checking optical lens design specifications.

## Overview

`optics-spec-checker` is a lightweight Python project that helps users check whether an optical lens design satisfies basic design requirements.

It can evaluate key lens specifications such as:

- Effective focal length
- F-number
- Field angle
- Distortion

This project is designed for students, researchers, and beginners who are learning optical system design and want a simple way to verify lens design conditions.

## Features

- Check effective focal length tolerance
- Check maximum F-number
- Check minimum field angle
- Check maximum distortion
- Print a clear PASS / FAIL report
- Written in simple Python for easy learning and extension

## Example Output

```txt
Lens Specification Check Result
----------------------------------------
Effective Focal Length: 49.3 | Requirement: 48.00 mm ~ 52.00 mm | PASS
F-number: 4.2 | Requirement: <= 4.50 | PASS
Field Angle: 27.0 | Requirement: >= 26.50 deg | PASS
Distortion: 1.5 | Requirement: <= 2.00 % | PASS
----------------------------------------
Overall Result: PASS