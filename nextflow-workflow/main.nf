#!/usr/bin/env nextflow

/*
Enable DSL 2 syntax
*/

nextflow.enable.dsl = 2

/*

Define default parameters

*/

params.read1 = "${baseDir}/../datasets/H3A_VarCall_TestData/WES_chr1_50X_E0.005/WES_chr1_50X_E0.005_merged_read1.fq.gz"
params.read2 = "${baseDir}/../datasets/H3A_VarCall_TestData/WES_chr1_50X_E0.005/WES_chr1_50X_E0.005_merged_read2.fq.gz"
params.ref_seq = "${baseDir}/../datasets/H3A_VarCall_TestData/WES_chr1_50X_E0.005/HG19_GATKbundle2.8_noDecoys.noChrInName.fa.gz"

/*

Import modules here

*/

include {
    RUN_FASTQC;
    TRIM_SEQUENCES
} from "./modules.nf"


/*

Declare the main pipepline below:

*/

workflow {
    // Process 1: Quality controls
    RUN_FASTQC(params.read1, params.read2)
    TRIM_SEQUENCES(params.read1, params.read2)
}
