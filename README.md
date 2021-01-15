XSteam2
-------

Original Released by Magnus Holmgren for Matlab and Excel:
<http://xsteam.sourceforge.net> and/or <http://www.x-eng.com>

Updated version of original XSteam code for properties of water and steam using IAPWS-97 (2012 Update)/IFC-97 
formulation. Also included are updated XLS files and .BAS files from the original XSteam Code.
The XLS and .BAS only contain the update to the Region 5 correlation.
The Python code contains all the new changes

Changes:
 * Jan 13, 2021
 * The conversions to bar and deg_C have been removed, all units are the same as the official specification
 * Equations added for metable vapor Region 2 but must be called directly
 * The coefficients for region 5 were updated to match most recent 2012 IAPWS 97 release
 * Iteration counters (max 1000 iterations) added to ensure no infinite loops when calling iterated properties
 * A self-test routine to check that calculated values match reference values in 2012 IAPWS 97 release (They do)
 * All arrays have been hoisted out of the functions so they not are created in each function call
 * If numba is not available, should use the list version

Performance:
 * Tested via running self-test 100 times
 * %timeit benchmark()
 * 1.22 s ± 34.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) (Without numba)
 * 79.6 ms ± 1.78 ms per loop (mean ± std. dev. of 7 runs, 10 loops each) (With numba) - 15.3 x speedup
 * Your performance will vary, but numba version should be significantly faster