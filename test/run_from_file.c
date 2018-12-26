#include "scs.h"
#include "rw.h"
#include "util.h"

/* Simple helper function to run problems from data files */
/* Mostly useful for debugging */
int main(int argc, char **argv) {
    ScsData *d;
    ScsCone *k;
    ScsSolution *sol;
    ScsInfo info = {0};
    if (argc < 2) {
      scs_printf("Need to specify a filename, exit.\n");
      return -1;
    }
    char * filename = argv[1];
    SCS(read_data)(filename, &d, &k);
    sol = scs_calloc(1, sizeof(ScsSolution));
    scs(d, k, sol, &info);
    SCS(free_data)(d, k);
    SCS(free_sol)(sol);
    return 0;
}

