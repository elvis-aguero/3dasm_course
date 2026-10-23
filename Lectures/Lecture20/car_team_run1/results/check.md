# Model Recomputation Verification

## Summary
**Overall: PASS**

All recomputed values match the file values within tolerance (1e-6 relative).

## M1 Results

| Parameter | Recomputed | File Value | Relative Diff | Status |
|-----------|-----------|-----------|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| sd_parameter | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |
| n_train | 37 | 37 | - | PASS |
| n_test | 13 | 13 | - | PASS |

**Model M1: PASS**

Columns: model, a, b, sd_parameter, coverage, nll, n_train, n_test ✓

## M2 Results

| Parameter | Recomputed | File Value | Relative Diff | Status |
|-----------|-----------|-----------|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| sd_parameter | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.503770939937341 | 4.503770939937342 | 2.2e-16 | PASS |
| n_train | 37 | 37 | - | PASS |
| n_test | 13 | 13 | - | PASS |

**Model M2: PASS**

Columns: model, a, b, sd_parameter, coverage, nll, n_train, n_test ✓

## Implementation Details

- **Data**: Loaded from `data/car_stopping_distance` using `ExperimentData.from_file()`
- **Split**: `train_test_split(row index, train_size=0.75, random_state=1987)` yielded 37 training rows and 13 test rows
- **M1**: lstsq of y on [x, x²] (no intercept), sd_parameter = numpy.std(residuals, ddof=0)
- **M2**: lstsq of y/x on [1, x], sd_parameter = numpy.std(residuals, ddof=0)
- **Assessment**: Coverage and NLL computed on test rows with normal density assumption
- **Tolerance**: All relative differences ≤ 1e-6 ✓

## Verification Conclusion

✅ **OVERALL: PASS**

All models, parameters, and metrics have been independently recomputed and verified to match the file values exactly (within floating-point precision).
